'''
获取车站信息
'''
import re
import os
import requests

def getStation():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9077"
    response = requests.get(url, verify= True)
    station = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    station = dict(station)
    station = str(station)
    write(station)
def write(station):
    file = open("station.text",'w',encoding='utf-8')
    file.write(station)
    file.close()
def read():
    file = open("station.text",'r',encoding='utf-8')
    data = file.readline()
    file.close()
    return data
def isStationExist():
    exist = os.path.exists("station.text")
    return exist
