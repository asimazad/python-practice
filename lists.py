#Lists practice

marks=[12,13,14,15,16,17,20,25,30,35]
print(marks)
print(len(marks))
print(marks[0])
print(marks[9])

student=["asim",20,4,"kashmir"]
print(student)
print(type(student))
print(student[2])

#List slicing

num=["asim","ajk",34,12,12,21,32,43,56,3,6,65,43]
print(num)
print(len(num))
print(num[0:2])
print(num[1:])
print(num[0:])
print(num[0:len(num)])


val=[1,2,5,4,3,6,7,4,3,7,8,9,8,7,10]
print(val.append(11))
print(val)
print(val.sort())
print(val)
print(val.sort(reverse=True))
print(val)
print(val.sort(reverse=False))
print(val)
print(val.insert(0,500))
print(val)
print(val.remove(3))
print(val)
print(val.pop(0))
print(val)

info=["asim",20,4,"ajk"]
print(info.append("qureshi"))
print(info)
print(info.insert(0,"myinfo"))
print(info)
print(info.remove("asim"))
print(info)
print(info.pop(0))
print(info)
#problem solving

marks=[]
sub1=input(("enter marks of 1st subject"))
sub1.append(marks)
sub2=input(("enter marks of 2nd subject"))
sub2.append(marks)
sub3=input(("enter marks of 3rd subject"))
sub3.append(marks)
sub4=input(("enter marks of 4th subject"))
sub4.append(marks)
sub5=input(("enter marks of 5th subject"))
sub5.append(marks)
print("your marks are--->",marks)

#check pallandrom

list=["r","a","c","e","c","a","r"]
print(list)
list_copy=list.copy()
list_copy.reverse()
if(list_copy==list):
    print("pallandrom")
else:
    print("Not pallandrom")


