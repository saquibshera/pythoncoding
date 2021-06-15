persons=["saquib","aamir","umer"]
persons.append("Abid")
persons.insert(1,"salman")
persons.remove("saquib")
length=persons.__len__()
print("the number of persons is "+str(length))
for person in persons:
    print(person)