SELECT NVL(NULL,1),'1����Ϊ1������2' FROM DUAL;--�����һ������Ϊ��,ֵΪ�ڶ�������
SELECT NVL2(NULL,0,1),'1����Ϊ2������3' FROM DUAL;--�����һ��������Ϊ��,ֵΪ��2��������ֵΪ��3������
SELECT DECODE(3/1,3,'��ȷ��','�����') FROM DUAL;
---DECODE(value,if1,then1,if2,then2,if3,then3,...,else)����ʾ���value����if1ʱ��DECODE�����Ľ������then1,...,
-- ����������κ�һ��ifֵ���򷵻�else
SELECT NULLIF(1,0) FROM DUAL;
