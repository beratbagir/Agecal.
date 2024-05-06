import tkinter

window = tkinter.Tk()
window.title("AGEcal")
window.minsize(300, 200)


def validate_input(text):
    if text.isdigit() and len(text) <= 2:
        return True
    else:
        return False


def calculate_age():
    birth_day = int(birth_day_entry.get())
    birth_month = int(birth_month_entry.get())
    birth_year = int(birth_year_entry.get())

    now_day = int(now_day_entry.get())
    now_month = int(now_month_entry.get())
    now_year = int(now_year_entry.get())

    age = now_year - birth_year

    if now_month < birth_month or (now_month == birth_month and now_day < birth_day):
        age -= 1

    result_label.config(text=f"Your age is {age}")


birth_label = tkinter.Label(text="Please enter your birth date (DD/MM/YYYY):")
birth_label.config(fg="black")
birth_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

birth_day_entry = tkinter.Entry(width=5, validate="key")
birth_day_entry.grid(row=1, column=0, padx=5, pady=5)
birth_day_entry.config(validatecommand=(birth_day_entry.register(validate_input), "%P"))

birth_month_entry = tkinter.Entry(width=5, validate="key")
birth_month_entry.grid(row=1, column=1, padx=5, pady=5)
birth_month_entry.config(validatecommand=(birth_month_entry.register(validate_input), "%P"))

birth_year_entry = tkinter.Entry(width=8, validate="key")
birth_year_entry.grid(row=1, column=2, padx=5, pady=5)
birth_year_entry.config(
    validatecommand=(birth_year_entry.register(lambda text: text.isdigit() and len(text) <= 4), "%P"))

now_label = tkinter.Label(text="Please enter the current date (DD/MM/YYYY):")
now_label.config(fg="black")
now_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

now_day_entry = tkinter.Entry(width=5, validate="key")
now_day_entry.grid(row=3, column=0, padx=5, pady=5)
now_day_entry.config(validatecommand=(now_day_entry.register(validate_input), "%P"))

now_month_entry = tkinter.Entry(width=5, validate="key")
now_month_entry.grid(row=3, column=1, padx=5, pady=5)
now_month_entry.config(validatecommand=(now_month_entry.register(validate_input), "%P"))

now_year_entry = tkinter.Entry(width=8, validate="key")
now_year_entry.grid(row=3, column=2, padx=5, pady=5)
now_year_entry.config(validatecommand=(now_year_entry.register(lambda text: text.isdigit() and len(text) <= 4), "%P"))

my_button = tkinter.Button(text="Calculate", command=calculate_age)
my_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

result_label = tkinter.Label(text="")
result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

window.mainloop()
