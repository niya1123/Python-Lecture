class Serval():
    """
    参考例です.
    """

    def __init__(self, name: str, act: str):
        """
        引数のstrとか書いてるやつは明示的に型を示しており, プログラマはこれに従う必要があります.
        しかし, プログラムは従う必要はなくもし違う型のオブジェクトが与えられてもスクリプトを実行します.
        """
        self.name = name
        self.act = act

    def intro_serval(self):
        """
        文字列を扱う方法はさまざまあり, コメントアウトされているもののような方法もあります.
        """
        print("私の名前は" + self.name + "!" + self.act + "するのが得意なんだ!")
        # print('私の名前は%s!%sするのが得意なんだ!'%(self.name, self.act))
        # print('私の名前は{}!{}するのが得意なんだ!'.format(self.name, self.act))
        # print(f'私の名前は{self.name}!{self.act}するのが得意なんだ!')


if __name__ == "__main__":
    """
    sysは引数をとる場合や, プログラムの動作に関連するものを定義しているモジュールです.
    試しに, 引数として与えられてほしくないものを設定して正しく設定するよう促すものを書きました.
    sys.argvは引数を受け取るもので, 'python hoge.py 1 2'などで実行されればargvの中身は['hoge.py', '1', '2']となっています.
    """
    import sys

    if len(sys.argv) == 3:
        for i in sys.argv[1:]:
            try:
                if(type(float(i)) is float):
                    print("引数には数字以外を入力してください")
                    sys.exit(0)
            except ValueError:
                pass
    else:
        print("引数が正しく設定されていません")
        sys.exit(0)            

    s = Serval(sys.argv[1], sys.argv[2])
    s.intro_serval()
        