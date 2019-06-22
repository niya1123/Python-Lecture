class ReplyHello():

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'こんにちは、{self.name}さん!')

if __name__ == "__main__":
    
    ReplyHello(input("名前を入力してください: ")).say_hello()
