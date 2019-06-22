class Serval():

    def __init__(self, name: str, act: str):
        self.name = name
        self.act = act

    def intro_serval(self):
        print("私の名前は" + self.name + "!" + self.act + "するのが得意なんだ！")  

if __name__ == "__main__":
    import sys

    for i in sys.argv[1:]:
        try:
            if(type(float(i)) is float):
                print("引数には数字以外を入力してください")
            sys.exit(0)    
        except ValueError:
            pass

    s = Serval(sys.argv[1], sys.argv[2])
    s.intro_serval()
        