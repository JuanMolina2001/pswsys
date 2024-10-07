from tkinter import Toplevel, Label, Entry, Button, messagebox, ttk, Frame, Tk
from ..utils import auth, dataEncrypt
import json

class PasswordMg:
    def __init__(
        self, selected, treeView: ttk.Treeview, window: Tk, oldContainer: Frame,key
    ):
        self.key = key
        self.selected = selected
        self.treeView = treeView
        self.window = window
        self.container = Frame(window)
        self.oldContainer = oldContainer
        columns = ("Source", "User/Email", "Password", "hidden")
        list_box = ttk.Treeview(
            self.container, columns=columns, show="headings", height=1
        )
        for col in columns:
            if col == "hidden":
                list_box.column(col, width=0, stretch=False)
                continue
            list_box.heading(col, text=col.title(), anchor="center")
            list_box.column(col, anchor="center", width=150)
        list_box.insert("", "end", values=treeView.item(selected)["values"])
        list_box.pack()
        Button(
            self.container, text="copy", command=lambda: self.verify(self.copy)
        ).pack()
        Button(
            self.container, text="delete", command=lambda: self.verify(self.delete)
        ).pack()
        self.container.pack()

    def copy(self):
        value = self.treeView.item(self.selected)["values"][-1]
        self.window.clipboard_clear()
        self.window.clipboard_append(value)

    def delete(self):
        self.treeView.delete(self.selected)
        self.container.forget()
        self.oldContainer.pack()
        data = []
        columns = ["source", "user", "d", "password"]

        for row in self.treeView.get_children():
            dictionary = dict(zip(columns, self.treeView.item(row)["values"]))
            del dictionary["d"]
            data.append(dictionary)
        print(json.dumps(data))
        dataEncrypt().write(json.dumps(data).encode(), self.key)
    
    def verify(self, callback):
        modal = Toplevel(self.window)
        modal.title("Password")
        Label(modal, text="Write the user password of windows").pack()
        password = Entry(modal, show="*")
        password.pack()

        def onReturn(_):
            if auth(password.get()):
                modal.destroy()
                callback()
            else:
                messagebox.showerror("Error", "Invalid password")

        password.bind("<Return>", onReturn)
