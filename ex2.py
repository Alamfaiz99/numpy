import numpy as np
'''
a=np.array(9)
print(a)
a1=np.array([10,20,30,40])
print(a1)
a2=np.array([[1,2,3,4],[5,6,7,8]])
print(a2)
print(a2.ndim)
'''
l=[[10,20,30,40],[1,2,3,4]]
a=np.asarray(l,dtype='int',order='F')
print(a)
for i in np.nditer(a):
    print(i)
#s=b'i am sm faizna alam'
#a1=np.frombuffer(s,dtype='',count=-1,offset=0)
#print(a1)
a1=np.arange(0,10,2,dtype='int')
print(a1)
a2=np.linspace(0,10,num=5,endpoint=True,dtype='int')
print(a2)
a3=np.logspace(0,10,num=2,endpoint=True,base=2,dtype='int')
print(a3)
