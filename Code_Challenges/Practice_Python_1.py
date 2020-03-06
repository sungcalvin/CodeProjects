#Loops

#Range function (Output is Python 2.0 only)

#Outputs an ordered sequence given an index input
print(range(3))
range(10,15)
print(range(10,15))


#For loops

#Start with a list "squares" showing colors.
squares = ["red", "yellow", "green", "purple", "blue"]

print("Squares is now", squares)

#For loop to set these colors to "white"
for i in range(0,5):
    squares[i] = "white"

print("Squares is now", squares)

#For loop to print list squares, without needing indices
squares = ["red", "yellow", "green", "purple", "blue"]

for square in squares:

    print(square)

print("\n")

#Syntax to iterate throug a list and provide the index of each element
squares = ["red", "yellow", "green", "purple", "blue"]

#Variable "i" is the index, "square" the corresponding element in the list
for i, square in enumerate(squares):
    
    print(i, square)

print("\n")


#While loops are similar to for loops

