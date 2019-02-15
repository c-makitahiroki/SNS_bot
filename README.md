# SNS_bot
　Instagramで指定したハッシュタグの最新投稿から順にいいね！や投稿者のフォローをする。

# Enviroment
 - System & Softweare version
    - Windows 10 Home 64bit
    - Pycharm Commmunity Edition 2018.3.4
    - Python 3.6.5(Anaconda 3.5.2.0 64-bit)
 - Library version
    - pandas 0.24.0
    - selenium 3.141.0
    - numpy 1.15.4
    - urllib 
 - setting file
    - chromedriver.exe
      - chromeの自動テストソフトウェア。インターネットから別途ダウンロードする。
    - setting.json
      - SNSのログインURL、ユーザ、パスワードを記載する。
    - keyword_list.csv
      - excludeは処理分岐用。この値が"0"の行のみ処理を行う。それ以外の場合は処理をスキップする。履歴管理用に使用する。
      - like_clickがYの場合、該当のキーワードの投稿にいいね！をする。
      - follow_clickがYの場合、該当のキーワードの投稿者をフォローする。
      - keywordに検索したいキーワードを指定する。＃は必要なし。
      - countに良いねしたい数を指定する。
      - noteはメモ用。

# How to Use
 1. 動作環境を構築する。
   ※一例です。上記の環境が構築出来れば何でもよいです。
    1.1. anacondaをインストールする。 
   (参考URL)https://weblabo.oscasierra.net/python-anaconda-install-windows/
  1.2. anaconodaより、下記のライブラリをインストールする。
   (参考URL)https://www.toyo104-memo.com/entry/anaconda-conda
   anaconda-Navigator等を使っても良いと思います。
  1.3. Pycharmをインストールする。(任意)
   (参考URL)https://gammasoft.jp/python/pycharm-install-on-windows/
   コードを改良したり、プログラムを実行する時に使います。
   Pythonコードを実行できる環境があれば特に必要ありません。
 2. コードを実行する。
