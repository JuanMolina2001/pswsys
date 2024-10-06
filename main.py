from tkinter import Tk
from src.components.login import Login
from src.components.createPsw import CreatePassword
from src.components.barMenu.main import BarMenu
import os

window = Tk()
window.title("PSW")
window.geometry("500x300")
window.resizable(False, False)
BarMenu(window)


if os.path.isfile('data.enc') is False:
    CreatePassword(window)
else:
    Login(window)

window.mainloop()