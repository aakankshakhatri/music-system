import tkinter as tk
import show

root=tk().Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(root,text="press it",command=lambda: execfile("/home/aakankshakhatri/Facial-Expression-Detection-master(2)/show.py"))
button.pack()

root.mainloop()
