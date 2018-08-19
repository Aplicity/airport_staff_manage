import pandas as pd
from os import listdir

'''
 函数名称：merge_passage_Data
 函数作用：把<通道客流数据>中某一年中每天的航空数据数据表合并到一个表
 输入参数：存放某年每天数据的文件名
 输出参数：某年每天数据的汇总表
'''

def merge_passage_Data(month_fileName, year):
    mergeData = []
    month = []
    day = []
    for fileName in listdir('通道客流数据/' + month_fileName):  # 读取文件夹中每个文件名
        data = pd.read_excel('通道客流数据/' + month_fileName + '/' + fileName)  # 打开文件夹中的数据
        mergeData.append(data)  # 把数据添加到空list上
        file_Name_list = fileName.strip().split('.')  # 把数据文件名以'.'分割开
        month.append(file_Name_list[0])  # 提取月份的值，添加到空list
        day.append(file_Name_list[1])  # 提取天数的值，添加到空list

    for i in range(len(mergeData)):
        mergeData[i]['month'] = month[i]  # 对每个数据表添加月份列
        mergeData[i]['day'] = day[i]  # 对每个数据表添加日值列
        mergeData[i]['year'] = year  # 对每个数据表添加年份列

    year_Data = mergeData[0]  # 合并所有数据表
    for i in range(len(mergeData) - 1):
        year_Data = pd.concat([year_Data, mergeData[i + 1]], ignore_index=True)

    year_Data = year_Data.dropna()

    return year_Data

def main():
    passage_Data_2017 = merge_passage_Data('2017年6月-12月', 2017)
    passage_Data_2018 = merge_passage_Data('2018年1月-4月',2018)
    passage_Data = pd.concat([passage_Data_2017, passage_Data_2018], ignore_index=True)
    passage_Data.to_excel('各通道各小时客流数据.xls')

if __name__ == '__main__':
    main()