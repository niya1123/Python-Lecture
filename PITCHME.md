# 第一回 Python導入

---

## Mac編

---?code=mac_install.sh
実行するコード一覧

---
?code=mac_install.sh
@[1](xcodeツールのインストール.
これ以降の作業を実行するために必要です.
英語のポップアップが表示されますが、基本的にAgreeを選択していればOKです.)

---
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Homebrewというツールのダウンロード.Homebrewとは、色んなツールをダウンロードするためのツールで、これさえあれば大抵の機能は追加できる

---
```sh
brew -v
```
brewが入ってるかどうかの確認.brewのバージョンが表示される