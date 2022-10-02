# to add a value to the elements of an array

# by using loop

from numpy import *
arr=array([2,3,4,5,6,7,8])
print('given array',arr)

print('after adding 5')
for i in range(0,len(arr)):
    arr[i]=arr[i]+5
print('using for loop',arr)


# by using array built in operations
arr=array([2,3,4,5,6,7,8])
arr1=arr+5

print('using array operation',arr1)

# addition of two array

print('addition of two arrays')

print('using loop')
i=0
j=0
for i in range(0,len(arr)):
    arr[i]=arr[i]+arr1[j]
    j+=1
print(arr)




# by using array built in operations
print('using built in operations')

arr=array([2,3,4,5,6,7,8])
arr2=arr1+arr
print(arr2)


print(sin(arr))
print(log(arr))
print(min(arr))
print(max(arr))


