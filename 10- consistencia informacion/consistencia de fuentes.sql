

select
fechas.fecha,
pe.ultima,
inv.ultima,
rav.ultima
from
(
select fecha
from
merval.pampa_energia
union
select fecha
from
merval.invertironline_pampa_energia
union
select fecha
from
merval.ravaonline_pampa_energia
) fechas
left join pampa_energia pe on fechas.fecha = pe.fecha
left join invertironline_pampa_energia inv on fechas.fecha = inv.fecha
left join ravaonline_pampa_energia rav on fechas.fecha = rav.fecha
order by fechas.fecha desc
