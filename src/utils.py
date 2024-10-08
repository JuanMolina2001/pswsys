from cryptography.fernet import Fernet
import platform
from playsound import playsound

def auth(password: str):
    try:
        if platform.system() == "Windows":
            import win32security
            import win32api

            user = win32api.GetUserName()
            token = win32security.LogonUser(
                user,
                None,
                password,
                win32security.LOGON32_LOGON_INTERACTIVE,
                win32security.LOGON32_PROVIDER_DEFAULT,
            )
        else:
            import pam
            import getpass

            user = getpass.getuser()
            p = pam.pam()
            if p.authenticate(user, password):
                return True
            else:
                return False
        if token:
            return True
        else:
            return False
    except Exception as e:
        return False


def decrypt(encryptedData, key):
    try:
        if key:
            f = Fernet(key)
            decryptedData = f.decrypt(encryptedData)
            return decryptedData
    except Exception as e:
        raise Exception(str(e))


def encrypt(data, key):
    try:
        if key:
            f = Fernet(key)
            encryptedData = f.encrypt(data)
            return encryptedData
    except Exception as e:
        raise Exception(str(e))


def validateKey(key):
    try:
        data = open("data.enc", "rb").read()
        decrypt(data, key)
        return True
    except Exception as e:
        return False


def getKey(password):
    try:
        import hashlib
        import base64

        hashedPassword = hashlib.sha256(password.encode()).digest()
        key = base64.urlsafe_b64encode(hashedPassword[:32])
        return key
    except Exception as e:
        raise Exception(str(e))


class dataEncrypt:
    def read(self, key):
        try:
            data = open("data.enc", "rb").read()
            return decrypt(data, key)
        except Exception as e:
            raise Exception(str(e))

    def write(self, data, key):
        try:
            if validateKey(key):
                encryptedData = encrypt(data, key)
                with open("data.enc", "wb") as f:
                    f.write(encryptedData)
            else:
                raise Exception("Invalid key")
        except Exception as e:
            raise Exception(str(e))


def verify(func):
    def wrapper(self, *args, **kwargs):
        from tkinter import Toplevel, Label, Entry, PhotoImage,Button,Frame
        modal = Toplevel(self.window)
        modal.overrideredirect(True)
        modal.attributes("-topmost", True) 
        modal.title("Password")
        modal.focus_force()
        modal.grab_set()
        height = 200
        width = 300
        screen_width = modal.winfo_screenwidth()
        screen_height = modal.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        modal.geometry(f'{width}x{height}+{x}+{y}')

        self.shield_image = PhotoImage(file="src/assets/images/shield-lock.png")
        password = Entry(modal, show="*")
        Label(modal, image=self.shield_image).pack(pady=10)
        password.focus_force()
        password.pack(pady=10)
        Label(modal, text=self.lang.get("verifyTitle","Write the User password ")).pack(pady=10)
        def onSubmit():
            if auth(password.get()):
                modal.destroy()
                func(self, *args, **kwargs)
            else:
                try:
                    playsound("src\\assets\\sounds\\error.wav")
                except Exception as e:
                    print(str(e))
        frame_btn = Frame(modal)
        frame_btn.pack(pady=10)
        Button(frame_btn, text=self.lang.get("submit","Accept"),command=onSubmit).grid(row=0, column=0,padx=10)
        Button(frame_btn, text=self.lang.get("cancel","Cancel"),command=lambda:modal.destroy()).grid(row=0, column=1,padx=10)
        password.bind("<Return>", lambda _: onSubmit())
        modal.after(100, lambda:playsound("src\\assets\\sounds\\alert.wav"))
    return wrapper