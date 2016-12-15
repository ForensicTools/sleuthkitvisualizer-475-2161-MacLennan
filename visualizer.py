#!/usr/bin/python
import os

# ************
# Author: Ryan MacLennan
# Filename: visualizer.py
# This file is the command line version of the gui.
# It will also ask if you want to run the gui version as well.
# ************


#windows command path
istat = os.path.normpath("sleuthkit-4.3.0-win32/bin/istat.exe ")
fsstat = os.path.normpath("sleuthkit-4.3.0-win32/bin/fsstat.exe ")
fls = os.path.normpath("sleuthkit-4.3.0-win32/bin/fls.exe ")
ffind = os.path.normpath("sleuthkit-4.3.0-win32/bin/ffind.exe ")
fcat = os.path.normpath("sleuthkit-4.3.0-win32/bin/fcat.exe ")
icat = os.path.normpath("sleuthkit-4.3.0-win32/bin/icat.exe ")
tsk_recover = os.path.normpath("sleuthkit-4.3.0-win32/bin/tsk_recover.exe ")
tsk_loaddb = os.path.normpath("sleuthkit-4.3.0-win32/bin/tsk_loaddb.exe ")
tsk_gettimes = os.path.normpath("sleuthkit-4.3.0-win32/bin/tsk_gettimes.exe ")
tsk_comparedir = os.path.normpath("/sleuthkit-4.3.0-win32/bin/tsk_comparedir.exe ")
img_stat = os.path.normpath("sleuthkit-4.3.0-win32/bin/img_stat.exe ")
img_cat = os.path.normpath("sleuthkit-4.3.0-win32/bin/img_cat.exe ")
ils = os.path.normpath("sleuthkit-4.3.0-win32/bin/ils.exe ")
ifind = os.path.normpath("sleuthkit-4.3.0-win32/bin/ifind.exe ")
blkcat = os.path.normpath("sleuthkit-4.3.0-win32/bin/blkcat.exe ")
blkls = os.path.normpath("sleuthkit-4.3.0-win32/bin/blkls.exe ")
blkstat = os.path.normpath("sleuthkit-4.3.0-win32/bin/blkstat.exe ")
blkcalc = os.path.normpath("sleuthkit-4.3.0-win32/bin/blkcalc.exe ")
jcat = os.path.normpath("sleuthkit-4.3.0-win32/bin/jcat.exe ")
jls = os.path.normpath("sleuthkit-4.3.0-win32/bin/jls.exe ")
mmls = os.path.normpath("sleuthkit-4.3.0-win32/bin/mmls.exe ")
mmcat = os.path.normpath("sleuthkit-4.3.0-win32/bin/mmcat.exe ")
mmstat = os.path.normpath("sleuthkit-4.3.0-win32/bin/mmstat.exe ")

commandList = [istat, fsstat, fls, ffind, fcat, icat, tsk_recover, tsk_loaddb, tsk_gettimes, tsk_comparedir, img_stat, img_cat, ils, ifind, blkcat, blkls, blkstat, blkcalc, jcat, jls, mmls, mmcat, mmstat]
cwd = os.getcwd()

#os.system(r"C:\\Users\\rxmhelp\\PycharmProjects\\untitled\\sleuthkit-4.3.0-win32\\bin\\fsstat.exe -f ntfs C:\\Users\\rxmhelp\\PycharmProjects\\untitled\\DiskPartitionRawImage.dd > fsstat.txt")

print("Welcome to the sluethkit visualizer!")

answer = input("Do you want to run the GUI version? (Y/N)")

if answer.lower() == "y":
        print("COOL")
        os.system("python3 gui.py")

file = os.path.normpath(input("Please enter the file path of the image you want to run commands on: "))

#if '/' in file:
#    file = file.replace('/', '\\')

commandRunList = []

while answer != 'y':
    print(commandRunList)
    command = input("Please enter a command you would like to run (no .exe required): ")
    options = input("Please enter the flags to be used: ")
    for commands in commandList:
        if command in commands:
            output = os.path.normpath(" > "+ cwd + "\\"+ command + ".txt")
            commands = commands + options
            commands = commands + " "  + file
            commands = commands + output
            commandRunList.append(commands)
            print(commandRunList)
    answer = input("Would you like to run these commands now? (Y/N)")
    answer = answer.lower()

for run in commandRunList:
    print(run)
    os.system(run)
