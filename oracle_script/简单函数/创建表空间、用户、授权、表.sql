---创建表空间，需要创建表空间权限
CREATE TABLESPACE "DD" 
LOGGING DATAFILE 'E:\app\Administrator\oradata\orcl\DD.DBF' --数据库文件
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
select * from V_$TABLESPACE;

CREATE USER "DD" IDENTIFIED BY "nature" DEFAULT TABLESPACE DD;--创建用户
GRANT CONNECT,RESOURCE TO DD;
GRANT DBA TO DD;


---创建表
CREATE TABLE user_info1(
  tel_num varchar(11) NOT NULL,
  password varchar(30) NOT NULL,
  PRIMARY KEY (tel_num)
)TABLESPACE DD

--给列添加别名
COMMENT ON COLUMN user_info.tel_num is '电话号码';


--合并
MERGE INTO user_info t 
USING user_info1 t1 
ON (t.tel_num=t1.tel_num)
WHEN MATCHED THEN 
UPDATE set t.password=t1.password WHERE tel_num=t1.tel_num
WHEN NOT MATCHED THEN
INSERT VALUES(t1.tel_num,t1.password)