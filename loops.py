#while loops 
"""
i=1 
while i<=50:
    print("iam learning python")
    i+=1
"""
#problem solving
#print num ffrom 1-100
'''
i=1
while i<=100:
    print(i)
    i=+1
    '''
    #reverse counting
'''
i=100
while i>=1:
    print(i)
    i-=1
'''
#print Multiplication table of num n
"""
num=int(input("enter num to print table "))
i=1
while i<=10:
    print(num * i)
    i+=1
    """
#printing elements of list using loops
'''
nums=[11,42,53,14,56,87,99,32,43,54,32]
idx=0
while idx<len(nums):
    print("num at index",idx,"=",nums[idx])
    idx+=1
'''
#seach for a number in a tuple
'''
tup=(30,34,56,78,90,54,32,65,34,67,77,66,55)
a=78
i=0
while i<len(tup):
    if(tup[i]==a):
        print("found at index",i)
        break
    else:
        print("not found ")
    i+=1
'''
#break statment 
'''
i=0
while i<=10:
    print(i)
    if(i==5):
        break #stops at 5 and loop terminates
    i+=1
'''
#Continue statment 
"""
i=1
while i<=10:
    if(i%2==0): #odd numbers
        i+=1
        continue
    print(i)
    i+=1

#printing even  numbers
i=0
while i<=10:
    if(i%2==1): #Even numbers
        i+=1
        continue
    print(i)
    i+=1
"""
#For Loop
"""
marks=[1,3,4,5,6,7,8,]
for val in marks:
    print(marks)
"""
"""
str="iamlearningpython"
for char in str :
    if(char=='o'):
        print("o found")
        break
    print(str)
"""
"""
nums=[12,3,45,65,65,43,23,54,67,]

for el in nums:
    print(nums)
"""
"""
num=(21,45,67,87,54,32,54)
x=87
idx=0
for  el in num:
    if(el==x):
     print("found at idx",idx)
    idx+=1
"""  
