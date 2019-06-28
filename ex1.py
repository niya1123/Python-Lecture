value = 10
fruit_box = ['apple', 'orange', 'banana']

if(len(fruit_box) == value):
    print(f'箱の中には果物が{value}個あります')
elif(len(fruit_box) < value):
    print(f'箱の中には果物が{value}個以下あります')    
elif(len(fruit_box) > value):
    print(f'箱の中には果物が{value}個以上あります')
else:
    print('変数:valueの値が不正です')