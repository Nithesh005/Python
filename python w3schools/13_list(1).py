#  list
name = ["nithi","jenie","udhi","nithi","priya"]
print(name)
print(len(name))
print(type(name))

# access list item
print(name[1])
print(name[-1])
print(name[1:3])
if "jenie" in name:
    print("yes")

#change the list item
name[3] = "dharsh"
print(name)

#add list items
list2 = ["cse" , "ece"]
name.append("war")
name.insert(7,"waran")
name.extend(list2)
print(name)

#remove specifed item
name.remove("ece")
name.clear()
print(name)

#loop list
name = ["nithi","jenie","udhi","nithi","priya"]
for x in name:
    print(x)
# [print(x) for x in name]

for i in range(len(name)):
    print(name[i])

i = 0
while (i<len(name)):
    print(name[i],"while")
    i+=1

