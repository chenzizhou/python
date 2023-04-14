select t.*
  from (select e.*, rownum rn
          from (select * from @table_name order by u_id) e
         where rownum <= (pageIndex * pageSize)) t
 where t.rn >= £¨pageIndex - 1£© * pageSize + 1;
