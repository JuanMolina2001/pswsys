from tkinter import ttk,Frame,Tk,Label,Entry,Button,Toplevel,messagebox
from ..utils import auth
from .passwordMg import PasswordMg
class PswList:
    def __init__(self, listPasswords: list, window):
        self.window:Tk = window
        self.container = Frame(window)
        columns = ("Source","User/Email", "Password", "hidden")
        self.list_box = ttk.Treeview(self.container, columns=columns, show='headings')
        for col in columns:
            if col == "hidden":
                self.list_box.column(col, width=0, stretch=False) 
                continue
            self.list_box.heading(col, text=col.title(), anchor="center")
            self.list_box.column(col, anchor="center", width=150)
        for password in listPasswords:
            source = password['source'] or ""
            user = password['user'] or ""
            value = password['password']
            psw = '*' * len(password['password'])
            self.list_box.insert('', 'end', values=(source,user, psw,value)) 

        scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.list_box.yview)
        self.list_box.configure(yscroll=scrollbar.set)
        self.list_box.bind("<<TreeviewSelect>>", lambda event :PasswordMg(self.window,self.list_box.item(self.list_box.selection()[0])))
        self.container.pack()
        self.list_box.pack()

    