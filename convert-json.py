import json
import re
import os
import sys
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text = "Enter JSON File Location")
label.pack()

canvas = tk.Canvas(root, width = 400, height = 300)
canvas.pack()

entry = tk.Entry(root) 
canvas.create_window(200, 140, window=entry)
#sets up program tkinter window with text entry

def getResults ():
	filename = entry.get()
	isFile = os.path.isfile(filename)

	if not (isFile):
		print("Invalid File Path")
		return
	#ends getResults if path is bad
	else:
		f = open(filename, 'r')
		i=0
		while os.path.exists("results%s.csv" % i):
			i += 1
		res = open('results%s.csv' % i, 'w+')
		#adds number to result.csv
		emails = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
		#finds emails within json file
		for email in emails:
			res.write("%s\n" % email)
		#writes to csv, emails on individual lines
		f.close()
	res.close()

button = tk.Button(text='Enter', command=getResults)
canvas.create_window(200, 180, window=button)
#creates button that runs getResults function

root.mainloop()
