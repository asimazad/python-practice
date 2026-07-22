#Range function
"""
for el in range(10):
    print(el)
#print Even numbers
for val in range(0,20,2): 
    print (val)
    #print odd  numbers
for val in range(1,20,2): 
    print(val)
    """
#Nested for
"""
for i in range(1,10):
    for j in range (1,10):
        print(i,j)
"""
#patterns 
"""
for i in range(1,6):#right triangle
    print("*" * i)
"""
"""
for i in range (6,0,-1):# inverted right triangle
    print("*" * i)
"""
for i in range (1,6):
    print(" " ,* (5-i),end="")
    for j in range (1,i+1):
        print(j,end="")
        print ()
        

    
