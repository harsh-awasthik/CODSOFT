from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("900x1600")
root.configure(background = "black")

text = Entry(root, fg = "black", bg = "white")
text.pack()
text.insert(0, "Enter Your Task")


def print_added():
  lable = Label(root, text = text.get, fg = "white", bg = "black")
  lable.pack()

add_new = Button(root, text = "+ add new", command = print_added, fg = "white", bg = "black")

add_new.pack()
root.mainloop()