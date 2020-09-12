list = [5, 10, 66, 77, 54, 32, 11, 15]
slist = []

for i in range(len(list)) :
    slist.append(min(list))
    list.pop(list.index(min(list)))

print(slist)


def find_min(list) :
    min = list[0]
    index=0
    for key, item in enumerate(list) :
        if min >= item :
            min = item
            index = key
    print(index)

list = [5, 10, 66, 10, 77, 54, 1, 11, 15]
print(list)
find_min(list)

