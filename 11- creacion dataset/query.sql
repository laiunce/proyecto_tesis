select
fechas.fecha,
pe.ultima pam_ultima,
pe.apertura pam_apertura,
pe.maximo pam_maximo,
pe.minimo pam_minimo,
ypf.ultima ypf_ultima,
ypf.apertura ypf_apertura,
ypf.maximo ypf_maximo,
ypf.minimo ypf_minimo
from
(
select fecha
from
merval.invertironline_pampa_energia
union
select fecha
from
merval.invertironline_ypf
) fechas
left join invertironline_pampa_energia pe on fechas.fecha = pe.fecha
left join invertironline_ypf ypf on fechas.fecha = ypf.fecha
where 1=1
#and pe.ultima is null
#and fechas.fecha = 20161230
order by fechas.fecha desc
;