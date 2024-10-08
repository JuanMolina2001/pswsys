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
        columns=None,
        lang: dict = None,
    ):
        self.lang = lang
        self.columns = columns
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
        list_box = ttk.Treeview(
            self.container, columns=self.columns, show="headings", height=1
        )
        for col in self.columns:
            if col == "hidden":
                list_box.column(col, width=0, stretch=False)
                continue
            list_box.heading(col, text=col.title(), anchor="center")
            list_box.column(col, anchor="center", width=150)
        list_box.insert("", "end", values=self.treeView.item(self.selected)["values"])
        list_box.pack()
        buttonFrame = Frame(self.container)
        buttonFrame.pack()
        Button(buttonFrame, text=self.lang.get("back", "Back"), command=self.back).grid(
            row=0, column=0, padx=10, pady=10
        )
        Button(buttonFrame, text=self.lang.get("copy", "Copy"), command=self.copy).grid(
            row=0, column=1, padx=10, pady=10
        )
        Button(
            buttonFrame, text=self.lang.get("delete", "Delete"), command=self.delete
        ).grid(row=0, column=2, padx=10, pady=10)

    def create(self):
        self.source = Entry(self.container)
        self.user = Entry(self.container)
        self.password = Entry(self.container, show="*")
        labels = []
        for col in self.columns:
            if col == "hidden":
                continue
            labels.append(Label(self.container, text=col.title()))
        labels[0].pack()
        self.source.pack()
        labels[1].pack()
        self.user.pack()
        labels[2].pack()
        self.password.pack()
        Button(
            self.container,
            text=self.lang.get("submit", "Accept"),
            command=self.add,
        ).pack()
        Button(
            self.container, text=self.lang.get("cancel", "Cancel"), command=self.back
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
            messagebox.showerror(
                "Error",
                self.lang.get("passwordCannotBeEmpty", "Password cannot be empty"),
            )
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
            psw = "*" * len(str(self.password.get()))
            self.treeView.insert(
                "",
                "end",
                values=(self.source.get(), self.user.get(), psw, self.password.get()),
            )
            self.container.destroy()
            self.oldContainer.pack()
