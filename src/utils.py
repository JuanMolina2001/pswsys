from tkinter import messagebox
import json
import win32security
import win32api
from cryptography.fernet import Fernet
import base64
import hashlib


def auth(password:str):
    try:
        user = win32api.GetUserName()
        print(user)
        token = win32security.LogonUser(
            user,
            None,
            password,
            win32security.LOGON32_LOGON_INTERACTIVE,
            win32security.LOGON32_PROVIDER_DEFAULT,
        )
        print(token)
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
        messagebox.showerror("Error", str(e))


def encrypt(data, key):
    print('encrypt')
    try:
        if key:
            f = Fernet(key)
            encryptedData = f.encrypt(data)
            return encryptedData
    except Exception as e:
        messagebox.showerror("Error", str(e))

    