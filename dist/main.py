from tkinter import *
from random import *
from tkinter import messagebox


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(2, 4)]
    password_numbers = [choice(numbers) for _ in range(2, 4)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)



def save():
    is_ok = messagebox.askokcancel(title=website_entry.get(), message=f'These are entered Email: {email_entry.get()}\nPassword: {password_entry.get()}\n')
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you entered real website and password")
    else:
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}"
                data_file.write(data)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title('password manager')
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
canvas.grid(row=0, column=1)

web_label = Label(text='Website:')
web_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password = Label(text='Password:')
password.grid(row=3, column=0)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)

website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'email@email.com')
password_entry.grid(row=3, column=1)

gen_pass_button = Button(text='Generate Password', command=generate_password)
gen_pass_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
