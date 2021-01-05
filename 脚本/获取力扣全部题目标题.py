# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : json.py  @Time : PyCharm -lqj- 2020-10-11 0011
import json
import logging
import os
import ssl

import requests

GETCWD = os.getcwd()


class LeetCodeClass(object):
    def sendGet(self, clock_url):
        response = requests.get(clock_url, headers=self.make_dict('header_leetcode'), verify=False)
        if response.status_code == 200:
            s = response.text.encode().decode('unicode_escape')
            return s

    def sendPost(self, data, clock_url):
        response = requests.session().post(clock_url,
                                           json=data,
                                           headers=self.make_dict('header_leetcode'),
                                           verify=False)
        if response.status_code == 200:
            s = response.text.encode().decode()
            return s

    # def json_parse(self, get):
    #     msg_ = json.loads(get)['stat_status_pairs']
    #     for i in msg_:
    #         name = str(i.get("stat")["question_id"]) + ' ' + i.get("stat")["question__title"]
    #         name = name.replace('?', '')
    #         # print(GETCWD)
    #         os.chdir(GETCWD + '/topic_name/')
    #         print(os.getcwd())
    #         suffix = ".py"
    #         newfile = name + suffix
    #         if not os.path.exists(newfile):
    #             f = open(newfile, 'w')
    #             print(newfile)
    #             f.close()
    #             print(newfile + " created.")
    #         else:
    #             print(newfile + " already existed.")

    def json_parse(self, msg_):
        # msg_ = json.loads(post)
        translations_ = msg_["data"]["translations"]
        for i in translations_:
            # print(i.get("questionId"))
            # print(i.get("title"))
            name = str(i.get("questionId") + '.' + i.get("title"))
            print(name)
            name = name.replace('?', '')
            name = name.replace(' ', '')
            os.chdir('E:\\ProjectsPyCharm\\LeetCode\\题库\\')
            print(os.getcwd())
            suffix = ".py"
            newfile = name + suffix
            if not os.path.exists(newfile):
                f = open(newfile, encoding='utf-8', mode='w')
                s = '''# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : {} \n'''.format(newfile)
                f.write(s)
                print(newfile)
                f.close()
                print(newfile + " 被创造.")
            else:
                print(newfile + " 已经存在.")

    def make_dict(self, file_name):
        k = []  # 存放 header的 key
        kv_list = []  # 存放 [key,value]
        with open(file_name, 'r') as file_obj:
            for line in file_obj:
                row_kv = line.strip().split(":", 1)
                if len(row_kv[0]) == 0: continue
                k.append(row_kv[0])
                kv_list.append(row_kv)
            dict_fromkeys = dict.fromkeys(k)
            for k_v in kv_list:
                value = k_v[1].strip()
                dict_fromkeys[k_v[0]] = value

            return dict_fromkeys


if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    logging.captureWarnings(True)
    object = LeetCodeClass()

    # url = 'https://leetcode-cn.com/api/problems/all/'
    # url = 'https://leetcode-cn.com/api/problems/algorithms/'
    # get = object.sendGet(url)

    # data = {
    #     "operationName": "getQuestionTranslation",
    #     "variables": {},
    #     "query": "query getQuestionTranslation($lang: String) {\n  translations: allAppliedQuestionTranslations(lang: $lang) {\n    title\n    questionId\n    __typename\n  }\n}\n"
    # }
    # post = object.sendPost(data, "https://leetcode-cn.com/graphql/")

    # print(post)
    t = open('demo.json', encoding='utf-8')
    post = json.load(t)
    object.json_parse(post)
