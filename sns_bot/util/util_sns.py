import time
import numpy as np
import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja"  # .format()で{}の中の値を入れられるようになっている
mediaSelector = 'div.EZdmt'
nextPagerSelector = 'a.coreSpriteRightPaginationArrow'  # 次へボタン
closebuttonSelector = 'button.ckWGn' # 閉じるボタン
like_xpath_label = "/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span[contains(@class, 'glyphsSpriteHeart__outline__24__grey_9 u-__7')]" # いいねボタン


def login_SNS(SNSInfo, driver):
    driver.get(SNSInfo['SNSInfo']['loginURL'])
    time.sleep(3)
    elem_search_word = driver.find_element_by_class_name("_2hvTZ")
    elem_search_word.send_keys(SNSInfo['SNSInfo']['USER'])
    password = driver.find_element_by_name('password')
    password.send_keys(SNSInfo['SNSInfo']['Pass'])
    driver.find_element_by_css_selector("._0mzm-.sqdOP.L3NKy").click()
    driver.implicitly_wait(10)
    time.sleep(5)


def likeclick(keyword_list, driver):
    # csvで設定されているキーワードを自動でいいねする。
    def _extract_info(key):
        # キーワードをエンコードする
        tagname = key['keyword']
        key_count = key['count']
        encodedTag = urllib.parse.quote(tagname)  # URLに日本語は入れられないので、エンコードする
        encodedURL = tagSearchURL.format(encodedTag)
        print("encodedURL:{}".format(encodedURL))
        return encodedURL, key_count

    def _serch_tags():
        mediaList = driver.find_elements_by_css_selector(mediaSelector)
        for media in mediaList:
            media.click()

    likeword_list = []
    likecount_list = []

    for _, key in keyword_list.iterrows():
        exclude_flag = int(key['exclude'])  # 処理除外フラグ。これが1より大きい場合は処理しない。処理ログ用。
        likeword = key['keyword']
        print(likeword)
        if exclude_flag == 0:
            loop = 0
            likecount = 0
            URL, key_count = _extract_info(key)
            driver.get(URL)
            time.sleep(3)
            driver.implicitly_wait(10)
            _serch_tags()
            likeword_list.append(likeword)

            while loop < key_count:
                try:
                    time.sleep(3)
                    myDynamicElement_like_xpath = driver.find_element_by_xpath(like_xpath_label)
                    myDynamicElement_like_xpath.click()
                    loop += 1
                    likecount += 1
                    print("loop {} of {}".format(loop, key_count))
                    driver.find_element_by_css_selector(nextPagerSelector).click()
                except Exception as e:  # いいね！されていたら例外が出るのでここでスキップする。
                    driver.find_element_by_css_selector(nextPagerSelector).click()
                    loop += 1
                    print("loop {} of {}".format(loop, key_count))
            driver.find_element_by_css_selector(closebuttonSelector).click()
            likecount_list.append(likecount)

        else:
            print("This word was previously used. Skip proccessing.")
    for word, count in zip(likeword_list, likecount_list):
        print(word, ":  likecount:  ", count)

    print("finished.")
