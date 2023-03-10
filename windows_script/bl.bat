chcp 65001
@echo off
set /p param=
if %param%==4 (echo 请不要输入4！) else (echo %param%)
::%0在当前窗口重新调用自身
%0