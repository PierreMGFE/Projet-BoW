import pandas
import numpy as np
import matplotlib.pyplot as plt

from preprocessing.load_files import data
from re import sub

from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans



def create_data(data1="NY.GNP.PCAP.CD", data2="NY.GDP.PCAP.KD.ZG", year="2015"):
    # read excel file
    econ_data = pandas.read_excel("NLP/economic_data.xlsx")
    
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

# TODO : ajuster k

kmeans = KMeans(init='k-means++', n_clusters=5, n_init=10)
kmeans.fit(reduced_data)

predict_label = kmeans.predict(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .001     # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() - 0.1, reduced_data[:, 0].max() + 0.1
y_min, y_max = reduced_data[:, 1].min() - 0.1, reduced_data[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
# fig = plt.figure(1)
fig = plt.Figure(figsize=(10, 10), dpi=50)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)

i = 0

for country in country_label:
    # xpos, ypos = np.random.uniform(-50,50), np.random.uniform(-50,50)
    plt.annotate(country, xy=(reduced_data[i,0], reduced_data[i,1]), xycoords='data', xytext=(+1, +3), textcoords='offset points', fontsize=8)
    i += 1
plt.title('K-means clustering\n'
          'normalized (x=gni per capita, y=GDP per capita growth) \n'
          'for a given year\n'
          'world bank data\n')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(np.linspace(x_min,x_max,10, endpoint=True))
plt.yticks(np.linspace(y_min,y_max,10, endpoint=True))
plt.show()
