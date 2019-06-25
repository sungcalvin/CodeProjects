import numpy as np


#This code takes a list and returns only the even numbers.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evennumbers = [element for element in a if element % 2 == 0]

print(evennumbers)


numbers = [1, 2, 3, 4, 5]
mean = np.mean(numbers)
print(mean)
median = np.median(numbers)
print(median)
stdev = np.std(numbers)
print(stdev)
