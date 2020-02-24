
#Dictionaries

#A dictionary is a data structure like a list.  

#It is denoted with curly bracelets.

#The index is called a "Key" and does not have to be an integer. Dictionary keys must be immutable and unique.  
#The values can be immutable, mutable, and duplicates

DictA = {"Thriller": 1982, "Back in Black": 1980, "The Dark Side of the Moon": 1973}

#Dictionary values can be accessed accordingly:
print("Dictionary of movies and their creation dates DictA :", DictA)
print("Thriller was created in : ", DictA["Thriller"])
print("\n")

#Add a dictionary entry as follows:
print("Add a new dictionary entry as follows: \n")
DictA['The Dark Knight'] = 2012
#print("\n")
print("DictA after addition:", DictA)

#Delete a dictionary entry as follows:
print("Delete a new dictionary entry as follows: \n")
del(DictA['The Dark Knight'])
print("DictA after deletion:", DictA)

#Sets



print("\n")
