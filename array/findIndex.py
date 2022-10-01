from array import *

n=int(input('enter size of array: '))
arr=array('i',[])

print('enter values of array: ')

for i in range(n):
    x=int(input())
    arr.append(x)
    
#display elements of array

print("elements of array: ")
for i in arr:
    print(i)

#find index using loop
x=int(input('enter the value to be searched: '))
k=0
for i in arr:
    if i==x:
        print('index of element is: ',k)
    else:
        print("element not found in the array")


#using built in functions
print(arr.index(x))
