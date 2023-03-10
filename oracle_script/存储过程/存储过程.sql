--存储过程 无参
CREATE OR REPLACE PROCEDURE p_test_put is
BEGIN
	DBMS_OUTPUT.PUT_LINE('123456');
END p_test_put;

call p_test_put();
execute p_test_put;--在黑窗口运行（sqlplus）

--存储过程 带有入参
CREATE OR REPLACE PROCEDURE p_test_put_i(i in int) is
BEGIN
	DBMS_OUTPUT.PUT_LINE(i);
END p_test_put_i;

call p_test_put_i(123456)

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
END p_test_put_io;

var a int;--绑定出参
exec :a:=123456;--声明入参值
call p_test_put_io(:a);--调用时不接受常量值，只能用变量为其传值
