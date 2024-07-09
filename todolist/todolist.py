from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("900x1600")
root.configure(background = "black")

def print_added():
  lable = Label(root, text = "To Do list Updated", fg = "white", bg = "black")
  lable.pack()

add_new = Button(root, text = "+ add new", command = print_added, fg = "white", bg = "black")

add_new.pack()
root.mainloop()