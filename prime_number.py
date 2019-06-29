for i in range(2,1000):
    if 0 not in [i%j for j in range(2, i)]:
        print(i)
