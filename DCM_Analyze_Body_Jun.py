################################# setting ###########################

import numpy as np
import pandas as pd
import fnmatch
import os
import torch
from torchvision.io import read_image
from sklearn.model_selection import train_test_split
import pydicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
import statistics


import datetime


import imageio.v3 as iio
import ipympl
import skimage as ski


#import plotly.graph_objects as go

import scipy

from scipy import signal
from scipy.optimize import curve_fit
from scipy.signal import find_peaks, peak_prominences
from lmfit.models import LorentzianModel, QuadraticModel, LinearModel, VoigtModel, GaussianModel
#Download lmfit
#pip install lmfit


from pptx import Presentation
from pptx.util import Cm, Inches, Pt


def cm_to_inch(value):
    return value/2.54




def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def add_peak1(prefix, center, amplitude=0.002, sigma=0.0075):
    peak = GaussianModel(prefix=prefix)
    pars = peak.make_params()
    pars[prefix + 'center'].set(center, max=center*(1+PeakVariance), min=center*(1-PeakVariance))
    pars[prefix + 'amplitude'].set(amplitude, min=0)
    pars[prefix + 'sigma'].set(sigma, max=setsigma, min=0)
    return peak, pars



############################################################
############################################################


FileDir = r"C:\Users\taesu\OneDrive - purdue.edu\Tjun_231114_PEG_additive\PEG_additive\CT_20231114_104928\Sample_1_20231114_104928"
FileDir = FileDir.replace(os.sep,"/")
FileDir = FileDir + "/"
FileDir = FileDir.replace('\\','/')

e = datetime.datetime.now()

Img_Save_Path = "C:\JunDrive\Mouse_data\Fig_data"
Date_Index = "/%s%02d%02d%02d%02d%02d" % (e.year, e.month, e.day, e.hour, e.minute, e.second)
os.mkdir(Img_Save_Path + Date_Index + "_img")
Img_Save_Path = Img_Save_Path + Date_Index + "_img"
print(Img_Save_Path)
Img_Save_Path = Img_Save_Path + "/"
Img_Save_Path = Img_Save_Path.replace('\\','/')


PlotFig_Save_Path = "C:\JunDrive\Mouse_data\Histogram_Plot_data"
os.mkdir(PlotFig_Save_Path + Date_Index + "_plot")
PlotFig_Save_Path = PlotFig_Save_Path + Date_Index + "_plot"
PlotFig_Save_Path = PlotFig_Save_Path + "/"
PlotFig_Save_Path = PlotFig_Save_Path.replace('\\','/')




##############################################################
###### Intensity Filter ##########
##############################################################

Filt_On = 'no'
#Filt_On = 'yes'

UpImgBound = 3700
DownImgBound = 3240

##############################################################
########## Image Focuse ##########
##############################################################

ImgFocusH = (200, 400)
ImgFocusW = (140, 365)


##############################################################
########## Image Result & Save Option ##########
##############################################################

## Caution: If you set yes on Show Option, there will be long results

ImageResultShow = 'no'
#ImageResultShow = 'yes'

Image_BW_ResultShow = 'no'
#ImageResultShow = 'yes'

# Images will be saved as Black & White images ####
ImgFigSave = 'no'
#ImgFigSave = 'yes'

Hist_Fig_Save = 'no'
#Hist_Fig_Save = 'yes'

Hist_Peak_Mark = 'no'
#Hist_Peak_Mark = 'yes'

pptSave = 'no'
#pptSave = 'yes'



##############################################################

FileNumStart, FileNumEnd, IntervalFile = (280, 320, 13)

##############################################################



print('File Directory :\n', FileDir)
#img_id = r"19-no-samp2_20_20230928(2)_163702_3DFilter(Soft)_0281"


Num = 1

for FileIndex in range(FileNumStart,FileNumEnd+1,IntervalFile):
    print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")
    
    FileIndex2 = ("%04d" %(FileIndex))
    print(FileIndex2)
    SelectData = "*_"+FileIndex2+"*"
    OtherwayData = find(SelectData, FileDir)
    print(OtherwayData)
    #data = np.loadtxt("%s" %(OtherwayData[0]), comments = '%',delimiter=",")
    #print(data)
    
    ###################################################################
    
    dcm_img = pydicom.dcmread(OtherwayData[0], force=True)
    img_array = dcm_img.pixel_array

    if ImageResultShow == 'yes':
        fig, ax = plt.subplots()
        im = plt.imshow(img_array)
        fig.colorbar(im)
        plt.clim(3000,6000)

        plt.show()

    ##################################################################
    if Filt_On =='yes':
        np.place(img_array, img_array > UpImgBound, 0)
        np.place(img_array, img_array < DownImgBound, 0)

    if ImageResultShow == 'yes':
        fig, ax = plt.subplots()
        im = plt.imshow(img_array)
        fig.colorbar(im)
        #plt.clim(3000,6000)
        plt.show()

    ##################################################################
  
    
    img_array_selection = img_array[ImgFocusH[0]:ImgFocusH[1], 140:365]

    if ImageResultShow == 'yes':
        fig, ax = plt.subplots()
        im = plt.imshow(img_array_selection)
        fig.colorbar(im)
        plt.clim(3000,6000)
        plt.show()

    ##################################################################  
    
    img_array_bw = ski.util.img_as_float(img_array_selection)
    
    if Image_BW_ResultShow == 'yes':
        fig, ax = plt.subplots()
        im = plt.imshow(img_array_bw, cmap ="gray")

        fig.colorbar(im)
        plt.clim(0.02,0.09)
        plt.show()

        if ImgFigSave == 'yes':
            e = datetime.datetime.now()
            fig.savefig(Img_Save_Path + "%s_bw_Index%04d_%s%02d%02d%02d%02d%02d.png"
                        % (FileIndex2, Num, e.year, e.month, e.day,e.hour, e.minute, e.second))
        
        
    #print(img_array_selection)
    
    #Count = len([k for k in img_array_selection if k.any() > 0.01])
    Temp_img = img_array_selection
    Temp_img[Temp_img>0] = 1
    Temp_img[Temp_img<0] = 0
    
    Count = np.sum(Temp_img)
    print("Visuable Area : ",Count)
    
    ##################################################################
    if Filt_On =='yes':
        xscalerange = [0.048 , 0.060]
    else:
        xscalerange = [0.04 , 0.09]
        
        
        
    histogram, bin_edges = np.histogram(img_array_bw, bins=256, range=(xscalerange[0], xscalerange[1]))
    #histogram[0]=0
    #histogram = histogram / max(histogram)



    histogram = signal.savgol_filter(histogram,23,3)  

    x = bin_edges[0:-1]
    y = histogram
    y[y<0] = 0
    
    
    #print(histogram)
    if Image_BW_ResultShow == 'yes':

        plt.xlim([xscalerange[0], xscalerange[1]]) 


        fig, ax = plt.subplots()

        plt.title("Grayscale Histogram")
        plt.xlabel("grayscale value")
        plt.ylabel("pixel count")
        plt.xlim([xscalerange[0], xscalerange[1]])  # <- named arguments do not work here
        #plt.ylim([0.00, 1.0])
      
    
        plt.plot(x, y)  # <- or here
        plt.show()
        
        
        
        
        if ImgFigSave == 'yes':
            e = datetime.datetime.now()
            fig.savefig(PlotFig_Save_Path + "%s_bw_Index%04d_%s%02d%02d%02d%02d%02d.png"
                        % (FileIndex2, Num, e.year, e.month, e.day,e.hour, e.minute, e.second))

    if FileIndex == FileNumStart:
        hist_data = [x,y]
        #hist_data = np.transpose(hist_data)
        
    else:
        hist_data = np.append(hist_data,[y], axis=0)

    
    Num = Num + 1
    
    
#######################################################################

total_hist_num = np.shape(hist_data)
    
avg_hist_data = np.average(hist_data[1:total_hist_num[0],:], axis=0)

hist_data = np.append(hist_data,[avg_hist_data], axis=0)

hist_data = np.transpose(hist_data)
#print(hist_data)

if Hist_Fig_Save == 'yes':
    name = 'Avg_Histogram'
    e = datetime.datetime.now()
    ExportFileName = ("%s%02d%02d_%s_data_%02d%02d%02d.csv" % (e.year, e.month, e.day, name, e.hour, e.minute, e.second))
    pd.DataFrame(hist_data).to_csv(PlotFig_Save_Path + ExportFileName, index = False)

print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
    
plt.xlim([xscalerange[0], xscalerange[1]]) 


fig, ax = plt.subplots()

plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([xscalerange[0], xscalerange[1]])  # <- named arguments do not work here
#plt.ylim([0.00, 1.0])
      
x = hist_data[:,0]
y = hist_data[:,total_hist_num[0]]


    
plt.plot(x, y)  # <- or here




fitGmin = 0.04
fitGmax = 0.07
PeakHeightAllowFactor = 25
PeakBroadnessAllowFactor = 1


        
fitrange = [i for i, value in enumerate(x) if (value > fitGmin) * (value < fitGmax)]

x2 = x[fitrange]
y2 = y[fitrange]
y2 = y2[~np.isnan(y2)]

peaks, properties = find_peaks(y2, prominence = PeakHeightAllowFactor, width = PeakBroadnessAllowFactor)
prominences = peak_prominences(y2, peaks)[0]

roughfitq = x2[peaks]

#plt.plot(x2[peaks], y2[peaks], "rx",markersize = 10, markeredgewidth = 3)

plt.show()

MaxNumPeaksUse = 3

model = LinearModel(prefix='bkg_')
params = model.make_params(a=0, b=0)
    
rough_peak_positions = roughfitq[0:MaxNumPeaksUse]


PeakVariance = 0.1
setsigma = 0.3

for i, cen in enumerate(rough_peak_positions):
    peak, pars = add_peak1('lz%d_' % (i+1), cen)
    model = model + peak
    params.update(pars)

init = model.eval(params, x=x)
result = model.fit(y, params, x=x)

comps = result.eval_components()



peakdata02 = []
peakdata01 = []
    

    
for name, par in result.params.items():
    if 'center' in name:
        peakdata02 = np.array([name, par.value])
        peakdata01 = np.hstack((peakdata01,peakdata02))
for name, par in result.params.items():
    if 'height' in name:
        peakdata02 = np.array([name, par.value])
        peakdata01 = np.hstack((peakdata01,peakdata02))
            
for name, par in result.params.items():
    if 'fwhm' in name:
        peakdata02 = np.array([name, par.value])
        peakdata01 = np.hstack((peakdata01,peakdata02))
    
for name, par in result.params.items():
    if 'amplitude' in name:
        peakdata02 = np.array([name, par.value])
        peakdata01 = np.hstack((peakdata01,peakdata02))


n = 1
amp = []
for name, par in result.params.items():
    if 'amplitude' in name:
        if n == 1:
            amp = par.value
            print("  %s: value = %f" % (name, par.value))
            n = n + 1
        else:
            print("  %s: value = %f" % (name, par.value))
            amp = np.append(amp, par.value)
            n = n + 1
        
        
        
        
        
fig = plt.figure(figsize=(12,12)) 

plt.plot(x, y, label='data')
plt.plot(x, result.best_fit, label='best fit')
for name, comp in comps.items():
    #plt.semilogy(xdat, comp, '--', label=name)
    plt.plot(x, comp, '--', label=name)
plt.legend(loc='upper right')

plt.plot(x2[peaks], y2[peaks], "rx",markersize = 10, markeredgewidth = 3)
plt.show()









