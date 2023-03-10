@chcp 65001
@echo off
set a=1
if defined a (
	echo 已定义a
) else (
	echo 未定义a
)
pause>nul