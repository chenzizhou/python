--���ϱ���
declare
t_t dd_user_info.tel%type;--���е��ֶ�
begin
  select t.tel into t_t from dd_user_info t where t.tel='1';
  dbms_output.put_line(t_t);
end;

declare
  t_u dd_user_info%ROWTYPE;---���������ֶ�
begin
  select * into t_u from dd_user_info t where t.tel='1';
  dbms_output.put_line(t_u.tel||t_u.password);---����̨��ӡ
end;  
