# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot
import seaborn as sns
import quandl

quandl.ApiConfig.api_key = 'rUdPDrNZ9c1hVyYH1E4Q' # Here goes your key - get it on Quandl´s website after you open an free account.
                                                  # www.quandl.com

p0  = '19140101'
p1  = '20171231'

data1  = quandl.get("RATEINF/INFLATION_USA")[p0:p1] # Quandl code

# Making the dataframe
mat_Inflation   = pd.DataFrame( index = data1.index)

m = ["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

year      = []
month     = []
Inflation = []

for n in range(0,len(data1)) :
    ano = int(str(data1.index[n])[0:4])
    mes = int(str(data1.index[n])[5:7])
    year.append(ano)
    month.append(m[mes])
    Inflation.append(data1["Value"][n])

mat_Inflation["Year"]    = year
mat_Inflation["Month"]   = month
mat_Inflation["Value"]   = Inflation

# "Pivoting" the dataframe for the heatmap
Inf = mat_Inflation.pivot("Month", "Year", "Value")

# Indexing the heatmap y-axis (jan.bottom and dec. top)
m.reverse()
Inf = Inf.reindex(m[:12])

pyplot.rcParams['savefig.facecolor'] = "wheat"

#Heatmap
fig, g = pyplot.subplots(figsize=(12.8,9))
pyplot.subplots_adjust(top = 0.96, hspace = 0.32, left = 0.05, right = 1.0, wspace = 0.21, bottom = 0.08)

sns.heatmap(Inf, annot=False, ax=g, linewidths=0.2, cmap = "YlOrRd" )

pyplot.title("USA - Inflation % (YoY) Monthly")
pyplot.xlabel("")
pyplot.ylabel("")

#Boxplot
fig, g = pyplot.subplots(figsize=(8.76,6.9))
pyplot.subplots_adjust(top = 0.95, hspace = 0.32, left = 0.10, right = 0.93, wspace = 0.21, bottom = 0.05)

sns.boxplot(data = mat_Inflation, y ="Value", x = "Month", palette = "YlOrRd", fliersize = 2.0, linewidth = 1.0)

pyplot.title("USA - Inflation (YoY) Monthly Variation Distribution")
pyplot.xlabel("")
pyplot.ylabel("% (Year over Year)")


pyplot.show()
