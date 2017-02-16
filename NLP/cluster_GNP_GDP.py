
"""
===========================================================

input:  excel_file
            of macro data
            with as many countries as in our dataset (>100)
                mainly poor and developping countries
            from 2000 to 2016
            with    GNI per capita (name code: "NY.GNP.PCAP.CD")
                    GDP per capita growth (name code: "NY.GDP.PCAP.KD.ZG")
                    

=========== ========================================================
"""

import pandas
from preprocessing.load_files import data
import numpy as np
from re import sub
from sklearn.preprocessing import normalize
import os.path
from settings import ROOT_DIR


# TODO : list of years instead of year
def create_data(year, data1="NY.GNP.PCAP.CD", data2="NY.GDP.PCAP.KD.ZG"):
    """
    :param year: string for which year we want to get the year
    :param data1: code we want to select from the Excel sheet
    :param data2: code we want to select from the Excel sheet
    :return reduced_data: n*2 array containing normalized GNP / GDP per capita with n number of
    countries listed in reports for year n ;
    :return country_label: list of size n containing names of countries listed in reduced_data ;
    """
    econ_data = pandas.read_excel(os.path.join(ROOT_DIR,"data_files/excel_data/economic_data2.xlsx"))
    
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

    def transform(s):
        s1 = s.lower()
        s2 = sub(r'\W+', '', s1)
        return s2.replace(' ', '')

    data_year = data[year]
    countries = [country for country in data_year.keys()]

    reduced_data = normalize(econ_data3, axis=0)
    country_label_lw = [transform(country) for country in country_label]
    countries_lw = [transform(country) for country in countries]
    idxs = [idx for idx, country in enumerate(country_label_lw) if country in countries_lw]

    country_label = [country_label[idx].replace(' ', '') for idx in idxs]
    reduced_data = reduced_data[idxs]

    return reduced_data, country_label

