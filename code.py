# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)

#rename column
data = data.rename(str, columns={"Total": "Total_Medals"})

#display first 10 record
print(data.head(10))

#Code ends here



# --------------
#Code starts here
#create new column Better_Event based on total medals
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',
                        np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
 
print(data.head(5))                       
#better performing countires count
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
#new dataframe using 3 columns as below
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

#drop last row
top_countries.drop(top_countries.tail(1).index, inplace = True)

#function to fetch top 10 coutry names
def top_ten(top_countries, column_name):
    country_list=[]
    top_10_name = top_countries.nlargest(10, column_name)
    country_list = top_10_name["Country_Name"].tolist()
    return country_list

#call function

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
print(top_10_summer)
print(top_10_winter)
print(top_10)
#common list
common = []
#common = [set(top_10_summer) & set(top_10_winter) & set(top_10)]
for element in top_10_summer:
    if element in top_10_winter:
        if element in top_10:
            common.append(element)

print(common)



# --------------
#Code starts here
#subsetting data for summer
summer_df = data[data['Country_Name'].isin(top_10_summer)]

#subsetting data for winter
winter_df = data[data['Country_Name'].isin(top_10_winter)]

#subsetting data for top 10
top_df = data[data['Country_Name'].isin(top_10)]

#plot bar graph
ax = summer_df[['Country_Name','Total_Summer']].plot(kind='bar', title ="Summer", figsize=(5, 3),legend=True) 
ax = winter_df[['Country_Name','Total_Winter']].plot(kind='bar', title ="Winter", figsize=(5, 3),legend=True) 
ax = top_df[['Country_Name','Total_Medals']].plot(kind='bar', title ="Top", figsize=(5, 3),legend=True) 
#display
plt.show()


# --------------
#Code starts here
#add new column to summer_df
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
#find max ratio of summer gold and country
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold, summer_max_ratio)

#new column to winter_df
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
#print(winter_df)
#find max ratio of Winter gold and country
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold, winter_max_ratio)

#new column to top_df
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
#find max ratio of top gold and country
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold, top_max_ratio)



# --------------
#Code starts here
#drop last row of totals
data_1 = data.drop(data.tail(1).index)
#add new column
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points,best_country)


# --------------
#Code starts here
#single row dataframe for the best country
best = data[data['Country_Name']==best_country]
#subset best by columns as below
#best = best.groupby(['Gold_Total','Silver_Total','Bronze_Total'])
best = best.loc[:,['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
#plot a stacked plot
best.plot.bar()
plt.xlabel("Uniated States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


