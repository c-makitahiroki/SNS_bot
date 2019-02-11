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
closebuttonSelector = 'button.ckWGn'  # 閉じるボタン
like_xpath_label = "/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span[contains(@class, 'glyphsSpriteHeart__outline__24__grey_9 u-__7')]"  # いいね(未押下)ボタン
follow_xpath_label = "/html/body/div[2]/div[2]/div/article/header/div[2]/div[1]/div[2]/button[contains(@class,'oW_lN _0mzm- sqdOP yWX7d        ')]"  # フォロー(未押下)ボタン


def init_values():
    count = 0
    likecount = 0
    followcount = 0
    return count, likecount, followcount


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


def open_tags(driver):
    # 最新の投稿を開く
    mediaList = driver.find_elements_by_css_selector(mediaSelector)
    for media in mediaList:
        media.click()


def extract_info(key):
    # キーワードをエンコードする
    tagname = key['keyword']
    key_count = key['count']
    encodedTag = urllib.parse.quote(tagname)  # URLに日本語は入れられないので、エンコードする
    encodedURL = tagSearchURL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    return encodedURL, key_count


def auto_click(xpath, count, driver):
    try:
        like_click = driver.find_element_by_xpath(xpath)
        like_click.click()
        count += 1
        return count, None
    except Exception as e:  # いいね！やフォローされていたら例外が出るのでスキップする。
        return count, e


def sns_loop_main(keyword_list, driver):
    # 設定ファイルから取得した情報に基づいて処理を行う。
    word_list = []
    likecount_list = []
    followcount_list = []

    for _, key in keyword_list.iterrows():
        exclude_flag = int(key['exclude'])  # 処理除外フラグ。これが1より大きい場合は処理しない。処理ログ用。
        like_flag = key['like_click']
        follow_flag = key['follow_click']
        likeword = key['keyword']
        print(likeword)
        if exclude_flag == 0:
            loop, likecount, followcount = init_values()
            URL, key_count = extract_info(key)
            driver.get(URL)
            time.sleep(3)
            driver.implicitly_wait(10)
            open_tags(driver)

            while loop < key_count:
                time.sleep(3)
                if like_flag == "Y":
                    likecount, errflag = auto_click(like_xpath_label, likecount, driver)
                if follow_flag == "Y":
                    followcount, errflag = auto_click(follow_xpath_label, followcount, driver)
                loop += 1
                driver.find_element_by_css_selector(nextPagerSelector).click()
                print("loop {} of {}".format(loop, key_count))
            word_list.append(likeword)
            likecount_list.append(likecount)
            followcount_list.append(followcount)
            driver.find_element_by_css_selector(closebuttonSelector).click()

        else:
            print("This word was previously used. Skip proccessing.")
    for word, lcount, fcount in zip(word_list, likecount_list, followcount_list):
        print(word, ":  likecount:  ", lcount, ":  followcount:  ", fcount)

    print("finished.")
