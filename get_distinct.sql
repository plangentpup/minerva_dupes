select * from (
 (select distinct group1 as g from clean order by g)
 union distinct
 (select distinct group2 as g from clean order by g)
) a order by g;