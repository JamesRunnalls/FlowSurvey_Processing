#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      James.Runnalls
#
# Created:     10/03/2016
# Copyright:   (c) James.Runnalls 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import relevant modules
import arcpy, csv, math, time, sys
import Tkinter as t
import tkFileDialog as tf
import tkMessageBox as tm
import os

# Sets up user interface
window = t.Tk()
window.title('CCTV Automation')

# Function for opening the csv file
def opencsv():
    csvinput = tf.askopenfilename()
    csvv.set(csvinput)
    window.update_idletasks()

# The main function
def main():
    FDV = csv2.get()
    window.destroy()
    print FDV

    input_file = open(FDV, "r")
    lines = input_file.readlines()
    input_file.close()
    del lines[:14]
    del lines[-1]
    y = []
    for x in lines:
        y = y + x.split()
    i=0
    new_list = []
    while i<len(y):
      new_list.append(y[i:i+3])
      i+=3
    new_list.insert(0,['Flow l/s','Depth mm','Velocity m/s'])

    FDV = FDV.replace(".FDV", "")
    outputCSV = '{0}.csv'.format(FDV)
    b = open(outputCSV, 'wb')
    a = csv.writer(b)
    a.writerows(new_list)
    b.close()

# This section builds the user interface
# This is the first row for inputting the csv file location
csvv = t.StringVar()
csv1 = t.Message(text ="Location of FDV Input",width=200)
csv2 = t.Entry(window, textvariable=csvv,width=80)
csv3 = t.Button(text ="Browse", command = opencsv)
csv2.textvariable = csvv
# This creates the run button
run = t.Button(text ="Run", command = main)
# This controls the layout of the user interface
csv1.grid(row=0, column=0, padx=5, pady=5)
csv2.grid(row=0, column=1, padx=5, pady=5)
csv3.grid(row=0, column=2, padx=5, pady=5)
run.grid(row=4, column=1, padx=5, pady=20)
# This opens the user interface
window.mainloop()

