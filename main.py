from tkinter import *
import tkinter.messagebox as tmbox
import random
# -------------------------------------- PASSWORD GENERATOR ---------------------------------#
def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# --------------------------------------- SAVE PASSWORD -------------------------------------#

def save():
    web_data = website_entry.get()
    email_data = email_entry.get()
    pass_data = password_entry.get()

    if len(web_data) == 0 or len(pass_data) == 0:
        tmbox.showwarning(title="Warning", message="Website or Password cannot be empty !!!")
    else:
        # Asking for confirmation
        is_ok = tmbox.askokcancel(title=web_data, message=f"These are the details\n Email : {email_data} \n Password : {pass_data} \n Press 'ok' to save.")
        if is_ok:
            # Writing to a file
            with open("data.txt", "a+") as file:
                file.write(f"{web_data} | {email_data} | {pass_data} ||\n ")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

                # Showing Confirmation
                tmbox.showinfo(title="Data Saved", message="Your Id and Password has been saved Successfully")


# ------------------------------------------ UI SETUP ---------------------------------------#
win = Tk()
win.title("Password Manager")
win.geometry("550x400+300+200")
# win.config(bg="black")
win.resizable(False, False)

# Image Setup
logo_img = PhotoImage(file="./images/icons8-password-manager-100.png")
image = Label(image= logo_img)
image.place(x = 240, y=50)

# Label setup
website_label = Label(text="Website:", font=("poppins", 10))
website_label.place(x = 20, y= 200)

email_label = Label(text="Username/E-mail:", font=("poppins", 10))
email_label.place(x = 20, y= 230)

password_label = Label(text="Password:", font=("poppins", 10))
password_label.place(x = 20, y= 260)

# Entries
website_info = StringVar()
website_entry = Entry(width=40, font=("poppins", 10))
website_entry.place(x = 160, y= 200)
website_entry.focus()

email_info = StringVar()
email_entry = Entry(width=40, font=("poppins", 10))
email_entry.place(x = 160, y= 230)

password_info = StringVar()
password_entry = Entry(width=27, font=("poppins", 10))
password_entry.place(x = 160, y= 260)

# Buttons
gen_pass_btn = Button(text="Generate Password", command=pw_generator)
gen_pass_btn.place(x = 359, y= 260)

add_btn = Button(text="Add", width=39, font=("poppins", 10), command=save)
add_btn.place(x = 160, y= 290)

win.mainloop()
