@echo off 
choice /c dme /m defrag,mem,end 
if errorlevel 3 goto defrag 
if errorlevel 2 goto mem 
if errorlevel 1 goto end 

:defrag 
echo e
pause
goto end 
:mem 
mem 
goto end 

:end 
echo d 
pause