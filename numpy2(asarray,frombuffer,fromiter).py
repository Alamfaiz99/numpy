import numpy as np
#array with existing data---means having predefined data
'''
asarray(input,dtype,oreder)
input-->list,tuple,any combination
dtype-->int,flt,str
order-->row major order-->'C'
order-->col major order-->'F'
l=[10,20,30]-->seperated by comma
a=[10 20 30]-->seperation with space
rmo-->firstr fill with rows
cmo-->first fill the col

nditer()


frombuffer(buffer,dtype,count,offset)
offset-->position
create an array of given data type of given lenght from given pos
s=b'welcome'-->it consider everthing as a byte and in ascii value
frombuffer(s,dtype='s1',count=-1,offset=0)
result:[b'w' b'e',b'l'b'c',b'o',b'm',b'c']
offset means starts with that position
count means how many character you have to count


bydefault:
count=-1,offset=0
from buffer(s,dtype='s',count=3,offset=3)
[bw bc bi]

fromiter()-->iterable datastructue means list tuple string dictionary
fromiter()-->it wuill take the iterable sequence and convert it into array
with given count
fromiter(iterable,dtype,count)
iterable-list,tuble,any other sequence
dtype=str,int,float
count-->length of the resultant
by default count=-1

t=(10,20,30,40)
np.fromiter(t,dtype='float',count=-1)
[10. 20. 30.]
'''
a=np.array([10,20,30,40])
print(a)
#as-->means alias means duplicate
l=[10,20,30,40,50]
res=np.asarray(l,dtype='str',order='F')
help(np.asarray)           
print(res)
b=np.array([[1,2,3,4],[5,6,7,8]])
print(b)
r1=np.asarray(b,dtype='int',order='F')
print(r1)
for i in np.nditer(r1):
    print(i)
#here datatype is S1
#count=-1 means everything will vbe printed
s=b'welcome to adgitm'
#c=np.frombuffer(s,dtype='S1',count=-1,offset=0)
#print(c)

c=np.frombuffer(s,dtype='S1',count=10,offset=0)
print(c)
