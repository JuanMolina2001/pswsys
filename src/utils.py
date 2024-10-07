from cryptography.fernet import Fernet
import platform
import hashlib
import base64


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
