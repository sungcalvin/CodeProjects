#####Reading Files with Open


'''
When opening a file, use the open function.  

Arguments:
1) Filepath: Filename (note can use "" for a filename in the same directory)
2) Mode: r for read, w for write, a for append
3) Store in a file object

Always close the file with the close() statement.

More efficient to use a with statement to open a file.  The advantage is it automatically closes the file.

'''

#Follow the below format for open()
#Better practice to use a with statement to open a file because it automatically closes the file.
#The code will perform all directions in the indent block, then close the file at the end of the indent
with open("exampleFile.txt", "r") as File1:
    
    file_stuff = File1.read()

    print(file_stuff)

#You can check if a file is closed, but you cannot read from it from outside the indent.
print(File1.closed)

#However, you can print the file contents from outside the indent.
print(file_stuff)


#The readline() method can be called sequentially to read the next sequence.  Python will know to start a new line
#The same can be done with elements in a list.
with open("exampleFile.txt", "r") as File1:
    file_stuff = File1.readline()
    print(file_stuff)
    file_stuff = File1.readline()
    print(file_stuff)

#We can use a loop to print out each line.
with open("exampleFile.txt", "r") as File1:
    for line in File1:
        print(line)

#You can specify the number of characters you'd like to read from a string as an argument to readlines()
with open("exampleFile.txt", "r") as File1:
    file_stuff = File1.readlines(4)
    print(file_stuff)
    file_stuff = File1.readlines(5)
    print(file_stuff)
    file_stuff = File1.readlines(9)
    print(file_stuff)

    