--����
declare
type v_u_t is varray(20) of dd_user_info.tel%type null;
u_t v_u_t:=v_u_t('1','2','3');---����������ʼֵ
begin
  if u_t.exists('4') then---�жϼ����д���Ԫ��
    dbms_output.put_line('����');
  end if;
  dbms_output.put_line('��ǰ����Ԫ�ظ���Ϊ��'||u_t.count());---���ؼ�����Ԫ�ظ���
  u_t.extend(5,1);--���Ӽ���Ԫ��
  dbms_output.put_line('���Ӽ���Ԫ�غ󣬵�ǰ����Ԫ�ظ���Ϊ��'||u_t.count());---���ؼ�����Ԫ�ظ���
  u_t.trim(2);--�Ӽ���β��ɾ��Ԫ��
  dbms_output.put_line('ɾ��Ԫ�غ󣬵�ǰ����Ԫ�ظ���Ϊ��'||u_t.count());---���ؼ�����Ԫ�ظ���
  dbms_output.put_line('��ǰ����Ԫ��������Ϊ��'||u_t.limit());---���ؼ���Ԫ�ص�������
  dbms_output.put_line('��ǰ���ϵ�һ��Ԫ��Ϊ��'||u_t.first);---���ؼ��ϵ�һ��Ԫ��
  dbms_output.put_line('��ǰ���������һ��Ԫ��Ϊ��'||u_t.last);---���ؼ������һ��Ԫ��
  dbms_output.put_line('���ϵڶ���Ԫ��ǰһ��Ԫ��Ϊ��'||u_t.prior(2));---���ؼ��ϵ�ǰԪ��ǰһ��Ԫ��
  dbms_output.put_line('���ϵ�����Ԫ����һ��Ԫ��Ϊ��'||u_t.next(3));---���ؼ��ϵ�ǰԪ����һ��Ԫ��
  dbms_output.put_line('���ϵڶ���Ԫ��Ϊ��'||u_t(2));---���ؼ��ϵڶ���Ԫ��
  select t.tel into u_t(3)--�滻���ϵ�����Ԫ��     
  from dd_user_info t
  where t.tel='3';
  dbms_output.put_line('�滻�󼯺ϵ�����Ԫ��Ϊ��'||u_t(3));
end;
