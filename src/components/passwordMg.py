from tkinter import Label, Entry, Button, messagebox, ttk, Frame, Tk
from ..utils import dataEncrypt, verify
import json


class PasswordMg:
    def __init__(
        self,
        selected=None,
        treeView: ttk.Treeview = None,
        window: Tk = None,
        oldContainer: Frame = None,
        key=None,
    ):
        self.key = key
        self.selected = selected
        self.treeView = treeView
        self.window = window
        self.container = Frame(window)
        self.oldContainer = oldContainer
        self.container.pack()
        oldContainer.forget()
        if not selected:
            self.create()
        else:
            self.update()

    def update(self):
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
        list_box.insert("", "end", values=self.treeView.item(self.selected)["values"])
        list_box.pack()
        buttonFrame = Frame(self.container)
        buttonFrame.pack()
        Button(buttonFrame, text="Back", command=self.back).grid(
            row=0, column=0, padx=10, pady=10
        )
        Button(buttonFrame, text="copy", command=self.copy).grid(
            row=0, column=1, padx=10, pady=10
        )
        Button(buttonFrame, text="delete", command=self.delete).grid(
            row=0, column=2, padx=10, pady=10
        )
    def create(self):
        self.source = Entry(self.container)
        self.user = Entry(self.container)
        self.password = Entry(self.container, show="*")
        Label(self.container, text="Source").pack()
        self.source.pack()
        Label(self.container, text="User/Email").pack()
        self.user.pack()
        Label(self.container, text="Password").pack()
        self.password.pack()
        Button(
            self.container,
            text="Submit",
            command=self.add,
        ).pack()
    @verify
    def copy(self):
        value = self.treeView.item(self.selected)["values"][-1]
        self.window.clipboard_clear()
        self.window.clipboard_append(value)

    @verify
    def delete(self):
        self.treeView.delete(self.selected)

        data = []
        columns = ["source", "user", "d", "password"]

        for row in self.treeView.get_children():
            dictionary = dict(zip(columns, self.treeView.item(row)["values"]))
            del dictionary["d"]
            data.append(dictionary)
        dataEncrypt().write(json.dumps(data).encode(), self.key)
        self.container.destroy()
        self.oldContainer.pack()

    def back(self):
        self.container.destroy()
        self.oldContainer.pack()

    @verify
    def add(self):
        if self.password.get() == "":
            messagebox.showerror("Error", "Password cannot be empty")
        else:
            decryptData = dataEncrypt().read(self.key)
            data: list = json.loads(decryptData)
            data.append(
                {
                    "source": self.source.get(),
                    "user": self.user.get(),
                    "password": self.password.get(),
                }
            )
            dataEncrypt().write(json.dumps(data).encode(), self.key)
            psw = '*' * len(str(self.password.get()))
            self.treeView.insert(
                "", "end", values=(self.source.get(), self.user.get(), psw, self.password.get())
            )
            self.container.destroy()
            self.oldContainer.pack()
