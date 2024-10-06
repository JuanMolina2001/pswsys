import csv
import json
from tkinter import Tk, filedialog, Label, Entry, Button, Toplevel, messagebox, Frame
from ...utils import encrypt, decrypt
import hashlib
import base64
import os


class ImportPasswords:
    def __init__(self, window: Tk):
        if os.path.isfile("data.enc") is False:
            messagebox.showerror("Error", "Passwords not created")
            return
        self.window = window
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(
                ("CSV Files", "*.csv"),
                ("JSON Files", "*.json"),
                ("All Files", "*.*"),
            ),
            defaultextension=".csv",
        )
        if filename == "":
            return
        self.modal = Toplevel(self.window)
        self.modal.title("Import Passwords")
        self.modal.resizable(False, False)
        with open(filename, "r") as file:
            if filename.endswith(".csv"):
                self.data = list(csv.DictReader(file))
                Label(self.modal, text="Select the columns with the:").pack()
                source = Entry(Frame(self.modal))
                source.pack(side="right")
                Label(source.master, text="Source:").pack(side="left")
                source.master.pack()
                user = Entry(Frame(self.modal))
                user.pack(side="right")
                Label(user.master, text="User/Email:").pack(side="left")
                user.master.pack()
                password = Entry(Frame(self.modal))
                password.pack(side="right")
                Label(password.master, text="Password:").pack(side="left")
                password.master.pack()
            elif filename.endswith(".json"):
                self.data = json.load(file)
            Label(self.modal, text="Enter the password to encrypt the data").pack()
            self.psw = Entry(self.modal, show="*")
            self.psw.pack()

            def submit():
                try:
                    if filename.endswith(".csv"):
                        self.data = [
                            {
                                "source": row[source.get() or "source"],
                                "user": row[user.get() or "user"],
                                "password": row[password.get() or "password"],
                            }
                            for row in self.data
                        ]
                    self.encryptData()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            Button(
                self.modal,
                text="Submit",
                command=submit,
            ).pack()

    def encryptData(self):
        try:
            if self.psw.get() != "":
                key = base64.urlsafe_b64encode(
                    hashlib.sha256(self.psw.get().encode()).digest()[:32]
                )
                originalData = open("data.enc", "r").read()
                decryptedData = json.loads(decrypt(originalData, key))
                decryptedData.extend(self.data)
                self.data = decryptedData
                encryptedData = encrypt(json.dumps(self.data).encode(), key)
                with open("data.enc", "wb") as f:
                    f.write(encryptedData)
                self.modal.destroy()
            else:
                raise Exception("Password cannot be empty")
        except Exception as e:
            messagebox.showerror("Error", str(e))
