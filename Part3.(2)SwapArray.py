n, k = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB.sort(reverse=True)

for i in range(k) :
    listA[i] , listB[i] = listB[i], listA[i]

print(sum(listA))
