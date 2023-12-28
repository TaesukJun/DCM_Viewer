from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import pygame
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
                                               NavigationToolbar2Tk) 
    
#####################################################################
#####################################################################






root = Tk()
root.title("DCM Image Analysis")
root.iconbitmap(r'Icons\analyst.ico')
root.geometry("900x600")

pygame.mixer.init()

###################################################################
###################################################################


def soundplay():
    pygame.mixer.music.load(r"Sounds\Nice.mp3")
    pygame.mixer.music.play(loops=0)

def soundstop():
    pygame.mixer.music.pause()

def clicked(value):
    global myLabel
    myLabel.destroy()
    myLabel = Label(frame_Result_01, text = value)
    myLabel.pack()

def Dir_Open_01():
    global file_directory
    e_01.delete(0, END)
    file_directory = filedialog.askdirectory(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File Directory",
        )
    e_01.insert(0, file_directory)
    
def Dir_Open_02():
    global file_directory
    e_02.delete(0, END)
    file_directory = filedialog.askdirectory(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File Directory",
        )
    e_02.insert(0, file_directory)

def Dir_Open_03():
    global file_directory
    e_03.delete(0, END)
    file_directory = filedialog.askdirectory(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File Directory",
        )
    e_03.insert(0, file_directory)    

def plot(): 
    fig = Figure(figsize = (4, 4), 
                 dpi = 100) 

    y = [i**2 for i in range(101)] 

    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
  
    canvas = FigureCanvasTkAgg(fig, frame_Result_01)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, frame_Result_01) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()

###################################################################
###################################################################





###################################################################
###################################################################

OnOff_MODES = [
    ("On","On"),
    ("Off","Off"),
    ]

Option_Set = [
    
    ( "ImageResultShow" ), ( "Image_BW\nResultShow" ), ( "ImgFigSave" ), 
    ( "Hist_Fig_Save" ), ( "Hist_Peak_Mark" ),
    ( "pptSave" )
    
    ]


Option_Var_01 = StringVar()
Option_Var_01.set("Off")
Option_Var_02 = StringVar()
Option_Var_02.set("Off")
Option_Var_03 = StringVar()
Option_Var_03.set("Off")
Option_Var_04 = StringVar()
Option_Var_04.set("Off")
Option_Var_05 = StringVar()
Option_Var_05.set("Off")
Option_Var_06 = StringVar()
Option_Var_06.set("Off")

Option_Var_11 = StringVar()
Option_Var_11.set("Off")

Frame_gap_x = 18
Frame_gap_y = 2

#####################################################################
#####################################################################

Label(root, text = "Options",).grid(row=0, column=0)

n = 0
frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_01 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_02 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_03 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_04 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_05 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_06 , value = mod ).pack(anchor=CENTER)
n = n + 1

#####################################################################
#####################################################################

frame_11 = LabelFrame(root, text="File Directory Setting", padx= 30, pady=5)
frame_11.grid(row=4, rowspan= 3, column=1,padx=20,pady=5)

myButton = Button(frame_11, text="Data Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_01)
myButton.pack()
e_01 = Entry(frame_11, width = 50, borderwidth = 3)
e_01.pack(pady=(0,10))
e_01.insert(0,r"C:\Users\taesu\OneDrive - purdue.edu\Tjun_231114_PEG_additive\PEG_additive\CT_20231114_104928\Sample_1_20231114_104928")

myButton = Button(frame_11, text="Image Save Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_02)
myButton.pack()
e_02 = Entry(frame_11, width = 50, borderwidth = 3)
e_02.pack(pady=(0,10))
e_02.insert(0,"C:\JunDrive\Mouse_data\Fig_data")

myButton = Button(frame_11, text="Histogram Plot Save Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_03)
myButton.pack()
e_03 = Entry(frame_11, width = 50, borderwidth = 3)
e_03.pack(pady=(0,10))
e_03.insert(0,"C:\JunDrive\Mouse_data\Histogram_Plot_data")





#####################################################################
#####################################################################


frame_12 = LabelFrame(root, text="Image Analysis Setting", padx= 30, pady=5)
frame_12.grid(row=0, rowspan= 3, column=1,padx=20,pady=5)


Label(frame_12, text = "Filter On/Off", bg = "#90EE90",
      borderwidth = 3
      ).grid(row=0,column=4)
n = 1
for text, mod in OnOff_MODES:
    Radiobutton(frame_12, text=text, variable=Option_Var_11 , value = mod 
                ).grid(row=n, column=4)
    n = n + 1



Label(frame_12, text = "Intensity Filter (Higher Num in red)"
      ).grid(row=0,column=0,columnspan=3)

Label(frame_12, text = "Upper Int. Bound ="
      ).grid(row=1,column=0)
e_11 = Entry(frame_12, width = 12, borderwidth = 3,
             bg = "#F05650"
      )
e_11.grid(row=1,column=1,columnspan=2)
e_11.insert(0,"3700")

Label(frame_12, text = "Lower Int. Bound ="
      ).grid(row=2,column=0)
e_12 = Entry(frame_12, width = 12, borderwidth = 3,
             bg = "light blue"
      )
e_12.grid(row=2,column=1,columnspan=2)
e_12.insert(0,"3240")

Label(frame_12, text = "Area of Interest (FOV)"
      ).grid(row=3,column=0,columnspan=3, pady=(10,0))

Label(frame_12, text = "Horizontal From/To(pixel) = "
      ).grid(row=4,column=0)
e_13 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "light blue"
      )
e_13.grid(row=4,column=1)
e_13.insert(0,"200")
e_14 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#F05650"
      )
e_14.grid(row=4,column=2)
e_14.insert(0,"400")

Label(frame_12, text = "Vertical From/To(pixel) = "
      ).grid(row=5,column=0)
e_15 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "light blue" 
      )
e_15.grid(row=5,column=1)
e_15.insert(0,"140")
e_16 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#F05650"
      )
e_16.grid(row=5,column=2)
e_16.insert(0,"365")


Label(frame_12, text = "File Analysis Index Number"
      ).grid(row=6,column=0,columnspan=4, pady=(10,0))
Label(frame_12, text = "Start/End/Bin ="
      ).grid(row=7,column=0)


e_17 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "light blue" 
      )
e_17.grid(row=7,column=1)
e_17.insert(0,"270")

e_18 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "#F05650"
      )
e_18.grid(row=7,column=2)
e_18.insert(0,"330")

e_19 = Entry(frame_12, width = 4, borderwidth = 3,
             bg = "#CF9FFF"
      )
e_19.grid(row=7,column=3)
e_19.insert(0,"10")


#####################################################################
#####################################################################



frame_Result_01 = LabelFrame(root, text="Analyze")
frame_Result_01.grid(row=0,column=2,rowspan=len(Option_Set), padx=20,pady=20)


my_button = Button(frame_Result_01, text="Play", font = ("Times new roman",12),
       padx = 20, pady = 5,
       command=plot
                   ).pack()


#####################################################################
#####################################################################


Dialog_Index_Row = 0
Dialog_Index_Col = 3


my_button = Button(root, text="Nice", font = ("Times new roman",12),
       padx = 20, pady = 5,
       command=soundplay
                   ).grid(
                       row=Dialog_Index_Row+0, column=Dialog_Index_Col+0, 
                       padx = 10, pady = 5
                       )









"""
stop_button = Button(
    root, text="Stop", font = ("Times new roman",32),
    padx = 20, pady = 20,
    command=soundstop
    
    ).pack(padx = 20, pady = 20)
"""





mainloop()