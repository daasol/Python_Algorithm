def fib1(a) :
    if a == 0 or a==1 :
        return 1
    else :
        return fib1(a-2)+fib1(a-1)

print(fib1(5))


'''
fib(5) = fib(4) + fib(3) = 5 + 3
fir(4) = fib(3) + fib(2) = 3 + 2
fib(3) = fib(2) + fib(1) = 2 + 1
fib(2) = fib(1) + fib(0) = 1 + 1

fib(0)=1
fib(1) = 1
fib(2) = 2
fib(3) = 3
fib(4) = 5
'''

def fib2(a) :
    if a == 0  :
        return 0
    elif a==1 :
        return 1
    else :
        return fib2(a-2)+fib2(a-1)

def comma(n) :
    if len(n) < 3 :
        return n
    else :
        return comma(n[:len(n)-3])+','+n[len(n)-3:]

print(comma('10000000'))
n=10000000
n = format(n, ',')
print(n)