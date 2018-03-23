# -*- coding:utf-8 -*-
import requests,os,lxml
from bs4 import BeautifulSoup
class Meizut():
    def __init__(self,url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
            "Referer": "http://www.mzitu.com/all/"}
        self.headers = headers
        self.url = url

    def req(self,url):
        '''请求方法'''
        start_html = requests.get(url,headers=self.headers)
        return start_html
    def soup(self,html):
        #爬取页面
        soup = BeautifulSoup(html.text,"lxml")
        return soup
    def test(self):
        nub = 1
        '''获取图片下载地址'''
        html_firsr = self.req(self.url)#获取网页text信息
        soup_first = self.soup(html_firsr)#爬取页面
        all_a = soup_first.find("ul",class_='archives').find_all('a')#查找标签
        #循环读取图片类型链接地址
        for a in all_a:
            href = a["href"]
            html_sec = self.req(href)#获取网页text信息
            html_Soup = self.soup(html_sec)#爬取页面
            max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
            ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
            for page in range(1, int(max_span) + 1):
                page_url = href + '/' + repr(page)  ##同上
                # print(page_url)  ##这个page_url就是每张图片的页面地址啦！但还不是实际地址！
                save_html = self.req(page_url)  # 同上
                save_Soup = self.soup(save_html)
                save_url = save_Soup.find('div', class_='main-image').find('img')['src']
                '''保存图片'''
                name = save_url[-9:-4]
                img = self.req(save_url)
                with open(os.getcwd() + "\\妹子\\" + name + '.jpg', 'wb') as f:
                    f.write(img.content)
                    print("第",nub,"张保存完成")
                f.close()
                nub = nub+1
if __name__ =="__main__":
    meizi_url = "http://www.mzitu.com/all/"
    thing = Meizut(meizi_url)
    '''我就验证下'''