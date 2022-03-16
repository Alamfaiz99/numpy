import numpy as np
'''numpy-->stands for numerical python
provides lot of functions and builtins
to work in a domain of linear algebra ,fourier transform,matrices
-->provides functions related to arrays
-->creates an array called ndarrays
-->ndarray-->n dimentional array
-->working of nd arrays is faster than list
-->most of the parts of numpy-->designed by (c/c++)
-->array-->ndarray
-->create ndarray-->array()

'''
#0 dimentional array
a=np.array(54)
print(a)
#1 dimentional array
#array of 0 d array
a1=np.array([1,2,3])
print(a1)
#2 dimentional array
#array of 1 d array
a2=np.array([[1,2,3],[4,5,6]])
print(a2)
#3 d array is an array of 2 d array
a3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[5,6,7]]])
print(a3)

'''in order to check diemntion
we have ndim-->n dimentions
type(a.ndim)
'''
print(a.ndim)
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
#to check which type of object it is
print(type(a))
