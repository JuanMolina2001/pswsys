pyinstaller --noconsole --name pswsys --icon=logo.ico main.py
mkdir -p dist/pswsys/src/assets
cp -r src/assets dist/pswsys/src/assets
cp src/settings.json dist/pswsys/src/settings.json
cp logo.ico dist/pswsys/logo.ico
