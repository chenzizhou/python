@echo off
if not exist d:\test.bat (
	echo @echo off>d:\test.bat
) else (
	del d:\test.bat
)
pause>nul