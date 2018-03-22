select pam.fecha,pam2.fecha
from
merval.pampa_energia pam
left join merval.invertironline_pampa_energia pam2 on pam.fecha = pam2.fecha
where pam.fecha > 20170101
;



select *
from
merval.ypf_sociedad ypf
left join merval.invertironline_ypf ypf2 on ypf.fecha = ypf2.fecha
where ypf.fecha > 20170101

;


select pam.fecha,ypf.fecha
from
merval.pampa_energia pam
left join merval.ypf_sociedad ypf on pam.fecha = ypf.fecha
UNION
select pam.fecha,ypf.fecha
from
merval.pampa_energia pam
right join merval.ypf_sociedad ypf on pam.fecha = ypf.fecha
;




select *
from
merval.ypf_sociedad
where 1=1
and fecha > 20091110
and fecha < 20091119
;



select *
from
merval.invertironline_ypf
where 1=1
and fecha > 20101110
and fecha < 20101119
;

select *
from
merval.ravaonline_pampa_energia
;

