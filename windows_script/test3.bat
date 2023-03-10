::该文件名为test4.bat
@chcp 65001
::该文件名为test.bat
@echo off
echo 这是主程序第一个输出
timeout 2
call E:\桌面\test4.bat p1 p2
timeout 2
echo 这是主程序第二个输出
pause