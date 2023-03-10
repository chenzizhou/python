@chcp 65001
@echo off
set a=123
set b=abc
set c=12
::/i字符串大小写忽略
if /i %b% equ ABC (
  if %a% geq %c% (
    echo %a%^>=%c%
  ) else (
    echo %a%^<%c%
  )
) else (
  echo %b%不等于ABC
)
pause>nul