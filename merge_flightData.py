import pandas as pd
from os import listdir
'''
 函数名称：merge_flight_monthData
 函数作用：把2017年中某一个月中每天的航空数据数据表合并到一个表
 输入参数：存放某月每天数据的文件名
 输出参数：某月每天数据的汇总表
'''

def merge_flight_monthData(month_fileName):
    mergeData = []
    month = []
    day = []
    for fileName in listdir(month_fileName):                    # 读取文件夹中每个文件名
        data = pd.read_excel(month_fileName + '/' + fileName)   # 打开文件夹中的数据
        mergeData.append(data)                                  # 把数据添加到空list上
        file_Name_list = fileName.strip().split('.')            # 把数据文件名以'.'分割开
        month.append(file_Name_list[0])                         # 提取月份的值，添加到空list
        day.append(file_Name_list[1])                           # 提取天数的值，添加到空list

    for i in range(len(mergeData)):
        mergeData[i]['month'] = month[i]        # 对每个数据表添加月份列
        mergeData[i]['day'] = day[i]            # 对每个数据表添加日值列
        mergeData[i]['year'] = 2017             # 对每个数据表添加年份列

    month_Data = mergeData[0]                   # 合并所有数据表
    for i in range(len(mergeData) - 1):
        month_Data = pd.concat([month_Data, mergeData[i + 1]], ignore_index=True)

    return month_Data

def main():
    DataSet = []
    for month_fileName in listdir('2017年航班数据'):
        Data = merge_flight_monthData('2017年航班数据/{}'.format(month_fileName))
        DataSet.append(Data)

    fight_Data = DataSet[0]

    for i in range(len(DataSet) - 1):
        fight_Data = pd.concat([fight_Data, DataSet[i + 1]], ignore_index=True)

    fight_Data.to_excel('2017年各个航班数据.xls')

if __name__ == "__main__":
    main()