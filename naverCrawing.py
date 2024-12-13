import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains
import time
from urllib import parse
import uuid
import re



def get_naver(search_datas, cnt_count):
    for searchKeyword,keyword in search_datas:
        searchKeyword = searchKeyword.strip()
        keyword = keyword.strip()
        time.sleep(5)

        #네이버 접속
        driver =webdriver.Chrome()

        driver.get(r"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={}".format(searchKeyword))
        time.sleep(3)
        driver.fullscreen_window()
        cnt = 0
        for i in range(100):
            cnt += 50
            if cnt >= cnt_count:
                break
            ActionChains(driver).send_keys(Keys.END).perform()
            time.sleep(2)
        f_ele=driver.find_elements(By.CSS_SELECTOR,".image_group img")
        f_ele = f_ele[:cnt_count]
        print(len(f_ele))

        f_ele = [ie.get_attribute("src") for ie in f_ele if ie.get_attribute("src").startswith("http")]
        print(f_ele[0])
        pattern =r".+src=(http.+(\.jpg|\.JPG|\.JPEG|\.PNG))"
        f_url = [parse.unquote( re.search(pattern=pattern,string=ele).groups()[0]) for ele in f_ele]
        icount=0
        for u in f_url:
            img_site=requests.get(u)
            time.sleep(0.7)
            #print(img_site.headers) 동일이미지 색출할때
            if int(img_site.headers["content-length"]) < 5100:
                continue
            simg = img_site.content
            save_path = f"d:\\imgs\\{keyword}\\"
            if not os.path.exists(r"d:\imgs"):
                os.mkdir(r"d:\imgs")
            if not os.path.exists(save_path):
                os.mkdir(save_path)
                expandfile = u.split(".")[-1]
                ru = "n"+str(uuid.uuid4())
                file_path = ru + "." + expandfile
                with open(save_path+file_path,"wb") as fp:
                    fp.write(simg)
                    icount+=1
        print()
        print("네잉버에서 {} 를 받았습니다.".format(icount))

        driver.quit();




time.sleep(600)