#####Functions

##Some basic functions

#The function "len" returns the length of a list
print("The length of this list is: ", len(['A', 'B', 1]))
print("\n")

#This function "sum" returns the sum of all the elements in a list
album_ratings = [10.0, 8.5, 9.5, 7.0]
album_ratings_sum = sum(album_ratings)
print("The sum of list album_ratings is, ", album_ratings_sum)
print("\n")

#This function "sorted" returns a new sorted list or tuple without affecting the original
album_ratings = [10.0, 8.5, 9.5, 7.0]
sorted_album_rating = sorted(album_ratings)
print("Sorted album rating is ", sorted_album_rating)
print("Album rating is unchanged ", album_ratings)
print("\n")

#This list method "sort" returns the 
album_ratings = [10.0, 8.5, 9.5, 7.0]
album_ratings.sort()
print("List album-ratings sorted using list method .sort() is ", album_ratings)
print("\n")

##Some user-defined functions

#Sometimes a function will not return anything.  Example:
def MJ():
    print("Michael Jackson is here!")

#Function call
MJ()
print("\n")

#This function takes an input a as an argument and adds one to it.  
def add1(a):
    """Add 1 to a.
        
        Type more here in this code block!

    """
    b = a + 1;
    print(a, " + 1 = ", b)
    return b

add1(1131)
print("\n")

#This function prints out in sequence the index and contents of an enumerable parameter
def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print("Album ", i, "Rating is ", s)
    
album_ratings = [10.0, 9.5, 8.5]
printStuff(album_ratings)
print("\n")

#This function takes a sequence of names as an argument and prints them out one at a time.  
def ArtistNames(*names):
    """
    ArtistNames prints the parameters given

    Note: This also makes use of a loop

    """
    for name in names:
        print(name)

ArtistNames("Michael Jackson", "AC / DC", "Pink Floyd")

ArtistNames("Michael Jackson", "AC / DC")

ArtistNames(1,2,3,4)
print("\n")


