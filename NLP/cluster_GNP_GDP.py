from re import sub

import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize

from preprocessing.load_files import data

# TODO : list of years instead of year
def create_data(data1="NY.GNP.PCAP.CD", data2="NY.GDP.PCAP.KD.ZG", year="2015"):
    # read excel file
    econ_data = pandas.read_excel("data_files/excel_data/economic_data.xlsx")
    
    # select gni per capita and not missing data
    econ_data_gni_pc = econ_data[(econ_data["Series Code"] == data1) & (econ_data[year + " [YR" + year + "]"] != "..")]
    
    # reduce the size with 3 columns
    econ_data_gni_pc_yr = econ_data_gni_pc.loc[:, ["Country Name", "Country Code", year+" [YR"+year+"]"]]
    # change the name of columns 2015 to gni per capita 2015 in order to merge later
    econ_data_gni_pc_yr.rename(columns={year+" [YR"+year+"]": "gni per capita "+year}, inplace=True)
    
    # select GDP per capita growth and not missing data
    econ_data_gdp_pc_growth = econ_data[(econ_data["Series Code"] == data2) & (econ_data[year+" [YR"+year+"]"]!="..")]
    econ_data_gdp_pc_growth_yr = econ_data_gdp_pc_growth.loc[:, ["Country Name", "Country Code", year+" [YR"+year+"]"]]
    # change the name of columns 2015 to GDP per capita growth 2015 so as to merge later
    econ_data_gdp_pc_growth_yr.rename(columns={year+" [YR"+year+"]": "GDP per capita growth "+year}, inplace=True)
    
    # merge with country name as key (make sure gni and GDP correspond to the same country each time)
    econ_data2 = pandas.merge(econ_data_gni_pc_yr, econ_data_gdp_pc_growth_yr, on="Country Name")
    
    # extract gni per capita and GDP per capita growth as float
    econ_data3 = np.asarray(econ_data2[econ_data2.columns[[2,4]]].values, dtype=np.float64)
    # extract the names of the country corresponding one-to-one to the precedeing array so as to label in a plot
    country_label = (econ_data2[econ_data2.columns[0]].values)
    return econ_data3, country_label


def g(s):
    s1 = s.lower()
    s2 = sub(r'\W+', '', s1)
    return s2.replace(' ', '')

year = "2008"
data_year = data[year]
countries = [country for country in data_year.keys()]

econ_data3, country_label = create_data(year=year)
reduced_data = normalize(econ_data3, axis=0)
country_label_lw = [g(country) for country in country_label]
countries_lw = [g(country) for country in countries]
idxs = [idx for idx, country in enumerate(country_label_lw) if country in countries_lw]



reduced_data = reduced_data[idxs]
country_label = [country_label[idx] for idx in idxs]


print(__doc__)

kmeans = KMeans(init='k-means++', n_clusters=5, n_init=10)
kmeans.fit(reduced_data)

predict_label = kmeans.predict(reduced_data)

