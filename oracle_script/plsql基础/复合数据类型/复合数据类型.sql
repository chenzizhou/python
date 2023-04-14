--数组
declare
type v_u_t is varray(20) of dd_user_info.tel%type null;
u_t v_u_t:=v_u_t('1','2','3');---必须声明初始值
begin
  if u_t.exists('4') then---判断集合中存在元素
    dbms_output.put_line('存在');
  end if;
  dbms_output.put_line('当前集合元素个数为：'||u_t.count());---返回集合中元素个数
  u_t.extend(5,1);--增加集合元素
  dbms_output.put_line('增加集合元素后，当前集合元素个数为：'||u_t.count());---返回集合中元素个数
  u_t.trim(2);--从集合尾部删除元素
  dbms_output.put_line('删除元素后，当前集合元素个数为：'||u_t.count());---返回集合中元素个数
  dbms_output.put_line('当前集合元素最大个数为：'||u_t.limit());---返回集合元素的最大个数
  dbms_output.put_line('当前集合第一个元素为：'||u_t.first);---返回集合第一个元素
  dbms_output.put_line('当前集合最后以一个元素为：'||u_t.last);---返回集合最后一个元素
  dbms_output.put_line('集合第二个元素前一个元素为：'||u_t.prior(2));---返回集合当前元素前一个元素
  dbms_output.put_line('集合第三个元素下一个元素为：'||u_t.next(3));---返回集合当前元素下一个元素
  dbms_output.put_line('集合第二个元素为：'||u_t(2));---返回集合第二个元素
  select t.tel into u_t(3)--替换集合第三个元素     
  from dd_user_info t
  where t.tel='3';
  dbms_output.put_line('替换后集合第三个元素为：'||u_t(3));
end;
