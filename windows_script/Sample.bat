@echo off 
:begin
choice /c abc /m 1,2,3 
if errorlevel 3 goto c 
if errorlevel 2 goto b
if errorlevel 1 goto a

:a 
echo 1
pause
goto begin


:b
echo 2
pause
goto begin


:c
echo 3
pause
goto begin


