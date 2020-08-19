'''
 2진수로 데이터 처리시 0.2를 정확히 표현할 수 없어 오류가 발생함.
 이 때 round()를 이용

'''


a = 0.3 + 0.6
print(a)

if a == 0.9 : print(True)
else : print(False)

print(round(a, 4))
''' 3째 자리까지 반올림'''

if round(a, 4) : print(True)
else : print(False)