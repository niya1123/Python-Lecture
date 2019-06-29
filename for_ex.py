url = 'http://kindai-csg.com/'

# 普通のfor文
for u in url:
    print(u)

# for-else
for u in url:
    print(u, end="")
else:
    print()
    print('表示したやよ～')

# 内包表記
data = [x for x in range(0,10001) if x % 500 == 0]
print(data)