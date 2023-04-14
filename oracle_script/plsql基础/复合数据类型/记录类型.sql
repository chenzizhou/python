--记录类型 单行多字段
declare
type record_u is record(tel dd_user_info.tel%type,password dd_user_info.password%type);
t_u record_u;
begin
  select * into t_u from dd_user_info t where t.tel='1';
  dbms_output.put_line(t_u.tel||t_u.password);
end;
