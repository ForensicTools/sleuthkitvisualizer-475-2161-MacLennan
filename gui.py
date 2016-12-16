#!/usr/bin/python
#
# ************
# Author: Ryan MacLennan
# Filename: gui.py
# This program is to be a gui application for the Sleuth Kit
# ************
import tkinter as tk
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

window = tk.Tk()  # initialized the window for tk
window.wm_title("Sleuth Kit Visualizer")  # sets the title for the "window"

commandList = []

def listAppend(command):
    commandList.append(command)
    print(commandList)


# *********************************************************************#
#
# Tools Section
#
# *********************************************************************#


# *****
# File system layer tools
# *****

fslt1 = tk.Button(window, text="FSStat", command = lambda: listAppend(fsstat))  # creates checkbox for fsstat command

# *****
# File name layer tools
# *****

fnlt1 = tk.Button(window, text="FLS", command = lambda: listAppend(fls))  # creates checkbox for fls command

fnlt2 = tk.Button(window, text="FFIND", command = lambda: listAppend(ffind))  # creates checkbox for ffind command

# *****
# Meta Data Layer Tools
# *****

mdlt1 = tk.Button(window, text="Icat", command = lambda: listAppend(icat))  # creates checkbox for icat command

mdlt2 = tk.Button(window, text="Istat", command = lambda: listAppend(istat))  # creates checkbox for istat command

mdlt3 = tk.Button(window, text="ILS", command = lambda: listAppend(ils))  # creates checkbox for ils command

mdlt4 = tk.Button(window, text="IFind", command = lambda: listAppend(ifind))  # creates checkbox for ifind command

# *****
# Fully automated tools
# *****

fat1 = tk.Button(window, text="TSK CompareDir", command = lambda: listAppend(tsk_comparedir))  # creates checkbox for tsk_comparedir command

fat2 = tk.Button(window, text="TSK GetTimes", command = lambda: listAppend(tsk_gettimes))  # creates checkbox for tsk_gettimes command

fat3 = tk.Button(window, text="TSK Load DB", command = lambda: listAppend(tsk_loaddb))  # creates checkbox for tsk_loaddb command

fat4 = tk.Button(window, text="TSK Recover", command = lambda: listAppend(tsk_recover))  # creates checkbox for tsk_recover command

# *****
# Image File Tools
# *****

ift1 = tk.Button(window, text="IMG Stat", command = lambda: listAppend(img_stat))  # creates checkbox for img_stat command

ift2 = tk.Button(window, text="IMG Cat", command = lambda: listAppend(img_cat))  # creates checkbox for img_cat command

# *******
# Data Unit Layer Tools
# *******

dult1 = tk.Button(window, text="FCat", command = lambda: listAppend(fcat))  # creates checkbox for fcat command

dult2 = tk.Button(window, text="BLKcat", command = lambda: listAppend(blkcat))  # creates checkbox for blkcat command

dult3 = tk.Button(window, text="BLKls", command = lambda: listAppend(blkls))  # creates checkbox for blkls command

dult4 = tk.Button(window, text="BLKstat", command = lambda: listAppend(blkstat))  # creates checkbox for blkstat command

dult5 = tk.Button(window, text="BLKcalc", command = lambda: listAppend(blkcalc))  # creates checkbox for fcat command

# *******
# File System Journal Tools
# *******
fsjt1 = tk.Button(window, text="JCAT", command = lambda: listAppend(jcat))  # creates checkbox for fcat command

fsjt2 = tk.Button(window, text="JLS", command = lambda: listAppend(jls))  # creates checkbox for fcat command

# *******
# Volume System Tools
# *******
vst1 = tk.Button(window, text="MMLS", command = lambda: listAppend(mmls))  # creates checkbox for fcat command

vst2 = tk.Button(window, text="MMStat", command = lambda: listAppend(mmstat))  # creates checkbox for fcat command

vst3 = tk.Button(window, text="MMCat", command = lambda: listAppend(mmcat))  # creates checkbox for fcat command

# *******
# Making the grid pattern
# *******



# Labels
toolsLabel = tk.Label(text="Tools", font='Helvetica 14 bold')
fsltLabel = tk.Label(text="File System Layer Tools", font='Helvetica 14 bold')
fnltLabel = tk.Label(text="File Name Layer Tools", font='Helvetica 14 bold')
dultLabel = tk.Label(text="Data Unit Layer Tools", font='Helvetica 14 bold')
fatLabel = tk.Label(text="Fully Automated Tools", font='Helvetica 14 bold')
iftLabel = tk.Label(text="Image File Tools", font='Helvetica 14 bold')
mdltLabel = tk.Label(text="Meta Data Layer Tools", font='Helvetica 14 bold')
fsjtLabel = tk.Label(text="File System Journal Tools", font='Helvetica 14 bold')
vstLabel = tk.Label(text="Volume System Tools", font='Helvetica 14 bold')

toolsLabel.grid(row=0, columnspan=5)

fsltLabel.grid(row=2, columnspan=5)
#fslt1.bind("<LEFT>", listAppend(fsstat))
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

# e = tk.Entry(tk)
# e.grid(row=18, column=4)
# Adding next buttont o go next frame for the options of each command
b = tk.Button(text="Next", width=15)
b.grid(row=18, columnspan=5)

window.mainloop()  # runs the tk window
