---高级查询
--集合操作符可以将两个或多个查询返回的结果组合起来，
--常用的集合操作符包括: UNION、 UNION ALL、INTERSECT和MINUS。 --这些集合操作符具有相同的优先级，当同时使用多个操作符时，会按照从左到右的方式引用这些集合操作符。
--当使用集合操作符时，必须确保不同查询的列个数和数据类型都要匹配。

--union 获取并集（去重）
select * from user_info1 --最左边表字段为主字段
union --去重合并
select * from user_info

--union all（去合集，不去重）
select * from user_info
union all--不去重合并
select * from user_info1

--intersect（取交集）
select * from user_info
intersect--获取结果集交集
select * from user_info1

--minus（取主表的差集）
select * from user_info A--主表
minus
select * from user_info1 B

--层次化查询，一张表中两个字段存在所属关系
select level, empno,mgr,ename from emp--level指出节点在树中所处的层次
start with ename='KING'--起始查询行
connect by prior empno=mgr--定义父行和子行的关系
order by level;

select level,lpad(' ',4*level-1)||ename
from emp
start with ename='JONES'
connect by prior empno=mgr;

---rollup 对每个分组结果进行小计，然后对所有分组小计求和
select d. dname,sum(e.sal)
from emp e, dept d
where e. deptno=d.deptno
group by rollup(d.dname)
order by d.dname;


---cube子句 对每列的分组进行小计，然后每列小计进行求和
select e.job,d.dname,sum(e.sal)
from emp e,dept d
where e.deptno=d.deptno
group by rollup(e.job,d.dname)---返回所有列组合的小计信息
order by e.job,d.dname;

--grouping(column)当字段值为空时，值为1，否则为0；
select grouping(d.dname),d.dname, sum(e.sal)
from emp e,dept d
where e.deptno=d.deptno
group by rollup(d.dname)
order by d.dname;
