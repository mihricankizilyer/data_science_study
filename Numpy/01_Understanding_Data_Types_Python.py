#################################################
# NUMPY
#################################################
# List can have every type of data
# Array can have just same data
import numpy as np

#integer array
np.array([1,3,5,7,9])

#all number return to float
np.array([1.1,3,5.1,7,9])

#converting all values to the same type
np.array([1,3,5,7,9], dtype = 'float32')

#nested lists result in multidimensional arrays
np.array([range(i,i+3) for i in [1,3,5]])

######################
# Creating Arrays from Scratch
######################

#Create a length-5 integer array filled with zeros
np.zeros(5, dtype = int)

# Create a 4x6 floating-point array filled with 1s
np.ones((4,6), dtype=int)

# Create a 3x4 array filled with 3.14
np.full((3,4), 3.14)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange(0,20,2)

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0,1,5)

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3,3))

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
np.random.normal(0,1,(3,3))

# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0,10,(3,3))

# Create a 3x3 identity matrix
np.eye(3)

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that
# memory location
np.empty(3)