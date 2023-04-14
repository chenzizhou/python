DECLARE 
R_DD DD_USER_INFO%ROWTYPE;
MY_EXCEPTION EXCEPTION;---自定义异常
PRAGMA EXCEPTION_INIT(MY_EXCEPTION,-9999);
BEGIN
       RAISE MY_EXCEPTION;---自定义异常抛出
       SELECT * INTO R_DD FROM DD_USER_INFO; 
       EXCEPTION
              WHEN MY_EXCEPTION THEN---接受自预定义异常
                   DBMS_OUTPUT.PUT_LINE('程序报错');
              WHEN OTHERS THEN
                   DBMS_OUTPUT.PUT_LINE('error');
       
END;
----预定义异常和自定义异常使用类似 当错误号系统已提供 未提供名称 需自己定义
