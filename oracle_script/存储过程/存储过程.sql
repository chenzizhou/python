--�洢���� �޲�(����ע�ͣ�
CREATE OR REPLACE PROCEDURE p_test_put is
BEGIN
	DBMS_OUTPUT.PUT_LINE('123456');
END p_test_put;

call p_test_put();
/*execute p_test_put;--�ںڴ������У�sqlplus��*/  --����ע��

--�洢���� �������
CREATE OR REPLACE PROCEDURE p_test_put_i(i in int default 123) is
BEGIN
	DBMS_OUTPUT.PUT_LINE(i);
END p_test_put_i;

call p_test_put_i();--ִ��ʹ��Ĭ�ϲ���ֵ
call p_test_put_i(123456);--ϵͳ�Զ�ƥ�����ֵ
call p_test_put_i(i=>123456);--��Ӧ������ֵ


--�洢���� ���г��� ���г��εĴ洢���̣����������������
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
  p_test_put_o(i);---����ʱ���α�����һ������������һ������
end;

--�洢���� ������κͳ���
CREATE OR REPLACE PROCEDURE p_test_put_i_o(i in int default 12345 ,a out int) is
BEGIN
	a:=123;
	DBMS_OUTPUT.PUT_LINE(i);
END p_test_put_i_o;
var a int;--������մ洢���̷��ص�ֵ
call p_test_put_i_o(123456,:a);

--�洢���� ��������������ǳ���
CREATE OR REPLACE PROCEDURE p_test_put_io(i in out int) is
BEGIN
	i:=i+0;
	DBMS_OUTPUT.PUT_LINE(i);
  p_test_put_i(2);--�洢����ֱ�ӵ��ô洢����
END p_test_put_io;

declare
  a int:=123456;--�󶨳���
begin
  p_test_put_io(a);--����ʱ�����ܳ���ֵ��ֻ���ñ���Ϊ�䴫ֵ(�������ô洢���̣�ֱ���ù�����)
end;
