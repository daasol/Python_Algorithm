

#list에서 slist로 삽입될 때, slist의 어디에 들어갈지 자리를 찾아 들어감

def find_insert(slist, temp) :
    for i in range(len(slist)) :
        if temp < slist[i] : #temp보다 큰 값 바로 앞에 삽입되야하므로
            return i #인덱스 값인 i를 반환
    return len(slist) #끝가지 돌았는데 못찾으면 마지막에 삽입



list = [5, 10, 66, 77, 54, 32, 11, 15]
slist = []
print(list)
while list :
    temp = list.pop(0)
    index = find_insert(slist, temp)
    slist.insert(index, temp) #insert(index, item) 특정 인덱스에 itemp 삽입

print(slist)





