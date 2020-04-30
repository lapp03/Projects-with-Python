"""
NBA Analysis 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 

players = pd.read_csv('basketball_players.csv')
master = pd.read_csv('basketball_master.csv')
nba = pd.merge(players, master, how='left', left_on='playerID', right_on='bioID')

#QUESTION 1
nba['points'].mean()
nba['points'].median()

#QUESTION 2
nba[["firstName", "middleName", "lastName","year", "points"]].sort_values("points", ascending=False).head(1)

#QUESTION 3
sns.boxplot(data=nba[["points", "assists", "rebounds"]]) 
#plt.show()


#QUESTION 4
nba_grouped_year = nba[["points", "year"]].groupby("year").median()
nba_grouped_year = nba_grouped_year.reset_index()
nba_grouped_year = nba_grouped_year[nba_grouped_year["points"] > 0]
sns.regplot(data=nba_grouped_year, x="year", y="points").set_title("Median points per Year")
#plt.show()

#QUESTION 5
players_with_maxpoints = nba[["firstName", "lastName","year", "points",
                              'fgAttempted']] .sort_values("points", ascending=False).head(10)
players_with_maxpoints = players_with_maxpoints.assign(difference = nba['points']- nba['fgAttempted'])
efficient_players = players_with_maxpoints.sort_values("difference", ascending=False).head(5)


#QUESTION 6
nba = nba.assign(ranking = nba['points'] + nba['rebounds'] + nba['steals'] + nba['blocks'])
exceptional_players = nba[['playerID',"firstName", "lastName","year", 'ranking']]
                                                .sort_values("ranking", ascending=False).head(5)
top5 = exceptional_players.groupby('ranking')

#QUESTION 7
three_by_year = nba[["threeAttempted", "year"]].groupby("year").mean()
three_by_year = three_by_year.reset_index()
three_by_year = three_by_year[three_by_year["threeAttempted"] > 0]
sns.regplot(data=three_by_year, x="year", y="threeAttempted").set_title("Mean three-points Shots per Year")
#plt.show()

#QUESTION 8 

#QUESTION 9
nba_grouped_state = nba[["points", "birthState"]].groupby("birthState").median()
topStates = nba_grouped_state.sort_values("points", ascending=False)

#QUESTION 10
# Create data
points_by_height = nba[["points", "height",'playerID']].groupby("playerID").mean()
points_by_height = points_by_height.reset_index()
points_by_height = points_by_height[points_by_height["points"] > 0]
sns.regplot(data=points_by_height, x="height", y="points").set_title("Mean points by Height")
plt.show() 
