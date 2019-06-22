class Serval():

    def __init__(self, name, act):
        self.name = name
        self.act = act

    def intro_serval(self):
        print("私の名前は" + self.name + "!" + self.act + "するのが得意なんだ！")  

if __name__ == "__main__":
    name, act = input("名前と行動を入力してください: ").split()
    
    s = Serval(name, act)
    s.intro_serval()
        