# Importing the modules
import random
import string
import tkinter as tk


# Creating the main window
window = tk.Tk()
window.configure(background="white")
window.title("Password Generator")
window.geometry("300x200")
window.resizable(False, False)

# Creating the widgets
label1 = tk.Label(window, text="Enter the length of the password:", background="white")
label1.place(x=10, y=10)

entry1 = tk.Entry(window, background="white")
entry1.place(x=10, y=40)

label2 = tk.Label(window, text="Your password is:", background="white")
label2.place(x=10, y=80)

entry2 = tk.Entry(window, state="readonly", background="white")
entry2.place(x=10, y=110)

button1 = tk.Button(window, text="Generate", background="green")
button1.place(x=10, y=150)


# Defining the function to generate the password
def generate_password():
    # Getting the length from the user input
    length = int(entry1.get())
    # Creating a list of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generating a random password of the specified length
    password = "".join(random.choice(chars) for _ in range(length))
    # Displaying the password on the screen
    entry2.config(state="normal")
    entry2.delete(0, tk.END)
    entry2.insert(0, password)
    entry2.config(state="readonly")


# Binding the function to the button
button1.config(command=generate_password)

# Running the main loop
window.mainloop()
