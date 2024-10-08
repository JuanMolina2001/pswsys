from tkinter import Tk
from src.components.login import Login
from src.components.createPsw import CreatePassword
from src.components.barMenu.main import BarMenu
import os
import json
def main():
    window = Tk()
    window.title("PSW")
    window.geometry("500x300")
    window.resizable(False, False)
    with open('src/settings.json', 'r') as f:
        settings = json.load(f)
    def reload():
        window.destroy()
        main()
    window.reload = reload
    BarMenu(window)
    if os.path.isfile('data.enc') is False:
        CreatePassword(window,settings)
    else:
        Login(window,settings)

    window.mainloop()
if __name__ == '__main__':
    main()