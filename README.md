# SNS_bot
　Instagramで指定したハッシュタグの最新投稿から順にいいね！や投稿者のフォローをする。  
　既にいいね！済みの投稿、フォロー済みのフォロワーはスキップします。

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
 1.動作環境を構築する。  
　※一例です。上記の環境が構築出来れば何でもよいです。  
　　1.1.anacondaをインストールする。   
　　　(参考URL)https://weblabo.oscasierra.net/python-anaconda-install-windows/  
　　1.2.anaconodaより、上記「Library version」記載ののライブラリをインストールする。  
　　　(参考URL)https://www.toyo104-memo.com/entry/anaconda-conda  
　　　anaconda-Navigator等を使っても良いと思います。  
　　1.3. Pycharmをインストールする。(任意)  
　　　(参考URL)https://gammasoft.jp/python/pycharm-install-on-windows/  
　　　コードを改良したり、プログラムを実行する時に使います。  
　　　Pythonコードを実行できる環境があれば特に必要ありません。  
     
 2. Pythonコード(sns_main.py)を実行する。  
　　2.1. setting.jsonとkeyword_list.csvに必要な情報を入力する。  
　　2.2. sns_main.pyに、下記3つの引数を持たせて実行する。  
　　　第一引数：setting.jsonファイルのフルパス  
　　　第二引数：keyword_list.csvファイルのフルパス  
　　　第三引数：chromedriver.exeのフルパス  
　　　　※2019/02/15時点　chromedriverにしか対応していません。  
　　　　　settingフォルダに同梱していますので、こちらを使って頂くと良いかと思います。
