---创建表空间，需要创建表空间权限
CREATE TABLESPACE "DD" 
LOGGING DATAFILE 'D:\app\nature\oradata\orcl\DD.DBF' --数据库文件
SIZE 32M --数据文件大小
AUTOEXTEND ON --自动扩增
NEXT 32M --每次扩增大小
MAXSIZE UNLIMITED --最大文件大小
EXTENT MANAGEMENT LOCAL --区间（表空间）管理 本地、字典dictionary
SEGMENT SPACE MANAGEMENT AUTO; --段空间管理  

--	"V$" ：针对某个实例的视图
-- "GV$" ：全局视图，针对多个实例环境。
-- "X$"  ：是 'GV$' 视图的数据来源，Oracle 内部表。
-- "V_$" ：固定表或视图，其同义词是 'V$'
-- "GV_$"：固定表或视图，其同义词是 'GV$'
--select * from V_$TABLESPACE;

/*
CREATE USER '用户名，一般为字母数字型和“#”及“_”符号' 
IDENTIFIED BY '用户口令，一般为字母数字型和“#”及“_”符号'
DEFAULT TABLESPACE '默认的表空间'
TEMPORARY TABLESPACE '临时表空间名'
PROFILE '资源文件'
QUOTA '用户可以使用的表空间的字节数'
PASSWORD EXPIRE--立即将口令设成过期状态，用户再登录前必须修改口令
ACCOUNT LOCK OR ACCOUNT UNLOCK;--用户是否被加锁，默认情况下是不加锁的。
;--创建用户
*/
CREATE USER 'dd' 
IDENTIFIED BY 'nature'
DEFAULT TABLESPACE 'dd'
;--创建用户


GRANT CONNECT,RESOURCE TO DD;
GRANT DBA TO DD;

---创建表
DROP TABLE USER_INFO;
CREATE TABLE user_info(
  u_id int,
  tel_num varchar(11) NOT NULL,
  password varchar(30) NOT NULL,
  sex varchar(2) DEFAULT '男',
  age int DEFAULT 18，
  height varchar(10) DEFAULT 100,
  PRIMARY KEY (tel_num)
)TABLESPACE DD

---创建序列
DROP SEQUENCE SE_U_ID;

CREATE SEQUENCE SE_U_ID
MINVALUE 0        ---序列最小值
MAXVALUE 1000     ---序列最大值
START WITH 0    ---不能小于最小值
INCREMENT BY 1  ----小于MAX-MIN
CYCLE
CACHE 2--缓存值必须大于1且小于一次循环的值
;

SELECT SE_U_ID.NEXTVAL FROM DUAL;
SELECT * FROM USER_INFO;
---创建表1
CREATE TABLE user_info1(
  tel_num varchar(11) NOT NULL,
  password varchar(30) NOT NULL,
  PRIMARY KEY (tel_num)
)TABLESPACE DD
--给列添加别名
COMMENT ON COLUMN user_info.tel_num is '电话号码';
alter table user_info add age int;--增加列
alter table user_info add sex varchar(2);--增加列
alter table user_info add height varchar(5);--增加列
alter table user_info modify age int default 20;--修改表结构

COMMENT ON COLUMN user_info1.tel_num is '电话号码';
alter table user_info1 add age int;--增加列
alter table user_info1 add sex varchar(2);--增加列
alter table user_info1 add height varchar(5);--增加列
alter table user_info1 modify age int default 20;--修改表结构

/*
drop table user_info;--删除表
drop table user_info1;
*/
insert into user_info t (t.u_id,t.tel_num,t.password)values(SE_U_ID.NEXTVAL,'2','2');
insert into user_info values('2','2',null);


insert into user_info1 t(t.tel_num,t.password) values('4','4');
insert into user_info1(tel_num,password) values('3','3');


alter table user_info add age int;

--合并 将user_info1中的数据合并到user_info中
MERGE INTO user_info t 
USING user_info1 t1 
ON (t.tel_num=t1.tel_num)
WHEN MATCHED THEN 
UPDATE set t.password=t1.password WHERE tel_num=t1.tel_num
WHEN NOT MATCHED THEN
INSERT VALUES(t1.tel_num,t1.password,t1.age)


select * from dba_profiles;---查看资源配置参数

select * from user_info;

--角色
create role dd_role;--创建角色
grant connect,resource,dba to dd_role;--授权
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




