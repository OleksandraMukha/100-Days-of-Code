from tkinter import *


#How to make button work?

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
#Adding space around the program 
window.config(padx=20, pady=20)


#Lable

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#for it to appear on the screen, you have to give it a layout
my_label.grid(column=0, row=0)


#Changing label text (two methods below)
my_label["text"] = "New Text"
my_label.config(text="New text")

#Button

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

#Creating new button

new_button = Button(text="New Button")
button.grid(column=2, row=0)

#Entry

input = Entry(width=10)
input.grid(column=3, row=2)
input.get()

# PACK (you can add side="left"), PLACE (provide x=0, y=0) and GRID



window.mainloop()

