import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "contacts.txt"

def load_contacts():
    contacts_list.delete(0, tk.END)
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                contacts_list.insert(tk.END, line.strip())

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    
    if not name or not phone:
        messagebox.showerror("Error", "Both name and phone number are required.")
        return
    
    with open(FILE_NAME, "a") as file:
        file.write(f"{name}, {phone}\n")
    
    contacts_list.insert(tk.END, f"{name}, {phone}")
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Contact added successfully!")

def search_contact():
    search_term = search_entry.get().strip().lower()
    contacts_list.delete(0, tk.END)
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if search_term in line.lower():
                    contacts_list.insert(tk.END, line.strip())
    
    if contacts_list.size() == 0:
        messagebox.showinfo("Not Found", "No matching contacts found.")

def reset_list():
    search_entry.delete(0, tk.END)
    load_contacts()

# GUI Setup
root = tk.Tk()
root.title("Address Book")
root.geometry("400x400")

# Labels & Entry Fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack()

tk.Label(root, text="Search:").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search_contact).pack()
tk.Button(root, text="Reset", command=reset_list).pack()

# Contacts Listbox
contacts_list = tk.Listbox(root, width=50, height=10)
contacts_list.pack()

load_contacts()

root.mainloop()
