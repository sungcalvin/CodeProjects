#Functions

#This function takes an input a and adds one to it.  
def function(a):
    """Add 1 to a.
        
        Type more here in this code block!

    """
    b = a + 1;

    print(a, " +1 = ", b)
    return b

print(function(1131))

print("\n")

def ArtistNames(*names):
    """
    ArtistNames prints the parameters given

    """
    for name in names:
        print(name)

ArtistNames("Michael Jackson", "AC / DC", "Pink Floyd")

ArtistNames("Michael Jackson", "AC / DC")

print("\n")