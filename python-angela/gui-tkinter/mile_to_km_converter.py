# ===============================================================
# Mile to Km Converter with Tkinter (TK Interface)
# ===============================================================
import tkinter

# ----- Miles to Km conversion ----- #
def miles_to_km():
    """Converts miles to km and config output in \"Kilometer_result_label\" """
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    kilometer_result_label.config(text=f"{km}")

# ----- Title ----- #
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# ------ Entry ----- #
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

# ----- Labels ------ #
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="km")
kilometer_label.grid(column=2,row=1)

# ----- Button ----- #
calculate_button = tkinter.Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()