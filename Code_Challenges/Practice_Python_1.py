#####Objects and Classes



class Circle(object):
    '''
        Intro:
    	
        Every object has 
		○ A type
		○ An internal data representation (a blueprint)
		○ A set of procedures for interacting with the object (methods)
	    
        An object is an instance of a particular type.
        
        Methods: A class or type's methods are functions that every instance of that class or type provides.  Example: "List.sort()".  Methods change or interact with the object

        

    '''

    def __init__(self, radius=3, color='red'):
        '''
        Note: You need two underscores on either side of the init
        Note: You do not need to specify "self" as a parameter when invoking a method it's in.  Python will take care of that.
        Note: Default values have been specified for the parameters.
        '''
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    

#Call a circle object
newCircle = Circle(5, 'purple')
newCircle.add_radius(2)
print(newCircle.radius)

#The 'dir' function is useful for obtaining all the data attributes and methods of a class.  Example: dir(NameofObject):
print(dir(Circle))

