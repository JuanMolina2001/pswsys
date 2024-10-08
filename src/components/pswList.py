from tkinter import ttk, Frame, Tk, Button
from .passwordMg import PasswordMg


class PswList:
    def __init__(self, listPasswords: list, window: Tk, key, reload, lang:dict):
        self.lang = lang
        self.window: Tk = window
        self.container = Frame(window)
        self.listPasswords = listPasswords
        self.columns = self.lang.get(
            "columns", ["Source", "User/Email", "Password", "hidden"]
        )
        self.list_box = ttk.Treeview(
            self.container, columns=self.columns, show="headings"
        )
        for col in self.columns:
            if col == "hidden":
                self.list_box.column(col, width=0, stretch=False)
                continue
            self.list_box.heading(col, text=col.title(), anchor="center")
            self.list_box.column(col, anchor="center", width=150)
        for password in listPasswords:
            source = str(password["source"]) or ""
            user = str(password["user"]) or ""
            value = str(password["password"])
            psw = "*" * len(str(password["password"]))
            self.list_box.insert("", "end", values=(source, user, psw, value))

        scrollbar = ttk.Scrollbar(
            self.container, orient="vertical", command=self.list_box.yview
        )
        self.list_box.configure(yscroll=scrollbar.set)

        def onSelection(_):
            if self.list_box.selection():
                PasswordMg(
                    self.list_box.selection(),
                    self.list_box,
                    window,
                    self.container,
                    key,
                    self.columns,
                    self.lang["passwordMng"],
                )

        self.list_box.bind("<<TreeviewSelect>>", onSelection)
        self.container.pack()
        self.list_box.pack()
        btn_frame = Frame(self.container)
        Button(
            btn_frame,
            text=self.lang.get("reload", "Reload"),
            command=lambda: reload(self.container),
        ).grid(column=0, row=0, padx=10, pady=10)
        Button(
            btn_frame,
            text=self.lang.get("add", "Add"),
            command=lambda: PasswordMg(
                None,
                self.list_box,
                window,
                self.container,
                key,
                self.columns,
                self.lang["passwordMng"],
            ),
        ).grid(column=1, row=0, padx=10, pady=10)
        btn_frame.pack()
