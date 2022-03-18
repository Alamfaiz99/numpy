import numpy as np
'''
these are functions to create arrays with numerical ranges
arange()
linspace()
logspace()

-->in all three functions we have to pass numerical ranges
return arrays with values in given range and required datatype
pass->start index,stop index,dtype=''

np.arange(start index,stopindex,step size,dtype='')
np.arange(0,10,2,dtype='int')
return array[0 2 4 6 8]

np.linspace(start index,stop index,num,endpoint,return,dtype)
s index=--->lower bound
st index=-->upper bound
num=number of required values in array
num is 2 means array has only 2 elements
default=50

endpoint=-->whetehr to include stop index or not
True=stop index will be included
False-->not included

return step=-->returns dif bw the values
optionsl
default=True-->visible
False-->value not visible

np.linspace(0,10,5,endpoint=False,return='true,')


np.logspace(start index,stop index,num,endpoints,base,dtype)

base-->base of log value
dtype=''int/float


'''

a=np.arange(0,10,2,dtype='int')
print(a)
ar1=np.linspace(0,10,5,endpoint=True)
print(ar1)
