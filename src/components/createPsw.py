from tkinter import Entry, filedialog, messagebox, Button, Frame, ttk,Label
from ..utils import encrypt,getKey
import json
from .login import Login
class CreatePassword:
    def __init__(self, window: ttk,settings):
        if settings['lang'] == 'system':
            import locale
            settings['lang'] = locale.getdefaultlocale()[0].split('_')[0]
        if settings['lang'] == 'en':
            self.lang = {}
        else:
            with open(f'src/assets/lang/{settings["lang"]}.json', 'r',encoding='utf-8') as f:
                self.lang = json.load(f)['createPsw']
        self.window = window
        self.container = Frame(window)
        Label(self.container, text=self.lang.get('title', "Create a password")).pack()
        password = Entry(self.container, show="*")
        rPassword = Entry(self.container, show="*")
        password.pack()
        rPassword.pack()
        submitButton = Button(
            self.container, text=self.lang.get('save', "Save"), command=lambda: self.submit(password, rPassword)
        )
        submitButton.pack()
        self.container.pack()
    def savePassword(self,key):
        filename = filedialog.asksaveasfilename(
            title= self.lang.get('saveAs', "Select a folder to save the password"),
            filetypes=(("Key File", "*.key"), ("All Files", "*.*")),
            defaultextension=".key",
        )
        if filename:
            with open(filename, "wb") as f:
                f.write(key)
        with open('data.enc', 'wb') as f:
            data = json.dumps(json.loads('[]')).encode()
            f.write(encrypt(data, key))
        self.container.destroy()
        Login(self.window)
    def submit(self, psw1, psw2):
        try:
            if psw1.get() != psw2.get() :
                messagebox.showerror("Error", self.lang.get('passwordsDoNotMatch', "Passwords do not match"))
            elif psw1.get() == "":
                messagebox.showerror("Error", self.lang.get('passwordCannotBeEmpty', "Password cannot be empty"))
            else:
                password = psw1.get()
                key = getKey(password)
                self.savePassword(key)
                messagebox.showinfo("Success", self.lang.get('passwordSavedSuccessfully', "Password saved successfully"))
        except Exception as e:
            messagebox.showerror("Error", str(e))
