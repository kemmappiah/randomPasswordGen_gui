from tkinter import *
import random
import string

window = Tk()
window.title("EMMAPP PASSWORD GENERATOR")
window.geometry("300x200")

instruction = ("""
    This is a Random Password Generator!
    Click 'Go' and I will give you a perfect password!
""")

top_label = Label(window, text=instruction)
top_label.pack()


def password_gen():
    password = []
    special_xters = ["!", "@", "#", "%", "&", "$", "?", "_", "-", "="]
    pwd_length = random.randrange(8, 12)
    pwd_xter = 0
    while pwd_xter <= pwd_length:
        num = random.randrange(0, 9)   # string.digits
        password.append(str(num))
        spx = random.choice(special_xters)   # string.punctuation
        password.append(spx)
        upp_alpha = random.choice(string.ascii_uppercase)
        password.append(upp_alpha)
        low_alpha = random.choice(string.ascii_lowercase)
        password.append(low_alpha)
        pwd_xter += 4
    
    random.shuffle(password)
    final_password = "".join(password)
    output_label.config(text=final_password)


go_button = Button(window, text="Go!", command=password_gen)
go_button.pack()
output_label = Label(window, fg="blue", font=20)
output_label.pack()

window.mainloop()
