#Dictionary 

record = {
    "name":"Asim Azad",
    "Age":21,
    "program":"Software engineering",
    "semester":"4th",
    "subjects":["oop,dsa","python"],
    "topics":("dictionary"),
    "gpa":3,
    "marks":{    #Nested dictionary
        "se fundalmental":20,
        "OOP":23,
        "DSA":30,      
}

}
#Methods
new_record={"city":"mirpur",}
record.update(new_record)
print(record)
#print(record)
'''
record["name"]="Haroon Bilal"
print(record["name"])
print(record["topics"])
print(record["marks"])
'''
#print(["marks"]["DSA"])
#print(record.keys)
#print(len(record))
#print(record.values)
#print(record.items())
#print(record.pairs[1])
#print(record.get["name"])
