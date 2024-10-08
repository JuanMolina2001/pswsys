pyinstaller --noconsole --name pswsys  main.py
xcopy src\assets dist\pswsys\src\assets /E /I
copy src\settings.json dist\pswsys\src\settings.json