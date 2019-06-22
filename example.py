class SayYourName():

    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name + "さん、こんにちは!")


if __name__ == "__main__":
    s = SayYourName(input("名前を入力してください: "))
    s.say_name()
