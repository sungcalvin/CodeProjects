#####Loading data with Pandas

#Dependencies or libraries are pre-written code that can be loaded to solve problems

#Import pandas
import pandas as pd
#Read csv
csv_path = 'example.csv'
df = pd.read_csv(csv_path)
#You can use the function head() to examine the first five lines
df.head()

#The process for loading an excel file is similar
#xlsx_path = 'example'
#df = pd.read_excel(csv_path)

#A dataframe can be created from a dictionary -- keys are column labels; values are row labes
songs = {
    'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', 'The Bodyguard', 'Bat from Hell', 'Thriller'], 
    'Released': [1982, 1980, 1973, 1992, 1977, 1992],
    'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33', '00:42:19']
        }
songs_frame = pd.DataFrame(songs)
print("Dataframe songs_frame is: ", songs_frame)
print("\n")

#You can print just a select column in a dataframe
x = songs_frame[['Album', 'Length']]
print("Columns 'Album' and 'Length' in dataframe songs_frame: ", x)
print("\n")

#This code prints a list of the indices of dataframe songs_frame
print(list(songs_frame.columns.values))


#This selects the unique elements from a data frame column
songs_frame_unique = songs_frame['Album'].unique()
print("Unique songs in song_frame: ", songs_frame_unique)
print("\n")

#This selects all songs released 1980 and after
songs_frame['Released'] >= 1980
songs_frame_80sandafter = songs_frame[songs_frame['Released'] >= 1980]
print("Songs 1980 and after in song_frame: ", songs_frame_80sandafter)
print("\n")

#Save a dataframe result to csv
songs_frame_80sandafter.to_csv('songs_frame_80sandafter.csv')

# Using loc, iloc, and ix
# There are three ways to select data from a data frame in Pandas: loc, iloc, and ix

#Loc looks up a row number in a dataframe column (specify label)
print(songs_frame.loc[0,'Album'])
print(songs_frame.loc[1,'Released'])
print("\n")

#iloc looks up a (row, column) pair in a dataframe
print(songs_frame.iloc[0,0])
print(songs_frame.iloc[0,1])
print(songs_frame.iloc[1,0])
print(songs_frame.iloc[1,1])
print("\n")

#ix looks for a label.  If it doesn't find a label, it will use an integer.  ix is deprecated in Pandas version 0.20.0 and later, so not covered here

#You can use loc and iloc to slice dataframes and assign the values to a new data frame

##Creating a new dataframe with loc slicing
###Take the first thru third rows, and from Artist to Released columns in original dataframe
songs_frame_loc_slice = songs_frame.loc[0:2, 'Album':'Released']
print("Song_frame sliced using .loc[], ", songs_frame_loc_slice)
print("\n")

##Creating a new dataframe with iloc slicing
###Take the first thru third rows, and from second thru third columns in original dataframe.  Note that the outer index is non-inclusive
songs_frame_iloc_slice = songs_frame.iloc[0:2, 1:3]
print("Song_frame sliced using .iloc[], ", songs_frame_iloc_slice)
print("\n")