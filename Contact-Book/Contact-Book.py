import tkinter as tk
from tkinter import simpledialog, messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.contacts = []

        # Labels and Entry Widgets
        self.name_label = tk.Label(master, text="Name:", background="white")
        self.name_entry = tk.Entry(master, width=20)

        self.phone_label = tk.Label(master, text="Phone:", background="white")
        self.phone_entry = tk.Entry(master, width=20)

        self.email_label = tk.Label(master, text="Email:", background="white")
        self.email_entry = tk.Entry(master, width=20)

        self.address_label = tk.Label(master, text="Address:", background="white")
        self.address_entry = tk.Entry(master, width=20)

        # Search bar and Button
        self.search_label = tk.Label(master, text="Search:")
        self.search_entry = tk.Entry(master, width=20)
        self.search_button = tk.Button(master, text="Search", command=self.search_contact, background="white")

        # Buttons
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact, background="green")
        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts, background="white")
        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact, background="white")
        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, background="red")

        # Listbox
        self.contact_listbox = tk.Listbox(master, width=40)

        # Grid Layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.search_entry.grid(row=4, column=1, padx=10, pady=5)
        self.search_button.grid(row=4, column=0, padx=10, pady=5)

        self.add_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.view_button.grid(row=7, column=0, columnspan=2, pady=5)
        self.update_button.grid(row=8, column=0, columnspan=2, pady=5)
        self.delete_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.contact_listbox.grid(row=0, column=3, rowspan=9, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, f"{name} - {phone}")
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        query = self.search_entry.get().lower()
        self.contact_listbox.delete(0, tk.END)

        for contact in self.contacts:
            if query in contact.name.lower() or query in contact.phone.lower():
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]

            updated_name = simpledialog.askstring("Update Contact", "Enter New Name:", initialvalue=selected_contact.name)
            if updated_name:
                updated_phone = simpledialog.askstring("Update Contact", "Enter New Phone:", initialvalue=selected_contact.phone)
                updated_email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=selected_contact.email)
                updated_address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=selected_contact.address)

                selected_contact.name = updated_name
                selected_contact.phone = updated_phone
                selected_contact.email = updated_email
                selected_contact.address = updated_address

                self.view_contacts()
                messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")

def main():
    root = tk.Tk()
    root.configure(background="white")
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
