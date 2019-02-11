# SNS_bot
　Instagramで指定したハッシュタグの最新投稿から順にいいねをする。

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
      - keywordに検索したいキーワードを指定する。＃は必要なし。
      - countに良いねしたい数を指定する。
      - excludeは処理分岐用。この値が"0"の行のみ処理を行う。それ以外の場合は処理をスキップする。履歴管理用に使用する。
      - noteはメモ用。
