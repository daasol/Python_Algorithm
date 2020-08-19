'''key - value'''


data = dict()

data['커피']='Coffee'
data['케이크']='Cake'

if '케이크' in data :
    print('케이크 있음')


''' key - keys(), value - values()'''

key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

for i in key_list :
    print(data[i])