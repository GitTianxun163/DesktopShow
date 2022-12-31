@echo off
echo Compiltering..
pyinstaller --distpath D:\ZhengHaozhe\programs -n DesktopShow --version-file versioninfo -i assets/logo.ico --add-data src;assets -w src/main.py
copy assets D:\ZhengHaozhe\programs\DesktopShow
echo Compiltered