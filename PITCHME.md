## 第三回 Pythonの基本的文法

---

前回, クラスをやりましたがそもそもPythonの基本文法について詳しく説明していなかったので今回はそこからやっていきたいと思います

---

### if文

---?code=if_ex.py

pythonのif文はこのように書かれます.

---?code=if_ex.py

@[6-11](if文のインデントは必ず必要です.半角スペース4つorタブ空白2つが推奨されています!)

---

### for文

---?code=for_ex.py

@[5-6](普通のfor文.if文同様インデント必須.)
@[8-12](python独特の構文.else句はforによる繰り返しが終了した直後に1度だけ実行します.)
@[14](これめっちゃ特殊だけどクッソ便利.次のページで詳しく説明する.)

---

### 内包表記とは

---

内包表記は, リスト, 集合, 辞書の生成に使われる.基本例は以下.

リストの生成: [繰り返し変数を使った要素の処理 for 繰り返し変数 in データ構造]

集合, 辞書の生成: {繰り返し変数を使った要素の処理 for 繰り返し変数 in データ構造}

---

また, 内包表記には前置ifと後置ifを置くことができ, 前者はif-else文の場合, 後者はifのみの場合というように使い分ける.以下に例を示す.

```python
zenti = ['FizzBuzz' if x % 15 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x for x in range(1, 1001)]

kouti = [x**2 for x in range(10) if x % 3 == 0]
```

---

慣れるまでの前置ifの内包表記の書き方.

```python
zenti = []
for x in range(1,1001):
    if(x % 15 == 0):
        zenti.append('FizzBuzz')
    elif(x % 3 == 0):
        zenti.append('Fizz')
    elif(x % 5 == 0):
        zenti.append('Buzz')
    else:
        zenti.append(x)
```

というのをまず実装する.

---

```python
zenti = []
for x in range(1,1001):
    if(x % 15 == 0):
        zenti.append('FizzBuzz')
    elif(x % 3 == 0):
        zenti.append('Fizz')
    elif(x % 5 == 0):
        zenti.append('Buzz')
    else:
        zenti.append(x)
```
@[3-10](ここをどう考えるかというと, まずif文の処理を最初に書く.次にif文の条件式を書く.次にelse文には次のelif文の処理を書く.これを順繰りに書いていく.)

---

### while文

---?code=while_ex.py


