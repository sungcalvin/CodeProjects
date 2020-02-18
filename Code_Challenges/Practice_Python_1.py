Name = "Michael Jackson"

#Every second character can be returned
print(Name[::2])
print(len(Name))

#"find" function returns the index of the first occurrence of a substring within a searched string
print(Name.find('el'))

print("\n")

#List and Tuples

#Tuples are an ordered sequence.  They are expressed as comma-separated elements within parenthesis
#All types of data can be contained within a tuple.  Ex: string, integer, float
Tuple1 = ("disco", 10, 1.2)
print("Tuple1 is", Tuple1)

#Tuples are indexed starting from "0", like strings
print(Tuple1[1])

#Tuples are their own type
print(type(Tuple1))

#Tuples can be concatenated or added
Tuple2 = Tuple1 + ("hard rock", 10)
print("Tuple2 is", Tuple2)

#Tuples can be sliced
print("The first three elements of Tuple2 are:", Tuple2[0:3])
print("Every second element of Tuple2, after slicing:", Tuple2[::2])

#Use the len command to obtain the length of the tuple
print("The lenth of Tuple2 is: ", len(Tuple2))

#Tuples are immutable, which means you can't change them.  This means that if you'd like to change a tuple, you must create a new one instead

#Tuples can contain other tuples, as well as other complex data types.  This is called nesting.  The elements can be accessed using standard indexing methods, through the nesting.
NT = (1, 2, ("pop", "rock"), (3, 4), ("disco", 1, 2))
print("The third element of NT is: ", NT[2])
print("The second element of that is: ", NT[2][1])

print("\n")

#Lists:  Also ordered sequences, like tuples
#Lists are represented with square brackets
#Lists are mutable

List = ["Michael Jackson", 10.1, 1982]
print("List L is: ", List)

#Lists can contain strings, integers, floats, tuples, other lists, and other data structures

#Lists can be sliced. The index conventions for lists and tuples are identical
print("The first two elements of L are: ", List[0:2])

#Lists are mutable

#To extend, can use "+", or ".extend" function
#print("L can be extended by list [1, 2, 3] with a + operator: ", L + [1, 2, 3])
L_extension = [0, 1, 2]
print("L can be extended by list [0, 1, 2] with an .extend operator: ", List.extend(L_extension))

#To append, the entire list can be appended, but will be the next element (unlike extend, which iterates thru the list)
L_append = [3, 4, 5]
print("L can be appended by list [3, 4, 5] with an .append operator: ", List.append(L_append))

print("The total length of List is now", len(List))
print("List L: ", List)

print("\n")




