--表类型
--直接赋值
declare
type table_u is table of dd_user_info%rowtype
index by BINARY_INTEGER;
t_u table_u;
begin
  --不能直接对表变量赋值：select * into new_emp from scott.emp where deptno=30; 这种赋值方法是错的，赋值需要使用下标
  select * into t_u(1) 
  from dd_user_info t 
  where t.did=1;
  t_u(1).tel:=2;--直接赋值
  dbms_output.put_line(t_u.first||','||t_u.count||','||t_u.last);
  dbms_output.put_line(t_u(1).tel||t_u(1).password);
end;

--和游标配合使用、及变量的方法
declare
type table_u is table of dd_user_info%rowtype
index by BINARY_INTEGER;
t_u table_u;
CURSOR dd_cursor IS SELECT * FROM dd_user_info;
D_NUM INT;
begin
  D_NUM:=0;
  FOR DD_ROW IN dd_cursor LOOP----使用for循环游标时，默认打开游标、取值、和关闭游标
    D_NUM:=D_NUM+1;
    T_U(D_NUM):=DD_ROW;
    dbms_output.put_line(t_u(D_NUM).tel);
    END LOOP;
   t_u.delete(1);---删除表类型第一条数据
   dbms_output.put_line(t_u.next(1));--取下1行的数据
  dbms_output.put_line(t_u.first||','||t_u.count||','||t_u.last);---查看变量第一条数据、变量所有行、最后一条数据
end;
