import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = int(length_entry.get())
    
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 5 characters.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        
        result_label.config(text="Generated Password:\n" + password, font=("Arial", 20))
        result_label.configure(width=30, height=6)
        
        

root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()


result_label = tk.Label(root, text="", font=("Times New Roman", 35), width=45, height=8)
result_label.pack()


root.mainloop()