#library(dplyr)
#library(tidyr)
#http://r-statistics.co/Time-Series-Analysis-With-R.html

dataset <- '/Users/laiunce/Desktop/scraping/2 - lee datos empresas/datasets/PAM.N.csv'
data2 <- read.csv(dataset)

#ordenada de viejo a nuevo
data_ord_asc <-data2[with(data2, order(FECHA)), ]

plot(data_ord_asc$ULTIMO,type = 'line')

maxima_fecha = max(data_ord_asc$FECHA)
minima_fecha = min(data_ord_asc$FECHA)

#año
ano_maxima_fecha <- substr(toString(maxima_fecha), 0, 4)
ano_minima_fecha <- substr(toString(minima_fecha), 0, 4)
#mes
mes_maxima_fecha <- substr(toString(maxima_fecha), 5, 6)
mes_minima_fecha <- substr(toString(minima_fecha), 5, 6)
#dia
dia_maxima_fecha <- substr(toString(maxima_fecha), 7, 8)
dia_minima_fecha <- substr(toString(minima_fecha), 7, 8)


valores <- data_ord_asc$ULTIMO

tsData2 <- ts(
  data=valores, 
  start = c(1,1), 
  #end = c(2017,10), 
  frequency = 365)


decomposedRes<-decompose(tsData2, type="mult")
#decomposedRes<-decompose(tsData2, type="additive")
plot(decomposedRes)


df <-data.frame(
decomposedRes$x,
decomposedRes$seasonal,
decomposedRes$trend,
decomposedRes$random
)

df[is.na(df)] <- 0



write.csv(df, file = '/Users/laiunce/Desktop/scraping/6-analisis serie temporal/salida.csv')

