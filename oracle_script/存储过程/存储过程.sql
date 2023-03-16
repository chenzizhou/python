--存储过程 无参(单行注释）
CREATE OR REPLACE PROCEDURE p_test_put is
BEGIN
	DBMS_OUTPUT.PUT_LINE('123456');
END p_test_put;

call p_test_put();
/*execute p_test_put;--在黑窗口运行（sqlplus）*/  --多行注释

--存储过程 带有入参
CREATE OR REPLACE PROCEDURE p_test_put_i(i in int default 123) is
BEGIN
	DBMS_OUTPUT.PUT_LINE(i);
END p_test_put_i;

call p_test_put_i();--执行使用默认参数值
call p_test_put_i(123456);--系统自动匹配参数值
call p_test_put_i(i=>123456);--对应参数赋值


--存储过程 带有出参 带有出参的存储过程，必须声明定义出参
CREATE OR REPLACE PROCEDURE p_test_put_o(i out int) is
BEGIN
  i:=123;
	DBMS_OUTPUT.PUT_LINE(i);
END p_test_put_o;

variable i int;
call p_test_put_o(:i);

declare
  i int;
begin
  p_test_put_o(i);---调用时出参必须是一个变量名不是一个常量
end;

--存储过程 带有入参和出参
CREATE OR REPLACE PROCEDURE p_test_put_i_o(i in int default 12345 ,a out int) is
BEGIN
	a:=123;
	DBMS_OUTPUT.PUT_LINE(i);
END p_test_put_i_o;
var a int;--定义接收存储过程返回的值
call p_test_put_i_o(123456,:a);

--存储过程 参数即是入参又是出参
CREATE OR REPLACE PROCEDURE p_test_put_io(i in out int) is
BEGIN
	i:=i+0;
	DBMS_OUTPUT.PUT_LINE(i);
  p_test_put_i(2);--存储过程直接调用存储过程
END p_test_put_io;

declare
  a int:=123456;--绑定出参
begin
  p_test_put_io(a);--调用时不接受常量值，只能用变量为其传值(程序块调用存储过程，直接用过程名)
end;
