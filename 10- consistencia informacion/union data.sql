
CREATE TEMPORARY TABLE fechas (
select*
from
(
select fecha
from
merval.cablevision
union
select fecha
from
merval.camuzzi
union
select fecha
from
merval.capex
union
select fecha
from
merval.caputo
union
select fecha
from
merval.carboclor
union
select fecha
from
merval.carlos_casado
union
select fecha
from
merval.caterpillar_inc_ar
union
select fecha
from
merval.celulosa
union
select fecha
from
merval.central_costan
union
select fecha
from
merval.central_puerto
union
select fecha
from
merval.chevron_corp_ar
union
select fecha
from
merval.china_mobile_ar
union
select fecha
from
merval.cisco_systems
union
select fecha
from
merval.citigroup_incorporated
union
select fecha
from
merval.coca_cola_co_ba
union
select fecha
from
merval.colgate_palmolive_company
union
select fecha
from
merval.colorin
union
select fecha
from
merval.comer_del_plat
union
select fecha
from
merval.compania_introductora_buenos_aires
union
select fecha
from
merval.con_del_oeste
union
select fecha
from
merval.consultatio_s
union
select fecha
from
merval.cresud
union
select fecha
from
merval.domec_compania_de_artefactos_domest
union
select fecha
from
merval.du_pont_de_nemours___company
union
select fecha
from
merval.dycasa
union
select fecha
from
merval.ecogas
union
select fecha
from
merval.edenor
union
select fecha
from
merval.empresa_distribuidora_electrica
union
select fecha
from
merval.ferrum
union
select fecha
from
merval.fiplasto
union
select fecha
from
merval.frances
union
select fecha
from
merval.garovaglio
union
select fecha
from
merval.general_electric_co
union
select fecha
from
merval.goldcorp
union
select fecha
from
merval.gp_fin_galicia
union
select fecha
from
merval.grimoldi
union
select fecha
from
merval.grupo_clarin
union
select fecha
from
merval.grupo_financiero_valores
union
select fecha
from
merval.grupo_supervielle_sa
union
select fecha
from
merval.havanna_sa
union
select fecha
from
merval.hewlett_packard
union
select fecha
from
merval.home_depot_inc
union
select fecha
from
merval.indupa
union
select fecha
from
merval.inst_rosembusc
)a
);



select
fechas.fecha,
t_1.ultima,
t_2.ultima,
t_3.ultima,
t_4.ultima,
t_5.ultima,
t_6.ultima,
t_7.ultima,
t_8.ultima,
t_9.ultima,
t_10.ultima,
t_11.ultima,
t_12.ultima,
t_13.ultima,
t_14.ultima,
t_15.ultima,
t_16.ultima,
t_17.ultima,
t_18.ultima,
t_19.ultima,
t_20.ultima,
t_21.ultima,
t_22.ultima,
t_23.ultima,
t_24.ultima,
t_25.ultima,
t_26.ultima,
t_27.ultima,
t_28.ultima,
t_29.ultima,
t_30.ultima,
t_31.ultima,
t_32.ultima,
t_33.ultima,
t_34.ultima,
t_35.ultima,
t_36.ultima,
t_37.ultima,
t_38.ultima,
t_39.ultima,
t_40.ultima,
t_41.ultima,
t_42.ultima,
t_43.ultima,
t_44.ultima
from
fechas
left join cablevision t_1 on fechas.fecha = t_1.fecha
left join camuzzi t_2 on fechas.fecha = t_2.fecha
left join capex t_3 on fechas.fecha = t_3.fecha
left join caputo t_4 on fechas.fecha = t_4.fecha
left join carboclor t_5 on fechas.fecha = t_5.fecha
left join carlos_casado t_6 on fechas.fecha = t_6.fecha
left join caterpillar_inc_ar t_7 on fechas.fecha = t_7.fecha
left join celulosa t_8 on fechas.fecha = t_8.fecha
left join central_costan t_9 on fechas.fecha = t_9.fecha
left join central_puerto t_10 on fechas.fecha = t_10.fecha
left join chevron_corp_ar t_11 on fechas.fecha = t_11.fecha
left join china_mobile_ar t_12 on fechas.fecha = t_12.fecha
left join cisco_systems t_13 on fechas.fecha = t_13.fecha
left join citigroup_incorporated t_14 on fechas.fecha = t_14.fecha
left join coca_cola_co_ba t_15 on fechas.fecha = t_15.fecha
left join colgate_palmolive_company t_16 on fechas.fecha = t_16.fecha
left join colorin t_17 on fechas.fecha = t_17.fecha
left join comer_del_plat t_18 on fechas.fecha = t_18.fecha
left join compania_introductora_buenos_aires t_19 on fechas.fecha = t_19.fecha
left join con_del_oeste t_20 on fechas.fecha = t_20.fecha
left join consultatio_s t_21 on fechas.fecha = t_21.fecha
left join cresud t_22 on fechas.fecha = t_22.fecha
left join domec_compania_de_artefactos_domest t_23 on fechas.fecha = t_23.fecha
left join du_pont_de_nemours___company t_24 on fechas.fecha = t_24.fecha
left join dycasa t_25 on fechas.fecha = t_25.fecha
left join ecogas t_26 on fechas.fecha = t_26.fecha
left join edenor t_27 on fechas.fecha = t_27.fecha
left join empresa_distribuidora_electrica t_28 on fechas.fecha = t_28.fecha
left join ferrum t_29 on fechas.fecha = t_29.fecha
left join fiplasto t_30 on fechas.fecha = t_30.fecha
left join frances t_31 on fechas.fecha = t_31.fecha
left join garovaglio t_32 on fechas.fecha = t_32.fecha
left join general_electric_co t_33 on fechas.fecha = t_33.fecha
left join goldcorp t_34 on fechas.fecha = t_34.fecha
left join gp_fin_galicia t_35 on fechas.fecha = t_35.fecha
left join grimoldi t_36 on fechas.fecha = t_36.fecha
left join grupo_clarin t_37 on fechas.fecha = t_37.fecha
left join grupo_financiero_valores t_38 on fechas.fecha = t_38.fecha
left join grupo_supervielle_sa t_39 on fechas.fecha = t_39.fecha
left join havanna_sa t_40 on fechas.fecha = t_40.fecha
left join hewlett_packard t_41 on fechas.fecha = t_41.fecha
left join home_depot_inc t_42 on fechas.fecha = t_42.fecha
left join indupa t_43 on fechas.fecha = t_43.fecha
left join inst_rosembusc t_44 on fechas.fecha = t_44.fecha
order by fechas.fecha desc




