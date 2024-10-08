from tkinter import Entry, messagebox, Button, Frame, ttk, Label
from .pswList import PswList
from ..utils import decrypt, getKey
import json


class Login:
    def __init__(self, window: ttk, settings):
        if settings["lang"] == "system":
            import locale

            settings["lang"] = locale.getdefaultlocale()[0].split("_")[0]
        if settings["lang"] == "en":
            self.lang = {}
        else:
            try:
                with open(
                    f'src/assets/lang/{settings["lang"]}.json', "r", encoding="utf-8"
                ) as f:
                    self.lang = json.load(f)["Login"]
            except Exception as e:
                self.lang = {}
        self.window = window
        self.container = Frame(window)
        Label(self.container, text=self.lang.get("psw", "Enter your password")).pack()
        self.passwordInp = Entry(self.container, show="*")
        self.passwordInp.focus()
        self.passwordInp.pack(pady=10)
        self.passwordInp.bind("<Return>", lambda _: self.submit())
        submitButton = Button(
            self.container, text=self.lang.get("submit", "Enter"), command=self.submit
        )
        submitButton.pack(pady=10)
        self.container.pack()

    def submit(self):
        try:
            key = getKey(self.passwordInp.get())
            data = open("data.enc", "r").read()
            decryptedData = json.loads(decrypt(data, key))

            def reload(List_container):
                List_container.destroy()
                self.submit()

            PswList(
                decryptedData, self.window, key, reload, self.lang.get("pswList", {})
            )
            self.container.forget()
        except Exception as e:
            messagebox.showerror("Error", str(e))
