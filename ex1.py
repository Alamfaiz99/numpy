import numpy as np
#arguments taken by array method is list,tuple,or any otehr iterables
'''
a0=np.array(78)
a1=np.array([10,20,30])
a2=np.array([[10,20,30],[40,50,60]])
a3=np.array([[[10,20,30],[40,50,60]],[[10,20,30],[40,50,60]]])
print(a0,a1,a2,a3,sep='\n')
print(a0.ndim,a1.ndim,a2.ndim,a3.ndim,sep='\n')
print(type(a0))
'''

'''
#how to create arrays from predefined data
l=[10,20,30,40]
print(l)
a=np.asarray(l,dtype='int',order='C')
#if you wanna iterate the values of the array
for i in np.nditer(a):
    print(i)
print(a)
t=((1,2,3,4,5),(6,7,8,9,10))
a1=np.asarray(t,dtype='int',order='F')
print(a1)
for i in np.nditer(a1):
    print(i)
'''
'''
n=int(input("Enter the dimention of array:"))
for i in range(n):
    a=np.arrazy(input("Enter ")+str(i)+("row:\n"))
print(a)
'''
'''
s=b'my name is sm'
print(type(s))
a=np.frombuffer(s,dtype='str',count=-1,offset=0)
print(a)
'''
t=(1,2,3,4)
a=np.fromiter(t,dtype='int',count=-1)
print(a)
