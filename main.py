from tkinter import *
from tkinter import messagebox
import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list =(

        [random.choice(letters) for _ in range(nr_letters)]+
        [random.choice(symbols) for _ in range(nr_symbols)]+
        [random.choice(numbers) for _ in range(nr_numbers)]

    )

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invalid", message="Please enter valid input")
        return

    is_ok = messagebox.askokcancel(title="confirmation",
                                   message=f"Details entered:\nEmail:{email}, \nPassword:{password},\n Is it ok to save")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}| {email}| {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#window

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)



#canvas

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo, anchor="center")
canvas.grid(column=1, row=0)

#label

website_label = Label(text="Website:",font=( "bold", 12))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:",font=("bold", 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("bold", 12))
password_label.grid(column=0, row=3)



#entry

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)




#button
generate_button =Button(text="Generate Password",font=("bold", 8), width=14, command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=32,command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()