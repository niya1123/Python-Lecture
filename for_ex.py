# coding: utf-8

url = 'http://kindai-csg.com/'

for u in url:
    print(u)

for u in url:
    print(u, end="")
else:
    print()
    print('表示したやよ～')

data = [x for x in range(0,10001) if x % 500 == 0]
print(data)