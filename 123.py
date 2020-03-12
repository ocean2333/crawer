import requests
from bs4 import BeautifulSoup

def reqU(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""



def fillULIST(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])


def printU(ulist,num):
    print("{:^10}{:^6}{:^10}".format("名称","排名","地址"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}{:^6}{:^10}".format(u[0],u[1],u[2]))
    print("suc"+str(num))

def main():
    uinfo=[]
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    html=reqU(url)
    fillULIST(uinfo,html)
    printU(uinfo,20)

main()