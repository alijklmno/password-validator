listOne = ['item1', 'item2', 'item3']
listTwo = ['item1', '1item', '2item', '3item', 'item2']

count = 0
for i in listOne:
    for j in listTwo:
        if i == j:
            count += 1

print(count)