pyinstaller --noconsole --name pswsys --icon=logo.ico main.py
xcopy src\assets dist\pswsys\src\assets /E /I
copy src\settings.json dist\pswsys\src\settings.json