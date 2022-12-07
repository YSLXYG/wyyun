# author:YSL
# coding=gbk

'''
@Project ：12-6 
@File    ：last_dir.py
@IDE     ：PyCharm 
@Author  ：小妖怪
@Date    ：2022/12/6 14:27 
'''
import os

dir=os.path.abspath(os.path.dirname(__file__))

with open(f'{dir}/song_name.txt',encoding='gbk')as f:
    songs=f.readlines()
    for song in songs:
        print(song.strip('\n'))
