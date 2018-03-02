list = ['item1', 'item2', 'item3' ]
for item in list:
    print(item)

index = 0
for item in list:
    print('index:' + str(index) + ', value:' + item)
    index += 1

for index in range(len(list)):
    print('index:' + str(index) + ', value:' + list[index])

for index, item in enumerate(list):
    print('index:' + str(index) + ', value:' + item)


newList = []
for item in list:
    newList.append(item + '-1')
print(newList)

# リスト内包表記
newList = [item + '-2' for item in list]
print(newList)

# if文あり
newList = [item + '-3' for item in list if not item.endswith('1')]
print(newList)

listV = ['a', 'i', 'u', 'e', 'o' ]
listC = ['k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w' ]

for V, C in zip(listV, listC):
    print(C+V)


for index, (V, C) in enumerate(zip(listV, listC)):
    print(index, C+V)
