from tkinter import Menu,Tk
from .importPsw import ImportPasswords
import os
import json

class BarMenu:
    def __init__(self, window: Tk):
        self.window = window
        self.menu_bar = Menu(window)
        # Archivo
        archivo_menu = Menu(self.menu_bar, tearoff=0)
        archivo_menu.add_command(label="Import passwords", command=lambda: ImportPasswords(self.window))
        archivo_menu.add_command(label="Exit", command=window.quit)
        self.menu_bar.add_cascade(label="File", menu=archivo_menu)
        #settings
        settings_menu = Menu(self.menu_bar, tearoff=0)
        # languages
        lang_dir = 'src/assets/lang'
        lang_files = os.listdir(lang_dir)
        lang_menu = Menu(settings_menu, tearoff=0)
        lang_menu.add_command(label="English", command=lambda: self.set_lang('en'))
        for lang in lang_files:
            with open(os.path.join(lang_dir, lang), 'r', encoding='utf-8') as f:
                name = json.load(f)['name']
            lang_menu.add_command(label=name, command=lambda lang=lang: self.set_lang(lang.replace('.json', '')))
        settings_menu.add_cascade(label="Language", menu=lang_menu)
        settings_menu.add_command(label="Theme", command=lambda: print("Theme"))
        settings_menu.add_command(label="Toggle sound", command=lambda: print("Toggle sound"))
        self.menu_bar.add_cascade(label="Settings", menu=settings_menu)
        # Asignar la barra de menú a la ventana
        window.config(menu=self.menu_bar)
    def set_lang(self, lang):
        with open('src/settings.json', 'r') as f:
            settings = json.load(f)
        settings['lang'] = lang
        with open('src/settings.json', 'w') as f:
            json.dump(settings, f)
        self.window.reload()
    def set_theme(self, theme):
        with open('src/settings.json', 'r') as f:
            settings = json.load(f)
        settings['theme'] = theme
        with open('src/settings.json', 'w') as f:
            json.dump(settings, f)
        self.window.reload()