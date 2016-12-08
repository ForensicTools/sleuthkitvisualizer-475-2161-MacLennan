#!/usr/bin/python
import os

# ************
# Author: Ryan MacLennan
# Filename: visualizer.py
# This file is the command line version of the gui.
# It will also ask if you want to run the gui version as well.
# ************


#windows command path
istat = "\\sleuthkit-4.3.0-win32\\bin\\istat.exe "
fsstat = "\\sleuthkit-4.3.0-win32\\bin\\fsstat.exe "
fls = "\\sleuthkit-4.3.0-win32\\bin\\fls.exe "
ffind = "\\sleuthkit-4.3.0-win32\\bin\\ffind.exe "
fcat = "\\sleuthkit-4.3.0-win32\\bin\\fcat.exe "
icat = "\\sleuthkit-4.3.0-win32\\bin\\icat.exe "
tsk_recover = "\\sleuthkit-4.3.0-win32\\bin\\tsk_recover.exe "
tsk_loaddb = "\\sleuthkit-4.3.0-win32\\bin\\tsk_loaddb.exe "
tsk_gettimes = "\\sleuthkit-4.3.0-win32\\bin\\tsk_gettimes.exe "
tsk_comparedir = "\\sleuthkit-4.3.0-win32\\bin\\tsk_comparedir.exe "
img_stat = "\\sleuthkit-4.3.0-win32\\bin\\img_stat.exe "
img_cat = "\\sleuthkit-4.3.0-win32\\bin\\img_cat.exe "
ils = "\\sleuthkit-4.3.0-win32\\bin\\ils.exe "
ifind = "\\sleuthkit-4.3.0-win32\\bin\\ifind.exe "
blkcat = "\\sleuthkit-4.3.0-win32\\bin\\blkcat.exe "
blkls = "\\sleuthkit-4.3.0-win32\\bin\\blkls.exe "
blkstat = "\\sleuthkit-4.3.0-win32\\bin\\blkstat.exe "
blkcalc = "\\sleuthkit-4.3.0-win32\\bin\\blkcalc.exe "
jcat = "\\sleuthkit-4.3.0-win32\\bin\\jcat.exe "
jls = "\\sleuthkit-4.3.0-win32\\bin\\jls.exe "
mmls = "\\sleuthkit-4.3.0-win32\\bin\\mmls.exe "
mmcat = "\\sleuthkit-4.3.0-win32\\bin\\mmcat.exe "
mmstat = "\\sleuthkit-4.3.0-win32\\bin\\mmstat.exe "

commandList = [istat, fsstat, fls, ffind, fcat, icat, tsk_recover, tsk_loaddb, tsk_gettimes, tsk_comparedir, img_stat, img_cat, ils, ifind, blkcat, blkls, blkstat, blkcalc, jcat, jls, mmls, mmcat, mmstat]


print("Welcome to the sluethkit visualizer!")

answer = input("Do you want to run the GUI version? (Y/N)")

if answer.lower() == "y":
        print("COOL")
        os.system("python3 gui.py")

file = input("Please enter the file path of the image you want to run commands on: ")
if '/' in file:
    file = file.replace('/', '\\')

commandRunList = []

while answer != 'y':
    command = input("Please enter a command you would like to run (no .exe required): ")
    options = input("Please enter the flags to be used: ")
    for commands in commandList:
        if command in commands:
            output = " > "+command+".txt"
            commands = commands + options
            commands = commands + output
            commandRunList.append(commands)
            print(commandRunList)
    answer = input("Would you like to run these commands now? (Y/N")
    answer = answer.lower()

for run in commandRunList:
        os.system(run)
