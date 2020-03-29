#####Writing files with open

'''
#You can write to files using an open function
with open("exampleFile.txt", "w") as File1:
    File1.write("This is line A\n")
    File1.write("This is line B\n")


#You can also use a for loop to write a list contents to a file
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open("exampleFile.txt", "w") as File1:
    for line in Lines:
        File1.write(line)
'''

#You can copy one file to another
with open("exampleFile.txt", "r") as readfile:
    with open("exampleFile_copy.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)