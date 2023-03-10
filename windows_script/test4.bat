::该文件名为test1.bat
@chcp 65001
@echo off
timeout 2
echo 这是子程序第一个输出
(echo 这是接收到的第一个参数%1) & (echo 和第二个参数%2)
pause