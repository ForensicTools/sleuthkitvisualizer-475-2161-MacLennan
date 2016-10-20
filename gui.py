#!/usr/bin/python
import tkinter
import os
istat = "/bin/istat.exe"
fsstat = "/bin/fsstat.exe"
fls = "/bin/fls.exe"
ffind = "/bin/ffind.exe"
fcat = "/bin/fcat.ext"
icat = "/bin/icat.exe"
tsk_recover = "/bin/tsk_recover.exe"
tsk_loaddb = "/bin/tsk_loaddb.exe"
tsk_gettimes = "/bin/tsk_gettimes.exe"
tsk_comparedir = "/bin/tsk_comparedir.exe"
img_stat = "/bin/img_stat.exe"
img_cat = "/bin/img_cat.exe"

window = tkinter.Tk()                   #initialized the window for tkinter
window.wm_title("Sleuth Kit Visualizer")#sets the title for the "window"


#*********************************************************************#
#								      #
#Tools Section							      #
#								      #
#*********************************************************************#


c1 = tkinter.Checkbutton(window, text = "Istat", \
    variable = istat, height = 3, width = 20)#creates checkbox for istat command 

#*****
#File system layer tools
#*****

c2 = tkinter.Checkbutton(window, text = "FSStat", \
    variable = fsstat, height = 3, width = 20)#creates checkbox for fsstat command 

#*****
#File name layer tools
#*****

c3 = tkinter.Checkbutton(window, text = "FLS", \
    variable = fls, height = 3, width = 20)#creates checkbox for fls command 

c4 = tkinter.Checkbutton(window, text = "FFIND", \
    variable = ffind, height = 3, width = 20)#creates checkbox for ffind command 

#*****
#
#*****

c5 = tkinter.Checkbutton(window, text = "FCat", \
    variable = fcat, height = 3, width = 20)#creates checkbox for fcat command 


c6 = tkinter.Checkbutton(window, text = "Icat", \
    variable = icat, height = 3, width = 20)#creates checkbox for icat command 

#*****
#Fully automated tools
#*****

c7 = tkinter.Checkbutton(window, text = "TSK CompareDir", \
    variable = tsk_comparedir, height = 3, width = 20)#creates checkbox for tsk_comparedir command 

c8 = tkinter.Checkbutton(window, text = "TSK GetTimes", \
    variable = tsk_gettimes, height = 3, width = 20)#creates checkbox for tsk_gettimes command 


c9 = tkinter.Checkbutton(window, text = "TSK Load DB", \
    variable = tsk_loaddb, height = 3, width = 20)#creates checkbox for tsk_loaddb command 

c10 = tkinter.Checkbutton(window, text = "TSK Recover", \
    variable = tsk_recover, height = 3, width = 20)#creates checkbox for tsk_recover command 



#*****
#Image File Tools
#*****

c11 = tkinter.Checkbutton(window, text = "IMG Stat", \
    variable = img_stat, height = 3, width = 20)#creates checkbox for img_stat command 


c12 = tkinter.Checkbutton(window, text = "IMG Cat", \
    variable = img_cat, height = 3, width = 20)#creates checkbox for img_cat command 

c1.pack()   #packs the checkbox
c2.pack()
c3.pack()
c4.pack()
c5.pack()
c6.pack()
c7.pack()   #packs the checkbox
c8.pack()
c9.pack()
c10.pack()
c11.pack()
c12.pack()

window.mainloop()                       #runs the tkinter window
