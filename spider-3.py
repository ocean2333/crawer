# coding=utf-8
# work with vpn !!!
import requests
from bs4 import BeautifulSoup
import os
import time
import zipfile

# http请求头
Hostreferer = {
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
	'Referer': 'https://www.wnacg.com/albums'
}
same_url = 'https://www.wnacg.com/albums'
main_url = 'https://www.wnacg.com'
all_url = 'https://www.wnacg.com/albums.html'
# 保存地址
path = 'D:/lyt/comic'

if __name__ == "__main__":
	if not os.path.exists('D:/lyt/comic'):
		os.makedirs('D:/lyt/comic')
	# 找寻最大页数
	print("this crawler work with vpn!!!\n")
	content = input('输入要搜索的内容：')
	start = int(input('从第几页开始'))
	path = 'D:/lyt/comic' + '/' + content
	if not os.path.exists(path):
		os.makedirs(path)
	os.chdir(path)
	ul = same_url + '-index-page-' + '1' + '-sname-' + content + '.html'
	try:
		start_html = requests.get(ul, headers=Hostreferer)
		soup = BeautifulSoup(start_html.text, "html.parser")
		page = soup.find('div', class_='f_left paginator').find_all('a')
		if len(page) == 0:
			max_page = 1
			print('共1頁')
		else:
			max_page = int(page[-2].get_text())
			print('共', max_page, '页')
	except:
		print("error in step0, maybe internet error")

	for n in range(start, max_page + 1):  # 页数循环
		# 基础处理
		print('第', n, '页')
		try:
			ul = same_url + '-index-page-' + str(n) + '-sname-' + content + '.html'
			start_html = requests.get(ul, headers=Hostreferer)
			soup = BeautifulSoup(start_html.text, "html.parser")
		except:
			print('error in step1')
			break
		# 获得一页内所有图集的名字
		all_a = soup.find('div', class_='gallary_wrap').find_all('a')
		# 逐个图集进行处理
		for a in all_a:  # 图集循环
			start_time = time.time()
			os.chdir(path)
			title = a.get_text()  # 提取标题
			if (title != ''):
				print("准备扒取：" + title)
				# 创建目录
				# win不能创建带？的目录
				try:
					if (os.path.exists(title.strip().replace('?', ''))):
						print('目录已存在')
						flag = 1
						break
					else:
						os.makedirs(title.strip().replace('?', ''))
						flag = 0
					os.chdir(title.strip().replace('?', ''))
				except:
					print('error in step2,making path progress')
					break

				# 获取下载地址
				download_href = ''
				try:
					href = main_url + a['href']
					html = requests.get(href, headers=Hostreferer)
					mess = BeautifulSoup(html.text, "html.parser")
					download_href = mess.find_all('a', class_='btn')[2]['href']
				# print(download_href)
				except:
					print('error in step3,geting href error')
					break

				# 下载zip文件并以二进制形式储存到文件中
				try:
					if (download_href != ''):
						down_url = main_url + download_href
						html = requests.get(down_url, headers=Hostreferer)
						mess = BeautifulSoup(html.text, "html.parser")
						zip_url = mess.find('a', class_='down_btn')['href']
						print(zip_url)
						zip = requests.get(zip_url, headers=Hostreferer)

						if html.status_code == 200:
							file_name = ('title' + '.zip')
							f = open(file_name, 'wb')
							f.write(zip.content)
							f.close()
							extracting = zipfile.ZipFile(file_name)
							extracting.extractall()
							extracting.close()
							os.remove(file_name)
						else:
							print("status code: ", html.status_code)
				except:
					print('error in step5')
					break
				print(title, '完成,', '目前第', n, '頁')
				end_time = time.time()
				try:
					print('%d' % ((end_time - start_time) / 60), 'min', '%d' % ((end_time - start_time) % 60), 'second')
				except:
					print('error in step6')
					break
		print('第', n, '页完成')
