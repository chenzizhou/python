---������ռ䣬��Ҫ������ռ�Ȩ��
CREATE TABLESPACE "DD" 
LOGGING DATAFILE 'D:\app\nature\oradata\orcl\DD.DBF' --���ݿ��ļ�
SIZE 32M --�����ļ���С
AUTOEXTEND ON --�Զ�����
NEXT 32M --ÿ��������С
MAXSIZE UNLIMITED --����ļ���С
EXTENT MANAGEMENT LOCAL --���䣨��ռ䣩���� ���ء��ֵ�dictionary
SEGMENT SPACE MANAGEMENT AUTO; --�οռ����  

--	"V$" �����ĳ��ʵ������ͼ
-- "GV$" ��ȫ����ͼ����Զ��ʵ��������
-- "X$"  ���� 'GV$' ��ͼ��������Դ��Oracle �ڲ���
-- "V_$" ���̶������ͼ����ͬ����� 'V$'
-- "GV_$"���̶������ͼ����ͬ����� 'GV$'
--select * from V_$TABLESPACE;

/*
CREATE USER '�û�����һ��Ϊ��ĸ�����ͺ͡�#������_������' 
IDENTIFIED BY '�û����һ��Ϊ��ĸ�����ͺ͡�#������_������'
DEFAULT TABLESPACE 'Ĭ�ϵı�ռ�'
TEMPORARY TABLESPACE '��ʱ��ռ���'
PROFILE '��Դ�ļ�'
QUOTA '�û�����ʹ�õı�ռ���ֽ���'
PASSWORD EXPIRE--������������ɹ���״̬���û��ٵ�¼ǰ�����޸Ŀ���
ACCOUNT LOCK OR ACCOUNT UNLOCK;--�û��Ƿ񱻼�����Ĭ��������ǲ������ġ�
;--�����û�
*/
CREATE USER 'dd' 
IDENTIFIED BY 'nature'
DEFAULT TABLESPACE 'dd'
;--�����û�


GRANT CONNECT,RESOURCE TO DD;
GRANT DBA TO DD;

---������
DROP TABLE USER_INFO;
CREATE TABLE user_info(
  u_id int,
  tel_num varchar(11) NOT NULL,
  password varchar(30) NOT NULL,
  sex varchar(2) DEFAULT '��',
  age int DEFAULT 18��
  height varchar(10) DEFAULT 100,
  PRIMARY KEY (tel_num)
)TABLESPACE DD

---��������
DROP SEQUENCE SE_U_ID;

CREATE SEQUENCE SE_U_ID
MINVALUE 0        ---������Сֵ
MAXVALUE 1000     ---�������ֵ
START WITH 0    ---����С����Сֵ
INCREMENT BY 1  ----С��MAX-MIN
CYCLE
CACHE 2--����ֵ�������1��С��һ��ѭ����ֵ
;

SELECT SE_U_ID.NEXTVAL FROM DUAL;
SELECT * FROM USER_INFO;
---������1
CREATE TABLE user_info1(
  tel_num varchar(11) NOT NULL,
  password varchar(30) NOT NULL,
  PRIMARY KEY (tel_num)
)TABLESPACE DD
--������ӱ���
COMMENT ON COLUMN user_info.tel_num is '�绰����';
alter table user_info add age int;--������
alter table user_info add sex varchar(2);--������
alter table user_info add height varchar(5);--������
alter table user_info modify age int default 20;--�޸ı�ṹ

COMMENT ON COLUMN user_info1.tel_num is '�绰����';
alter table user_info1 add age int;--������
alter table user_info1 add sex varchar(2);--������
alter table user_info1 add height varchar(5);--������
alter table user_info1 modify age int default 20;--�޸ı�ṹ

/*
drop table user_info;--ɾ����
drop table user_info1;
*/
insert into user_info t (t.u_id,t.tel_num,t.password)values(SE_U_ID.NEXTVAL,'2','2');
insert into user_info values('2','2',null);


insert into user_info1 t(t.tel_num,t.password) values('4','4');
insert into user_info1(tel_num,password) values('3','3');


alter table user_info add age int;

--�ϲ� ��user_info1�е����ݺϲ���user_info��
MERGE INTO user_info t 
USING user_info1 t1 
ON (t.tel_num=t1.tel_num)
WHEN MATCHED THEN 
UPDATE set t.password=t1.password WHERE tel_num=t1.tel_num
WHEN NOT MATCHED THEN
INSERT VALUES(t1.tel_num,t1.password,t1.age)


select * from dba_profiles;---�鿴��Դ���ò���

select * from user_info;

--��ɫ
create role dd_role;--������ɫ
grant connect,resource,dba to dd_role;--��Ȩ
alter role dd_role identified by nature;
alter role dd_role not identified;
grant dd_role to dd;
revoke dd_role from dd;

select * from dba_roles ;   
select * from user_role_privs;
select * from role_role_privs;
select * from role_sys_privs where role='DD_ROLE';
select * from session_roles;
select * from role_tab_privs;
drop role dd_role cascade;




