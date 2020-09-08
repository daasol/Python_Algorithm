#1부터 100까지

#재귀함수
def recursive(x) :
    if x == 1 :
        return 1
    else :
        return x*recursive(x-1)
print(recursive(5))

#for
x=6
answer =1
for i in range(1, x) :
    answer*=i
print(answer)

#while
y=5
answer = 1
while True :
    if y==0 :  break
    else :
        answer*=y
        y-=1
print(answer)


#이진수 구하기 recursive
def binary(n) :
    if n < 2 :
        return str(n)
    else :
        return str(binary(n//2))+str(n%2)

print(binary(11))

#문자열 뒤집기
result = ''
def nag( string) :
    if string=='' :
        return  ''
    else :
        return str(string[-1])+str(nag(string[:-1]))


result=nag('abcd')
print(result)


def changInt(str) :
    if str=='' :
        return 0
    else :
        return int(str[0])+int(changInt(str[1:]))

print(changInt('2231'))