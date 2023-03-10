@chcp 65001
::'与'一般用if嵌套实现
@echo off
set /p a="请输入数字："
::当a小于10且大于0
if %a% lss 10 if %a% gtr 0 echo 输入的是0-10
pause