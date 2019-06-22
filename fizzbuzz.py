class FizzBuzz():

    def __init__(self, start_value: int, end_value: int):
        self.start_value = start_value
        self.end_value = end_value

    def fizz_buzz(self):
        for i in range(self.start_value, self.end_value):
            if i % 15 == 0:
                print('Fizz Buzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)

if __name__ == "__main__":
    import sys
    for i in sys.argv[1:]:
        try:
            if(type(int(i)) is not int):
                print('引数が不正です')
                sys.exit(0)    
        except ValueError:
            print('引数が不正です')

    FizzBuzz(int(sys.argv[1]), int(sys.argv[2])+1).fizz_buzz()