#####One-dimensional numpy

#Numpy is a library for scientific computing.  Numpy is also the basis for Pandas

##Basics and Array creation

#A numpy array (ND array) is fixed in size and of uniform type
import numpy as np

#Cast a list to a numpy array
numpy_array = np.array([0, 1, 2, 3, 4])

#Print the type of the numpy array
print("The type of numpy_array is: ",type(numpy_array))

#Print the type of the numpy array's elements
print("The type of numpy_array's elements is: ",numpy_array.dtype)

#Print the number of elements in the array
print("The number of elements in numpy_array is: ",numpy_array.size)

#Print the rank of the array (number of its dimensions)
print("The number of dimensions in numpy_array is: ",numpy_array.ndim)

#Print the size of the array in each dimention (output will be tuple)
print("The size of each dimension in numpy_array is: ",numpy_array.shape)

print("\n")

##Indexing and slicing

c = np.array([0, 1, 2, 3, 4])
c[0] = 100
print("Numpy array c is now: ", c)

#Select elements 1 to 3
d = c[1:4]
print("Numpy array d is: ", d)

#Assign new values to c
c[3:5] = [100, 300]
print("Numpy array c is now: ", c)

print("\n")

##Basic operations

#This code adds two vectors, u and v and place in vector z using numpy
u = np.array([1,2])
v = np.array([3,1])
z = u + v
print("Vector z after addition: ", z)

#It would require multiple line of code to perform addition on two lists, as alternative to numpy:
u = [1,2]
v = [3,1]
z = []

for n, m in zip(u, v):
    z.append(n+m)

print("\n")

#This code multiplies a vector by a scalar of 2 using numpy
y = np.array([1,2])
z = 2 * y
print("Vector z after multiplication: ", z)

print("\n")

#This code takes a Hadamard product of two vectors, u and v, in a new vector z (i.e., first element of u * first element of v = first element of z)
u = np.array([1,2])
v = np.array([3,1])
z = u * v
print("Vector z after Hadamard product: ", z)

#This code takes the dot product of two vectors, u and v, into a number (i.e., first element of u * first element of v = first element of z, then all summed)
u = np.array([1,2])
v = np.array([3,1])
z = np.dot(u,v)
print("Vector z after dot product: ", z)

#This code adds a constant to a numpy array
u = np.array([1,2,3,-1])
z = u + 1
print("Vector z after adding 1 to u ", z)

print("\n")

#Universal functions


#A universal fundtion operations on ND arrays

#Take the mean of an array
a = np.array([1, -1, 1, -1])
mean_a = a.mean()
print("Mean of a is: ", mean_a)

#Take the max of an array
b = np.array([1, -2, 3, 4, 5])
max_b = b.max()
print("Mean of a is: ", max_b)

#Map the sin of a vector of radians to a new array
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print("Numpy array x of radians is: ", x)
print("Numpy array x of their sine is: ", y)

#Map the sin of a vector of radians to a new array
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print("Numpy array x of radians is: ", x)
print("Numpy array x of their sine is: ", y)

#The linspace function plots mathematical functions, returning even intervals over a range
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

#Plot the function
import matplotlib.pyplot as plt
plt.plot(x, y)
