text=['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']
list1=[]

for i in text :
    list1.append((chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2))))


print('list1 : ',' '.join(list1))

list2=[]
s=[i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]
list2=list(map(lambda x : (chr(int(x,2))),s))
print('list2 : ', ' '.join(list2))

list3=[]
def f(x) :
    return chr(int(x,2))
list3=list(map(f, s))
print('list3 : ',' '.join(list3))