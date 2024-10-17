import tkinter as tk
from tkinter import messagebox, simpledialog


class PassSafe:
    def __init__(self, root):
        self.root = root
        self.root.title("PassSafe - Secure Password Manager")
        self.root.geometry("400x300")
        self.credentials = []
        self.create_widgets()

    def create_widgets(self):
        self.label_account = tk.Label(self.root, text="Account Name")
        self.label_account.pack(pady=5)

        self.entry_account = tk.Entry(self.root)
        self.entry_account.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Password")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.btn_add = tk.Button(self.root, text="Add Password", command=self.add_password)
        self.btn_add.pack(pady=10)

        self.btn_show = tk.Button(self.root, text="Show Passwords", command=self.show_passwords)
        self.btn_show.pack(pady=5)

        self.btn_generate = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.btn_generate.pack(pady=5)

        self.listbox_credentials = tk.Listbox(self.root)
        self.listbox_credentials.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_password(self):
        account = self.entry_account.get()
        password = self.entry_password.get()

        if account and password:
            self.credentials.append((account, password))
            self.entry_account.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            messagebox.showinfo("Success", "Password added successfully!")
        else:
            messagebox.showerror("Error", "Both fields are required")

    def show_passwords(self):
        self.listbox_credentials.delete(0, tk.END) 
        for i, (account, password) in enumerate(self.credentials):
            self.listbox_credentials.insert(tk.END, f"{i + 1}. {account}: {password}")

    def generate_password(self):
        import random
        import string
        length = simpledialog.askinteger("Input", "Enter password length", minvalue=8, maxvalue=32)
        if length:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            self.entry_password.delete(0, tk.END)
            self.entry_password.insert(0, password)
            messagebox.showinfo("Generated Password", f"Password generated: {password}")
        else:
            messagebox.showerror("Error", "Invalid length")


if __name__ == "__main__":
    root = tk.Tk()
    app = PassSafe(root)
    root.mainloop()
