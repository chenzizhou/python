--子查询
--大于(小于)查询结果其中一个就满足
select * from user_info t where t.tel_num>any(select t1.tel_num from user_info1 t1)
select * from user_info t where t.tel_num<any(select t1.tel_num from user_info1 t1)
--大于（小于）查询结果所有就满足
select * from user_info t where t.tel_num>all(select t1.tel_num from user_info1 t1)
select * from user_info t where t.tel_num<all(select t1.tel_num from user_info1 t1)
--（不）满足后面查询的返回结果
select * from user_info t where not exists(select * from user_info1 t1 where t.tel_num=t1.tel_num)