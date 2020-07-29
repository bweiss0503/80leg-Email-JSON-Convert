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

def getResults ():
	filename = entry.get()

	isFile = os.path.isfile(filename)
	if not (isFile):
		print("Invalid File Path")
	else:
		f = open(filename, 'r')
		i=0
		while os.path.exists("results%s.csv" % i):
			i += 1
		res = open('results%s.csv' % i, 'w+')
		emails = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
		for email in emails:
			res.write("%s\n" % email)
		f.close()
	res.close()

button = tk.Button(text='Enter', command=getResults)
canvas.create_window(200, 180, window=button)

root.mainloop()
