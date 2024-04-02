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

# Scrollbar - currency
scrollbar_from = StringVar(root)
scrollbar_from.set("CZK")   # Default value
scrollbar_from_options = OptionMenu(root, scrollbar_from, "CZK", "EUR", "USD")
scrollbar_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))

# Scrollbar - output currency
scrollbar_to = StringVar(root)
scrollbar_to.set("EUR")
scrollbar_to_options = OptionMenu(root, scrollbar_to, "EUR", "CZK", "USD")
scrollbar_to_options.grid(row=1, column=1, padx=10, pady=(10, 0))

# Convert button
convert_button = Button(text="Přepočítat", font=("Arial", 12))
convert_button.grid(row=0, column=2, padx=10, pady=(10,0))

# Mainloop
root.mainloop()