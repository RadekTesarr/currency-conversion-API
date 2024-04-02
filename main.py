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


# Functions
def count():
    try:
        currency_from = scrollbar_from.get()
        currency_to = scrollbar_to.get()
        amount = int(user_input.get())

        # API
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "RL9pMJ3r9by0ZVlW4JyrqBAKkZAxEvDo"
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        response.raise_for_status()
        data_result = response.json()
        result_label.config(text=round(data_result["result"], 2))
        notify_label.config(text="")
    except:
        notify_label.config(text="Zadejte částku!")


# User input
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Scrollbar - input currency
scrollbar_from = StringVar(root)
scrollbar_from.set("CZK")   # Default value
scrollbar_from_options = OptionMenu(root, scrollbar_from, "CZK", "EUR", "USD", "PLN")
scrollbar_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))

# Scrollbar - output currency
scrollbar_to = StringVar(root)
scrollbar_to.set("EUR")
scrollbar_to_options = OptionMenu(root, scrollbar_to, "EUR", "CZK", "USD", "PLN")
scrollbar_to_options.grid(row=1, column=1, padx=10, pady=(10, 0))

# Convert button
convert_button = Button(text="Přepočítat", font=("Arial", 12), command=count)
convert_button.grid(row=0, column=2, padx=10, pady=(10,0))

# Result label
result_label = Label(text="0", bg=main_color, fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0)

# Notify label
notify_label = Label(bg=main_color, fg="white", font=("Arial", 12))
notify_label.grid(row=2, column=0)

# Mainloop
root.mainloop()