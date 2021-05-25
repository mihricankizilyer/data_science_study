########################################
# Numpy Array Attributes
########################################

import numpy as np
np.random.seed(0) # seed for reproducibility

x1 = np.random.randint(10, size=6) #one-dimensional array
x2 = np.random.randint(10, size=(3,4)) #two-dimensional array
x3 = np.random.randint(10, size=(3,4,6)) #three-dimensional array

print(x1)
print("-----")
print(x2)
print("-----")
print(x3)

#ndim: the number of dimensions
#shape: the size of each dimension
#size: the total size of the array
#dtype: data type

print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
print("x3 dtype: ", x3.dtype)

######################
# Multidimensional subarrays
######################

# two rows, three columns
x2
x2[:2,:3]

# all rows, every other column
x2[:3,::2]

# Finally, subarray dimensions can even be reversed together
x2[::-1,::-1]

# first column of x2
print(x2[:,0])

# first row of x2
print(x2[0,:])

# equivalent to x2[0,:]
print(x2[0])

# if we modify this subarray, we'll see that the original array is changed
x2[0,0] = 99

# CREATING COPIES OF ARRAYS

# we can modify this subarray, the original array is not touched
x2_copy = x2[:2,:2].copy()
x2_copy [0,0] = 42

########################################
# Reshaping of Arrays
########################################

a = np.arange(1,10).reshape((3,3))
a = np.array([1,2,3])

#row vector via reshape
a.reshape((1,3))

# row vector via newaxis
a[np.newaxis, :]

# column vector via reshape
a.reshape((3,1))

# column vector via newaxis
a[:,np.newaxis]

########################################
# Array Concatenation and Splitting
########################################

# np.concatenate, np.vstack, np.hstack
x = np.array([1,2,3])
y = np.array([3,2,1])
np.concatenate([x,y])
np.vstack([x,y])
np.hstack([x,y])

# more than two arrays can happen
z = [55,55,55]
print(np.concatenate([x,y,z]))

# can be used for two-dimensional arrays
arr = np.array([[1,2,3],[4,5,6]])

#concatenate along the first axis
np.concatenate([arr,arr])

# cpncatenate along the second axis (zero-indexed)
np.concatenate([arr,arr], axis=1)

# for mixed dimensions -> clearer -> np.vstack or np.hstack
x = np.array([1,2,3])
arr = np.array([[9,8,7],[6,5,4]])

# vertical stack the arrays
np.vstack([x, arr])

# horizontally stack the arrays
y = np.array([[28],[15]])
np.hstack([arr,y])

######################
# Splitting of arrays
######################

# np.split, np.hsplit, np.vsplit
x = [1,3,4,5,8,11,22,45]
x1, x2, x3 =np.split(x, [3,5])

arr = np.arange(16).reshape((4,4))
upper, lower = np.vsplit(arr,[2])
print(upper)
print(lower)

left, right = np.hsplit(arr, [2])
print(left)
print(right)
