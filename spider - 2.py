#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import random
import time
import multiprocessing as mp
import sys

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'https://www.wnacg.com/albums'
               }
same_url = 'https://www.wnacg.com/albums'
main_url = 'https://www.wnacg.com'
all_url = 'https://www.wnacg.com/albums.html'
#保存地址
path = 'D:/lyt/comic1'
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"]




def get_user_agent():
    return random.choice(user_agent)

def download(task,name_set):	
	while task:
		num = task[0]
		pic_name = name_set[num]
		print(pic_name)
		del(task[0])

		pic_url = main_url + pic_name
		pic_html = requests.get(pic_url,headers = Hostreferer)
		pic_soup = BeautifulSoup(pic_html.text,"html.parser") 
		Picreferer = {'User-Agent':get_user_agent(),'Referer':'pic_url'}
		pic = 'https:' + pic_soup.find('img',class_='photo')['src'] 			
		html = requests.get(pic,headers = Picreferer)
		mess = BeautifulSoup(html.text,"html.parser")
		print(pic) 
					

		if html.status_code != 404:
			file_name = ('pic_'+str(num)+'.jpg')
			f = open(file_name,'wb')
			f.write(html.content)
			f.close()
		else:
			print("error in pic ",num)


	



if not os.path.exists('D:/lyt/comic1'):
        os.makedirs('D:/lyt/comic1')

if __name__ == "__main__":
	#找寻最大页数
	content = input('输入要搜索的内容的编码（不知道是什么编码(原来打字也可以））')
	start =  int(input('从第几页开始'))
	ul = same_url+'-index-page-'+'1'+'-sname-'+content+'.html'
	start_html = requests.get(ul, headers = Hostreferer)
	soup = BeautifulSoup(start_html.text,"html.parser")
	page = soup.find('div',class_='f_left paginator').find_all('a')
	if len(page) == 0:
		max_page = 1
		print('共1頁')
	else:
		max_page = int(page[-2].get_text())
		print('共',max_page,'页')

	for n in range(start,max_page+1):#页数循环

		#基础处理
		print('第',n,'页')
		try:
			ul = same_url+'-index-page-'+str(n)+'-sname-'+content+'.html'
			start_html = requests.get(ul, headers = Hostreferer)
			soup = BeautifulSoup(start_html.text,"html.parser")
		except:
			print('error in step1')
	    #获得一页内所有图集的名字
		all_a = soup.find('div',class_='gallary_wrap').find_all('a')#也可能是直接去掉target。。。
		#逐个图集进行处理
		for a in all_a:#图集循环
			flag = 0
			title = a.get_text() #提取标题 
			start_time = time.time()	
			if(title != ''):
				print("准备扒取："+title)

	            #创建目录
	            #win不能创建带？的目录
				try:
					if(os.path.exists(path+title.strip().replace('?',''))):
							print('目录已存在')
							flag=1
					else:
						os.makedirs(path+title.strip().replace('?',''))
						flag=0
					os.chdir(path + title.strip().replace('?',''))
				except:
					print('error in step2')

	            #获得页面数量
				try:
					if(flag == 1):
						print('已经保存完毕，跳过')
						continue
					href = main_url + a['href']
					html = requests.get(href,headers = Hostreferer)
					mess = BeautifulSoup(html.text,"html.parser")
					pic_num = mess.find('div',class_='asTBcell uwthumb').find('img')
					page_set = mess.find('div',class_='f_left paginator').find_all('a')
					if len(page_set) == 0:
						page_max = 1
					else :
						page_max = int(page_set[-2].get_text())
				except:
					print('error in step3')

				#获得所有图片的地址
				try:
					#图集页面循环
					name_set = []
					for page_num in range(1,page_max+1):
						#page_url = 'https://www.wnacg.com/photos-index-page-'+str(page_num)+'-aid-'++'.html'
						page_url = main_url+page_set[-2]['href'][0:19]+str(page_num)+page_set[-1]['href'][-15:]
						print(page_url)

						page_html = requests.get(page_url,headers = Hostreferer)
						page_soup = BeautifulSoup(page_html.text,"html.parser")
						all_name = page_soup.find('ul',class_='cc').find_all('a')
						#all_span = page_soup.find_all('span',class_='name')
						for photo_href in all_name:
							name = photo_href['href']
							name_set.append(name)
					print('目录获取完成')
				except:
					print('error in step4')

				task_set1=[]
				task_set2=[]

				task_num = len(name_set)
				for _ in range(task_num-1):
					if _ % 2 == 0:
						task_set1.append(_)
					elif _ % 2 == 1:
						task_set2.append(_)


				print(task_set1,task_set2)

				p1 = mp.Process(target=download,args=(task_set1,name_set))
				p2 = mp.Process(target=download,args=(task_set2,name_set))

				p1.start()
				p2.start()

				p1.join()
				p2.join()

				print('完成,','目前第',n,'頁')
				end_time = time.time()
				try:
					print('%d'%((end_time - start_time)/60),'min','%d'%((end_time - start_time)%60),'second')
					print('each photo','%d'%((end_time - start_time)/len(name_set)),'s')
				except:
					print('error in step6')
		print('第',n,'页完成')


				

