/*�α���������
�α�����    ����
%FOUND      ���������ԣ������һ�ζ���¼ʱ�ɹ�����,��ֵΪ TRUE
%NOTFOUND  ���������ԣ���%FOUND �෴
%ISOPEN    ���������ԣ����α��Ѵ�ʱ���� TRUE
%ROWCOUNT  ���������ԣ������Ѵ��α��ж�ȡ�ļ�¼��*/

----�α�ʵ��Ҫ��Ҫ���ض��У�
DECLARE 
R_DD DD_USER_INFO%ROWTYPE;
CURSOR DD_CURSOR IS SELECT * INTO R_DD FROM DD_USER_INFO;--�����α꣬��ʾ�α�
BEGIN
  OPEN DD_CURSOR;---���α꣬��λ����һ������
  FETCH DD_CURSOR INTO R_DD;----��ȡ�α굱ǰ��λλ������
      WHILE DD_CURSOR%FOUND LOOP---�ж���һ���α��ȡ������û��
               DBMS_OUTPUT.PUT_LINE('��ǰ�α�ͣ������Ϊ��'||DD_CURSOR%ROWCOUNT||',ֵΪ��'||R_DD.U_ID);---��ȡ��ǰ�α궨λ����
               FETCH DD_CURSOR INTO R_DD;
    END LOOP;
    CLOSE DD_CURSOR;---�ر��α꣬�ͷ���Դ
EXCEPTION
  WHEN OTHERS THEN
       DBMS_OUTPUT.PUT_LINE('���򱨴�');
END;
