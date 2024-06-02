#EDA ON FIFA DATASET
#IMPORTING THE REQUIRED LIBRARIES FROM PYTHON
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#LOADING THE FIFA DATASET FILE NAME AS PLAYERS_20 AND PRINT FIRST 5 ROWS AND COULMNS
fifa = pd.read_csv(r"C:\Users\ASUS\Documents\datasets for visulaization\players_20.csv")
#print(fifa.head())
#print(fifa.shape)

#getting the names of all columns in the data
# for col in fifa.columns:
#     print(col)

#mining the different different data values
nat1 = fifa['nationality'].value_counts()
# print(nat1)
#first 10 nationality
nat2 = fifa['nationality'].value_counts()[0:10]
# print(nat2)
#print omly names of 5 first 
nat3 = fifa['nationality'].value_counts()[0:5].keys()
# print(nat3)

#making bar plot for nationality
plt.figure(figsize = (5,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color='g')
#print(plt.show())

player_salary = fifa[['short_name','wage_eur']]
#print(player_salary.head())
#now knowing the top 5 player who get more salary by desending order
player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)
#print(player_salary.head())

#Bar graph for short name and wage eur for top 5 players
plt.figure(figsize = (8,5))
plt.bar(list(player_salary['short_name'][0:5]),list(player_salary['wage_eur'][0:5]),color=['green','blue','red','pink','black'])
#print(plt.show())

#getting the information from countries name
#below code defines the nationality of germany
name = fifa['nationality'] == 'Germany'
#print(name)
#Germany
Germany = fifa[fifa['nationality']=='Germany'] #if it true then print the value
#print(Germany.head(10))

#now from Germany we want to extract players height,weight,wage,short name data 
# print(Germany.sort_values(by=['height_cm'],ascending=False).head())
# print(Germany.sort_values(by=['weight_kg'],ascending=False).head())
# print(Germany.sort_values(by=['wage_eur'],ascending=False).head())
# print(Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head())

#now checking from fifa whos shooting is best
player_shooting =fifa[['short_name','shooting']]
#print(player_shooting.sort_values(by=['shooting'],ascending=False).head())
#now same for defending
player_defending = fifa[['short_name','defending','nationality','club']]
#print(player_defending.head())
#print(player_defending.sort_values(by=['defending'],ascending=False).head())

#final analysis for the club name real madrid
real_madrid = fifa[fifa['club']=='Real Madrid']
#print(real_madrid.head())
print(real_madrid.sort_values(by=['wage_eur'],ascending=False).head())
print(real_madrid.sort_values(by=['shooting'],ascending=False).head())
print(real_madrid.sort_values(by=['defending'],ascending=False).head())
print(real_madrid['nationality'].value_counts())