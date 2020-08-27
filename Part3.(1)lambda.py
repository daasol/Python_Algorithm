n = int(input())

array=[]
for i in range(n) :
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

#lambda : 이름없는 함수,
#lambda x : x[0] : lambda의 인자로 x를 넘겨주면, 리스트x의 0번째 값을 반환.
#sorted(iterable, *, key=None, reverse=False) True:내림차순, False:오름차순
array=sorted(array, key=lambda student:student[1])

for student in array :
    print(student[0], end=' ')