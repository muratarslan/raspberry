from Tkinter import *

def printVal(val):
	label.config(text = val)

root = Tk()
root.title("Servo")

scale = Scale(root, orient = HORIZONTAL, length = 300, width = 20, from_ = 0, to = 255, command = printVal)
scale.pack(anchor = CENTER)


label = Label(root)
label.pack()

root.mainloop()





