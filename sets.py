#sets

num={1,2,3,4,"asim azad","must universty"}
print(type(num))
print(num)


#Methods of sets
marks=set()
marks.add(1)
marks.add(2)
marks.add(3)
marks.add(4)
marks.add("iam a student")
marks.add("Asim Azad")
print(marks)
print(type(marks))
marks.remove("Asim Azad")
print(marks)
marks.pop() 
print(marks)
marks.clear()
print(marks)

#methods on 2 sets 
set1={"asim Azad"}
set2={"iam a student of must univrsity"}
print(set1.union(set2))
print(set1.intersection(set2))


