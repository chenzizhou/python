/*游标属性类型
游标属性    作用
%FOUND      布尔型属性，当最近一次读记录时成功返回,则值为 TRUE
%NOTFOUND  布尔型属性，与%FOUND 相反
%ISOPEN    布尔型属性，当游标已打开时返回 TRUE
%ROWCOUNT  数字型属性，返回已从游标中读取的记录数*/

----游标实现要求要返回多行，
DECLARE 
R_DD DD_USER_INFO%ROWTYPE;
CURSOR DD_CURSOR IS SELECT * INTO R_DD FROM DD_USER_INFO;--定义游标，显示游标
BEGIN
  OPEN DD_CURSOR;---打开游标，定位到第一行数据
  FETCH DD_CURSOR INTO R_DD;----获取游标当前定位位置数据
      WHILE DD_CURSOR%FOUND LOOP---判断上一次游标获取到数据没有
               DBMS_OUTPUT.PUT_LINE('当前游标停留行数为：'||DD_CURSOR%ROWCOUNT||',值为：'||R_DD.U_ID);---获取当前游标定位行数
               FETCH DD_CURSOR INTO R_DD;
    END LOOP;
    CLOSE DD_CURSOR;---关闭游标，释放资源
EXCEPTION
  WHEN OTHERS THEN
       DBMS_OUTPUT.PUT_LINE('程序报错');
END;
