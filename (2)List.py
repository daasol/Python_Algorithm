''' 대괄호, (,) 쉼표로 원소 구분, 인덱스로 원소 접근 '''

''' 기본 list선언'''
a=[1,2,3,4,5,6,7,8,9]
b=list()

'''
 인덱싱 : 특정 원소 접근. 뒤에서 첫번째
'''
print(a[-1])

''' 슬라이싱 n번째부터 m-1번째 까지'''
print(a[1:4])

''' comprehension : 리스트 초기화 
홀수 제곱 리스트, 1~9 제곱 리스트'''
array=[]
for i in range(20) :
    if i%2 == 1 :
        array.append(i)

array=[i * i for i in range(1,10)]

array.append(10)
print(array)

R_array=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

R_array.sort()
print(R_array)

array.reverse()
print(array)

array.sort(reverse=True)
print(array)

print(array.count(1))

array.remove(81)
print(array)

'''set'''

remove_set = {9,10}

result = [i for i in R_array if i not in remove_set]
print(result)

