from selenium import webdriver

import argparse
import json
import pandas as pd
import codecs

from util import util_sns


def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("setting_file", type=str)
    parser.add_argument("keyword_list", type=str)
    parser.add_argument("chrome_driver", type=str)
    args = parser.parse_args()
    return args


def _load_json(setting_file):
    f = open(setting_file, 'r')
    jsonData = json.load(f)
    return jsonData


def _load_keyword_list(keyword_list):
    with codecs.open(keyword_list, "r", "UTF-8", "ignore") as file:
        keyword = pd.read_csv(file, header=0)
    return keyword


def main(args):
    SNSInfo = _load_json(args.setting_file)
    keyword_list = _load_keyword_list(args.keyword_list)

    driver = webdriver.Chrome(executable_path=args.chrome_driver)  # ここには任意のWebdriverを入れる
    util_sns.login_SNS(SNSInfo, driver)
    # util_sns.likeclick(keyword_list, driver)
    util_sns.sns_loop_main(keyword_list, driver)

if __name__ == '__main__':
    main(parse_args())
