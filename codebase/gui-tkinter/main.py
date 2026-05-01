# ===============================================================
# GUI - Tkinter (TK Interface)
# ===============================================================
import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "italic"))
my_label.pack()

# import turtle
# tim = turtle.Turtle()
# tim.write()

# my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=15)
input.pack()
print(input.get())

window.mainloop()