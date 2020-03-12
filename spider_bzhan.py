# coding=utf-8
import os
import random
import sys
import time
from multiprocessing import Pool

import requests
from bs4 import BeautifulSoup

# 1.输入cv号
# 1.5.获得该合集标题并创建文件夹
# 2.得到该网址下所有<figure class="img-box"中的图片地址
# 3.截去.jpg之后的部分
# 4.下载并储存

# v2.0:加入批量下载功能
#

head = 'https:'
http_head = 'https://www.bilibili.com'
http_site = http_head
http_cv = 'https://www.bilibili.com/read/cv'
http_ = 'https://h.bilibili.com/'
path = '/home/lyt/b/'
Hostreferer = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
num = 1
cvnum = []

while True:
    cv = input("输入cv号,输入空行结束")
    if cv == '':
        break
    cvnum.append(cv)

count = 0
#mod = input('选择模式：专栏=1，相簿=2')
mod = 1
for cv_num in cvnum:
    count = count + 1
    if int(mod) == 1:
        http_cv_new = http_cv + cv_num
        print(http_cv_new)
        start_html = requests.get(http_cv_new, headers=Hostreferer)
        start_soup = BeautifulSoup(start_html.text, "html.parser")
        # print(picset_title)
        '''
        try:
            picset_title = start_soup.find('h1', class_='title').text
            if(os.path.exists(path+picset_title.strip().replace('?', ''))):
                print('目录已存在')
                # exit()
            else:
                os.makedirs(path+picset_title.strip().replace('?', ''))
                flag = 0
                os.chdir(path + picset_title.strip().replace('?', ''))
        except:
            print('目录创建失败')
        '''
        os.chdir(path + '_paper')
        # print(start_soup)
        all_pic_figure = start_soup.find_all('img', attrs={'data-src': True})

        for fig in all_pic_figure:
            # print(fig)
            pic_site = fig['data-src']
            print(pic_site)
            #length = len(pic_site['data-src'])
            #pic_site = pic_site[:(length-(int(fig['width']) + int(fig['heeight']) + 8))]
            pic_html = requests.get((head + pic_site), headers=Hostreferer)
            try:
                if pic_html.status_code != 404:
                    file_name = (str(num)+'.jpg')
                    f = open(file_name, 'wb')
                    f.write(pic_html.content)
                    f.close()
                    num = num+1
                else:
                    break
            except:
                print(pic_html.status_code)
    elif int(mod) == 2:
        http_cv_new = http_ + cv_num
        print(http_cv_new)
        start_html = requests.get(http_cv_new, headers=Hostreferer)
        start_html.encoding = 'utf-8'
        start_soup = BeautifulSoup(start_html.text, "html.parser")
        picset_title = cv_num
        os.chdir(path + '_total_paper')
        '''
        try:
            if(os.path.exists(path+picset_title.strip().replace('?', ''))):
                print('目录已存在')
                # exit()
            else:
                os.makedirs(path + picset_title.strip().replace('?', ''))
                flag = 0
                os.chdir(path + picset_title.strip().replace('?', ''))
        except:
            print('目录创建失败')
        '''
        all_pic_figure = start_soup.find_all('div', class_='ssr-content')
        print(start_soup)
        print(all_pic_figure)
        for fig in all_pic_figure:
            # print(fig)
            pic_site = fig['data-photo-imager-src']
            print(pic_site)
            #length = len(pic_site['data-src'])
            #pic_site = pic_site[:(length-(int(fig['width']) + int(fig['heeight']) + 8))]
            pic_html = requests.get((head + pic_site), headers=Hostreferer)
            try:
                if pic_html.status_code != 404:
                    file_name = (str(num)+'.jpg')
                    f = open(file_name, 'wb')
                    f.write(pic_html.content)
                    f.close()
                    num = num+1
                else:
                    break
            except:
                print(pic_html.status_code)
    print("第", count, "个下载完了")
