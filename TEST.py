# author:YSL
# coding=gbk

'''
@Project ��12-6 
@File    ��TEST.py
@IDE     ��PyCharm 
@Author  ��С����
@Date    ��2022/12/6 13:07 
'''
import os

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

#1���򿪹ȸ������
dr=webdriver.Chrome()
dr.maximize_window()
#2�������ƹ���url
wyy_url='https://music.163.com/'
token={}
dr.get(wyy_url)
sleep(1)
dr.implicitly_wait(10)
move=dr.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/a")
ActionChains(dr).move_to_element(move).perform()
dr.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/a").click()
#���ѡ��������ʽ��¼
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/a").click()
#��ѡͬ��Э�����
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/div[2]/input").click()
#ѡ���ֻ��ŵ�¼
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div/div/div/div[1]/div[1]/a[1]/div").click()
sleep(1)
#ѡ�������¼
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/div[1]/a").click()
#�����ֻ��ź�����
phone_nums="18583698987"
secrets="YAOSL975714"
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/section/div[1]/div/input").send_keys(phone_nums)
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/section/div[2]/div/input").send_keys(secrets)
#3�������¼�������˺�
dr.find_element("xpath","/html/body/div[7]/div/div[2]/div/div[2]/section/a/div").click()
#�ֶ�������֤��
sleep(10)
#��������������Ӧ�ı���ȡ����
#��ȡ����
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
        #����ղ�
        sleep(1)
        # #��λ�����ͣԪ��
        # move = dr.find_element("xpath", "//*[@id=��auto-id-BDqLgK5TgMefuLda]/div/div/div[1]/div[3]/div/span[1]")
        # ActionChains(dr).move_to_element(move).perform()
        # dr.find_element("xpath", "//*[@id=��auto-id-BDqLgK5TgMefuLda]/div/div/div[1]/div[3]/div/span[1]").click()
        dr.find_element("xpath",'/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/a[1]').click()

        #����Ĭ�Ͽ�
        #�ж��Ƿ�Ϊvip����
        a=dr.find_element("xpath","/html/body/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div/a[1]/i").text
        if a=='����':
            # #���֮��Ӧ�赥
            dr.find_element("xpath", '//*[@id="content-operation"]/a[3]/i').click()
            sleep(1)
            dr.find_element("xpath","/html/body/div[11]/div[2]/div/div[2]/ul/li[*]//a[contains(text(),'300')]").click()
            print(f"{song}���ղسɹ�")
            dr.switch_to.default_content()
        else:
            print(f"{song}ΪVIP����������ղ�ʧ��")
            dr.switch_to.default_content()
