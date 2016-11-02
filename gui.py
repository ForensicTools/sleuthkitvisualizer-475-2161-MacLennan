#!/usr/bin/python
#
#************
#Author: Ryan MacLennan
#Filename: gui.py
#This program is to be a gui application for the Sleuth Kit
#************
import tkinter
import os
istat = "/bin/istat.exe"
fsstat = "/bin/fsstat.exe"
fls = "/bin/fls.exe"
ffind = "/bin/ffind.exe"
fcat = "/bin/fcat.exe"
icat = "/bin/icat.exe"
tsk_recover = "/bin/tsk_recover.exe"
tsk_loaddb = "/bin/tsk_loaddb.exe"
tsk_gettimes = "/bin/tsk_gettimes.exe"
tsk_comparedir = "/bin/tsk_comparedir.exe"
img_stat = "/bin/img_stat.exe"
img_cat = "/bin/img_cat.exe"
ils = "/bin/ils.exe"
ifind = "/bin/ifind.exe"
icat = "/bin/icat.exe"
blkcat = "/bin/blkcat.exe"
blkls = "/bin/blkls.exe"
blkstat = "/bin/blkstat.exe"
blkcalc = "/bin/blkcalc.exe"
jcat = "/bin/jcat.exe"
jls = "/bin/jls.exe"
mmls = "/bin/mmls.exe"
mmcat = "/bin/mmcat.exe"
mmstat = "/bin/mmstat.exe"

window = tkinter.Tk()                   #initialized the window for tkinter
window.wm_title("Sleuth Kit Visualizer")#sets the title for the "window"


#*********************************************************************#
#
#Tools Section
#
#*********************************************************************#


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
#Meta Data Layer Tools
#*****

mdlt1 = tkinter.Checkbutton(window, text = "Icat", \
    variable = icat, height = 3, width = 20)#creates checkbox for icat command

mdlt2 = tkinter.Checkbutton(window, text = "Istat", \
    variable = istat, height = 3, width = 20)#creates checkbox for istat command

mdlt3 = tkinter.Checkbutton(window, text = "ILS", \
    variable = ils, height = 3, width = 20)#creates checkbox for ils command

mdlt4 = tkinter.Checkbutton(window, text = "IFind", \
    variable = ifind, height = 3, width = 20)#creates checkbox for ifind command


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
#Data Unit Layer Tools
#*******

dult1 = tkinter.Checkbutton(window, text = "FCat", \
    variable = fcat, height = 3, width = 20)#creates checkbox for fcat command

dult2 = tkinter.Checkbutton(window, text = "BLKcat", \
    variable = blkcat, height = 3, width = 20)#creates checkbox for blkcat command

dult3 = tkinter.Checkbutton(window, text = "BLKls", \
    variable = blkls, height = 3, width = 20)#creates checkbox for blkls command

dult4 = tkinter.Checkbutton(window, text = "BLKstat", \
    variable = blkstat, height = 3, width = 20)#creates checkbox for blkstat command

dult5 = tkinter.Checkbutton(window, text = "BLKcalc", \
    variable = blkcalc, height = 3, width = 20)#creates checkbox for fcat command

#*******
#File System Journal Tools
#*******
fsjt1 = tkinter.Checkbutton(window, text = "JCAT", \
    variable = jcat, height = 3, width = 20)#creates checkbox for fcat command

fsjt2 = tkinter.Checkbutton(window, text = "JLS", \
    variable = jls, height = 3, width = 20)#creates checkbox for fcat command

#*******
#Volume System Tools
#*******
vst1 = tkinter.Checkbutton(window, text = "MMLS", \
    variable = mmls, height = 3, width = 20)#creates checkbox for fcat command

vst2 = tkinter.Checkbutton(window, text = "MMStat", \
    variable = mmstat, height = 3, width = 20)#creates checkbox for fcat command

vst3 = tkinter.Checkbutton(window, text = "MMCat", \
    variable = mmcat, height = 3, width = 20)#creates checkbox for fcat command

#*******
#Making the grid pattern
#*******

toolsLabel = tkinter.Label(text="Tools", font='Helvetica 14 bold')
fsltLabel = tkinter.Label(text="File System Layer Tools", font='Helvetica 14 bold')
fnltLabel = tkinter.Label(text="File Name Layer Tools", font='Helvetica 14 bold')
dultLabel = tkinter.Label(text="Data Unit Layer Tools", font='Helvetica 14 bold')
fatLabel = tkinter.Label(text="Fully Automated Tools", font='Helvetica 14 bold')
iftLabel = tkinter.Label(text="Image File Tools",font='Helvetica 14 bold')
mdltLabel = tkinter.Label(text="Meta Data Layer Tools", font='Helvetica 14 bold')
fsjtLabel = tkinter.Label(text="File System Journal Tools", font='Helvetica 14 bold')
vstLabel = tkinter.Label(text="Volume System Tools", font = 'Helvetica 14 bold')

toolsLabel.grid(row=0, columnspan=5)

fsltLabel.grid(row=2, columnspan=5)
fslt1.grid(row=3, column=0)

fnltLabel.grid(row=4, columnspan=5)
fnlt1.grid(row=5, column=0)
fnlt2.grid(row=5, column=1)

dultLabel.grid(row=6, columnspan=5)
dult1.grid(row=7, column=0)
dult2.grid(row=7, column=1)
dult3.grid(row=7, column=2)
dult4.grid(row=7, column=3)
dult5.grid(row=7, column=4)

fatLabel.grid(row=8, columnspan=5)
fat1.grid(row=9, column=0)
fat2.grid(row=9, column=1)
fat3.grid(row=9, column=2)
fat4.grid(row=9, column=3)

iftLabel.grid(row=10, columnspan=5)
ift1.grid(row=11, column=0)
ift2.grid(row=11, column=1)

mdltLabel.grid(row=12, columnspan=5)
mdlt1.grid(row=13, column=0)
mdlt2.grid(row=13, column=1)
mdlt3.grid(row=13, column=2)
mdlt4.grid(row=13, column=3)

fsjtLabel.grid(row=14, columnspan=5)
fsjt1.grid(row=15, column=0, columnspan=2)
fsjt2.grid(row=15, column=3, columnspan=2)

vstLabel.grid(row=16, columnspan=5)
vst1.grid(row=17, column=0)
vst2.grid(row=17, column=1)
vst3.grid(row=17, column=2)

#e = tkinter.Entry(tkinter)
#e.grid(row=18, column=4)
#Adding next buttont o go next frame for the options of each command
b = tkinter.Button(text="Next", width=15)
b.grid(row=18, columnspan=5)

window.mainloop()                       #runs the tkinter window
