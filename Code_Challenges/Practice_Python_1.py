#####Simple APIs, Part 1
'''
#Note: This requires prior installation of python package "nba_api".
# 
# Install accordingly:
# 1) Navigate to correct Python Interpreter.  (Best practice: Virtual environment)  
# 2) In console on Windows, type "python -m pip install nba_api"
# 3) The package should install

'''
#Import required modules
import numpy
import matplotlib.pyplot as plt
import pandas as pd

#To make request for a specific team, just need an ID (not JSON file)
from nba_api.stats.static import teams

#Return a list of dictionaries which have the same keys, but whose value depends on the team
nba_teams = teams.get_teams()

#Return the first five dictionaries
nba_teams[:5]

#Function to convert dictionary to a table
def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

#Convert list nba_teams to dictionary dict_nba_team
dict_nba_team = one_dict(nba_teams)

#Convert dictionary dict_nba_team to a dataframe df_teams.  Print out dataframe and head
df_teams = pd.DataFrame(dict_nba_team)
print("Sneak peak at df_teams: ", df_teams.head())
print("Full df_teams: ", df_teams)

#Find the row that contains the warriors
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print("Warriors dataframe: ", df_warriors)

#Access the first column of the dataframe df_warriors
id_warriors = df_warriors[['id']].values[0][0]

#The function leaguegamefinder makes an API call .  The parameter "team_id_nullable" makes an HTTP request
from nba_api.stats.endpoints import leaguegamefinder

#The gamefinder object returns a datagrame 
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

#The gamefinder object has a method get_data_frames() that returns a dataframe of all the games the Warriors played.  The "PLUS_MIN" column contains info on the score.
#If the value is negative, the Warriors lost by that many points; if positive, vice versa
games = gamefinder.get_data_frames()[0]
print("Sneak peak at games: ", games.head())
#print("Full list of games: ", games)

#Define games_home and games_away as games where the matchup is Warriors vs. the Toronto Raptors, at home vs @ Raptors
games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']

#Plot the score info of Warriors for games_away and games_home
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
games_away.plot(x = 'GAME_DATE', y = 'PLUS_MINUS', ax = ax)
games_home.plot(x = 'GAME_DATE', y = 'PLUS_MINUS', ax = ax)
ax.legend(["away", "home"])
plt.show()

#Conclusion: We see the Warriors play better at home.