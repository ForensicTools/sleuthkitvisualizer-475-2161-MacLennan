#!/usr/bin/python
#
#************
#Author: Eyan MacLennan
#Filename: gui.py
#This program is to be a gui application for the Sleuth Kit
#************
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
#
#Tools Section
#
#*********************************************************************#


c1 = tkinter.Checkbutton(window, text = "Istat", \
    variable = istat, height = 3, width = 20)#creates checkbox for istat command 

#*****
#File system layer tools
#*****

fslt1 = tkinter.Checkbutton(window, text = "FSStat", \
    variable = fsstat, height = 3, width = 20)#creates checkbox for fsstat command 

#*****
#File name layer tools
#*****

fnlt1 = tkinter.Checkbutton(window, text = "FLS", \
    variable = fls, height = 3, width = 20)#creates checkbox for fls command 

fnlt2 = tkinter.Checkbutton(window, text = "FFIND", \
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

fat1 = tkinter.Checkbutton(window, text = "TSK CompareDir", \
    variable = tsk_comparedir, height = 3, width = 20)#creates checkbox for tsk_comparedir command 

fat2 = tkinter.Checkbutton(window, text = "TSK GetTimes", \
    variable = tsk_gettimes, height = 3, width = 20)#creates checkbox for tsk_gettimes command 


fat3 = tkinter.Checkbutton(window, text = "TSK Load DB", \
    variable = tsk_loaddb, height = 3, width = 20)#creates checkbox for tsk_loaddb command 

fat4 = tkinter.Checkbutton(window, text = "TSK Recover", \
    variable = tsk_recover, height = 3, width = 20)#creates checkbox for tsk_recover command 



#*****
#Image File Tools
#*****

ift1 = tkinter.Checkbutton(window, text = "IMG Stat", \
    variable = img_stat, height = 3, width = 20)#creates checkbox for img_stat command 


ift2 = tkinter.Checkbutton(window, text = "IMG Cat", \
    variable = img_cat, height = 3, width = 20)#creates checkbox for img_cat command 

#*******
#Making the grid pattern
#*******

toolsLabel = tkinter.Label(text="Tools", font='Helvetica 14 bold')
fsltLabel = tkinter.Label(text="File System Layer Tools", font='Helvetica 14 bold')
fnltLabel = tkinter.Label(text="File Name Layer Tools", font='Helvetica 14 bold')
blahLabel = tkinter.Label(text="Blah tools", font='Helvetica 14 bold')
fatLabel = tkinter.Label(text="Fully Automated Tools", font='Helvetica 14 bold')
iftLabel = tkinter.Label(text="Image File Tools",font='Helvetica 14 bold')

toolsLabel.grid(row=0, columnspan=4)

c1.grid(row=1, column=0, sticky='E')

fsltLabel.grid(row=2, columnspan=4)
fslt1.grid(row=3, column=0, sticky='E')

fnltLabel.grid(row=4, columnspan=4)
fnlt1.grid(row=5, column=0, sticky='E')
fnlt2.grid(row=5, column=1, sticky='E')

blahLabel.grid(row=6, columnspan=4)
c5.grid(row=7, column=0, sticky='E')
c6.grid(row=7, column=1,sticky='E')

fatLabel.grid(row=8, columnspan=4)
fat1.grid(row=9, column=0, sticky='E')
fat2.grid(row=9, column=1, sticky='E')
fat3.grid(row=9, column=2, sticky='E')
fat4.grid(row=9, column=3, sticky='E')

iftLabel.grid(row=10, columnspan=4)
ift1.grid(row=11, column=0, sticky='E')
ift2.grid(row=11, column=1, sticky='E')



window.mainloop()                       #runs the tkinter window
