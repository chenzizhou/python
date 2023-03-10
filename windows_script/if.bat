::if常规用法，注意空格
@echo off
:start
set /p a=
if not %a%==1 (
	echo input 1
	goto start
) else (
	echo input exact
)
pause>nul

