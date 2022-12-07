# author:YSL
# coding=gbk

'''
@Project ：12-6 
@File    ：TEST.py
@IDE     ：PyCharm 
@Author  ：小妖怪
@Date    ：2022/12/6 13:07 
'''
import os

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

#1、打开谷歌浏览器
dr=webdriver.Chrome()
dr.maximize_window()
#2、网易云官网url
wyy_url='https://music.163.com/'
token={}
dr.get(wyy_url)
sleep(1)
dr.implicitly_wait(10)
move=dr.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/a")
ActionChains(dr).move_to_element(move).perform()
dr.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/a").click()
#点击选择其他方式登录
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/a").click()
#勾选同意协议服务
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/div[2]/input").click()
#选择手机号登录
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/a[1]/div").click()
sleep(1)
#选择密码登录
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div[1]/a").click()
#输入手机号和密码
phone_nums="18583698987"
secrets="YAOSL975714"
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/section/div[1]/div/input").send_keys(phone_nums)
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/section/div[2]/div/input").send_keys(secrets)
#3、点击登录网易云账号
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/section/a/div").click()
#手动滑动验证码
sleep(10)
#点击搜索框输入对应文本获取歌名
#获取歌名
dir=os.path.abspath(os.path.dirname(__file__))
with open(f'{dir}/song_name.txt',encoding='gbk')as f:
    songs=f.readlines()
    for song in songs:
        song=song.split()
        # wait=WebDriverWait(dr,10,0.5)
        dr.find_element("xpath", "/html/body/div[1]/div[1]/div/div[2]/div[1]/span/input[@name='srch']").clear()
        dr.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[1]/span/input[@name='srch']").send_keys(song)
        dr.find_element("xpath","/html/body/div[1]/div[1]/div/div[2]/div[1]/span/input[@name='srch']").send_keys(Keys.ENTER)
        dr.switch_to.frame("g_iframe")
        #点击收藏
        sleep(1)
        # #定位鼠标悬停元素
        # move = dr.find_element("xpath", "//*[@id=‘auto-id-BDqLgK5TgMefuLda]/div/div/div[1]/div[3]/div/span[1]")
        # ActionChains(dr).move_to_element(move).perform()
        # dr.find_element("xpath", "//*[@id=‘auto-id-BDqLgK5TgMefuLda]/div/div/div[1]/div[3]/div/span[1]").click()
        dr.find_element("xpath",'/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/a[1]').click()

        #返回默认框
        #判断是否为vip歌曲
        a=dr.find_element("xpath","/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div/a[1]/i").text
        if a=='播放':
            # #添加之对应歌单
            dr.find_element("xpath", '//*[@id="content-operation"]/a[3]/i').click()
            sleep(1)
            dr.find_element("xpath","/html/body/div[11]/div[2]/div/div[2]/ul/li[*]//a[contains(text(),'300')]").click()
            print(f"{song}，收藏成功")
            dr.switch_to.default_content()
        else:
            print(f"{song}为VIP尊享歌曲，收藏失败")
            dr.switch_to.default_content()
