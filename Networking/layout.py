from tkinter import *

root = Tk() # root window
entry = Entry()
entry.pack(side = BOTTOM)
button = Button(root,text="Send")

listbox = Listbox(root)
listbox.pack(side = BOTTOM)

root.mainloop()


