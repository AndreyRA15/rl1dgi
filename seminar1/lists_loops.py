valuesList = [1, True, "SomeString", 3.14]

print(valuesList[0:3:2])


if 1 in valuesList:
    valuesList.append(2)
else:
    valuesList.remove(True)


index = 0
while index < len(valuesList):
    print(valuesList[index])
    index+=1

valuesList.insert(1,6.28)

for el in valuesList:
    print(el)

for ind in range(1,100,10):
    print(ind)
