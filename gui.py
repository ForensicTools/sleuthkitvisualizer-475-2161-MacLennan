#!/usr/bin/python
import tkinter
import os
istat = "/bin/istat.exe"
fsstat = "/bin/fsstat.exe"
fls = "/bin/fls.exe"
ffind = "/bin/ffind.exe"
fcat = "/bin/fcat.ext"
icat = "/bin/icat.exe"


window = tkinter.Tk()                   #initialized the window for tkinter
window.wm_title("Sleuth Kit Visualizer")#sets the title for the "window"
c1 = tkinter.Checkbutton(window, text = "Istat", \
    variable = istat, height = 5, width = 20)#creates checkbox for istat command 

c2 = tkinter.Checkbutton(window, text = "FSStat", \
    variable = fsstat, height = 5, width = 20)#creates checkbox for fsstat command 


c3 = tkinter.Checkbutton(window, text = "FLS", \
    variable = fls, height = 5, width = 20)#creates checkbox for fls command 

c4 = tkinter.Checkbutton(window, text = "FFIND", \
    variable = ffind, height = 5, width = 20)#creates checkbox for ffind command 


c5 = tkinter.Checkbutton(window, text = "FCat", \
    variable = fcat, height = 5, width = 20)#creates checkbox for fcat command 


c6 = tkinter.Checkbutton(window, text = "Icat", \
    variable = icat, height = 5, width = 20)#creates checkbox for icat command 


c1.pack()   #packs the checkbox
c2.pack()
c3.pack()
c4.pack()
c5.pack()
c6.pack()

window.mainloop()                       #runs the tkinter window
