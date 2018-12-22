'''
根据参数进行查询
   5-7 目的地 3  车次 6  出发地 8  出发时间 9  到达时间 10 历时 26 无坐 29 硬座
   24 软座 28 硬卧 33 动卧 23 软卧 21 高级软卧 30 二等座 31 一等座 32 商务座特等座
'''
import requests
from getStation import *

data = []  #整理好的车次信息
class_data = []   #分类后的车次信息

def query(start,end,date):
    data.clear()
    response = requests.get("https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date,start,end))
    # 将json数据转换为字典类型，通过键值对取数据
    result = response.json()
    result = result['data']['result']
    if isStationExist()==True:
        station =  eval(read())     # 读取所有车站并转换为dic类型
        if len(result)!=0:
            for i in result:
                tmp_list = i.split('|')
                start_ch = list(station.keys())[list(station.values()).index(tmp_list[6])]
                end_ch = list(station.keys())[list(station.values()).index(tmp_list[7])]
                seat = [tmp_list[3], start_ch, end_ch, tmp_list[8], tmp_list[9], tmp_list[10]
                    , tmp_list[32], tmp_list[31], tmp_list[30], tmp_list[21]
                    , tmp_list[23], tmp_list[33], tmp_list[28], tmp_list[24], tmp_list[29], tmp_list[26]]
                newSeat = []
                # 循环将座位信息中的空既“”，改成--这样好识别
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)  # 保存新的座位信息
                data.append(newSeat)
        return data  # 返回整理好的车次信息
#获取动车信息
def get_Dinfo():
    if len(data)!=0:
        for d in data:
            if d[0][0]=='D':
                class_data.append(d)
#移除动车信息
def remove_Dinfo():
    if len(data) != 0:
        for d in data:
            if d[0][0]=='D':
                class_data.remove(d)
#获取高铁信息
def get_Ginfo():
    if len(data)!=0:
        for d in data:
            if d[0][0]=='G':
                class_data.append(d)

#移除高铁信息
def remove_Ginfo():
    if len(data) != 0:
        for d in data:
            if d[0][0]=='G':
                class_data.remove(d)

#获取直达车信息
def get_Zinfo():
    if len(data)!=0:
        for d in data:
            if d[0][0]=='Z':
                class_data.append(d)

#移除直达车信息
def remove_Zinfo():
    if len(data) != 0:
        for d in data:
            if d[0][0]=='Z':
                class_data.remove(d)

#获取特快车信息
def get_Tinfo():
    if len(data)!=0:
        for d in data:
            if d[0][0]=='T':
                class_data.append(d)

#移除特快车信息
def remove_Tinfo():
    if len(data) != 0:
        for d in data:
            if d[0][0]=='T':
                class_data.remove(d)

#获取快速车信息
def get_Kinfo():
    if len(data)!=0:
        for d in data:
            if d[0][0]=='K':
                class_data.append(d)

#移除快速车信息
def remove_Kinfo():
    if len(data) != 0:
        for d in data:
            if d[0][0]=='K':
                class_data.remove(d)