from tkinter import *
import requests

# Colors
main_color = "#14085f"

# Main Window
root = Tk()
root.minsize(400,120)
root.resizable(False, False)
root.title("Currency conversion 2.0")
root.config(bg=main_color)

# User input
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Mainloop
root.mainloop()