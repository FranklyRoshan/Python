# ===============================================================
# Tkinter Layout Managers
# pack(), place(), grid()
# ===============================================================

"""
Tkinter Geometry Managers Reference
In Tkinter, geometry managers handle the size and placement of widgets. Never mix different managers (e.g., pack and grid) within the same parent container, as this will cause the application to freeze.
------------------------------
1. The pack() Manager
Concept: Blocks/Stacking.
Organizes widgets in horizontal or vertical blocks. It is the easiest to use for simple, linear layouts.

* Best For: Simple top-to-bottom or left-to-right stacks (toolbars, sidebars).
* Key Attributes:
* side: Orientation (TOP, BOTTOM, LEFT, RIGHT).
   * fill: Expansion direction (X, Y, BOTH, NONE).
   * expand: Boolean; determines if the widget claims extra space in the parent.
   * anchor: Alignment within allocated space (e.g., NW, CENTER).

2. The grid() Manager
Concept: Table/Matrix.
Organizes widgets in a 2D grid of rows and columns. This is the industry standard for complex desktop UIs.

* Best For: Forms, dashboards, and structured interfaces.
* Key Attributes:
* row / column: Integer index (starts at 0).
   * rowspan / columnspan: Number of cells a widget occupies.
   * sticky: Alignment/Stretch behavior within a cell (N, S, E, W).
   * padx / pady: External padding around the cell.

3. The place() Manager
Concept: Absolute/Relative Positioning.
Allows precise control using specific coordinates. It bypasses the automatic layout logic used by the other two.

* Best For: Overlapping widgets, custom drawing tools, or fixed-pixel designs.
* Key Attributes:
* x / y: Absolute pixel coordinates.
   * relx / rely: Position relative to parent size (0.0 to 1.0).
   * width / height: Absolute size in pixels.
   * relwidth / relheight: Size relative to parent (0.0 to 1.0).

------------------------------
Comparison Matrix

* Layout Logic
* pack(): Stack-based (Relative)
   * grid(): Coordinate-based (Table)
   * place(): Coordinate-based (Absolute)
* Responsiveness
* pack(): High (Easy to scale)
   * grid(): Very High (Most flexible)
   * place(): Low (Requires manual updates)
* Complexity
* pack(): Low
   * grid(): Medium
   * place(): High (to maintain UI consistency)

Rule of Thumb: Use grid() for most general purposes due to its power and flexibility. Use pack() for simple, linear
layouts. Avoid place() unless you need explicit pixel control and are prepared to manage all resizing manually.
"""

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# --- 01.Labels ---
label = Label(text="This is old text")
label.config(text="This is new text")
# label.pack() # pack() Manager
# label.place(x=0, y=0) # place() Manager
label.grid(row=0, column=0) # grid() Manager
label.config(padx=20,pady=20)

# --- 02.Buttons ---
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1, column=1)

# --- 03.Entries ---
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(row=3, column=2)

# --- 04.Exercise ---
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(row=0, column=2)

window.mainloop()


