import pandas as pd 
import numpy as np
xl = pd.ExcelFile('4-施工图设计质量管控标准-暖通.xlsx')


# print(xl.sheet_names)
# sheet = xl.parse('1.1建筑')
# # print(sheet)
# sheet_list = list(sheet.iloc[:, 2].values)
# # print(sheet_list)
# exists_nan = True
# while exists_nan:
#     #除掉所有nan
#     exists_nan = False
#     for i in sheet_list:
#             if isinstance(i, float) and np.isnan(i):
#                 exists_nan = True
#                 sheet_list.remove(i)


# print(sheet_list)

# -*- coding: utf-8 -*-   
      
import os  
    
def file_name(file_dir):   
    file_names = []
    for root, dirs, files in os.walk(file_dir):  
        # print(root) #当前目录路径  
        # print(dirs) #当前路径下所有子目录  
        file_names = files
        # print(files) #当前路径下所有非目录子文件
        # print("----------------------------------------------------------------------")
    print("所有文件名是：")
    print(file_names)
    # legal_file_count = 0
    # for file_name in file_names:
    #     file_name = file_dir + "/" + file_name
    #     if '~$' in file_name:
    #         print("临时文件名是"+file_name)
    #         continue 
    #     legal_file_count += 1
    #     print("文件名是"+file_name)
    #     print("ok1")
    #     xl = pd.ExcelFile(file_name)
    #     print("ok2")
        
    #     print(xl.sheet_names)
    #     print("----------------------------------------------------------------------")
    # print("文件总数为"+str(legal_file_count))

# xl = pd.ExcelFile('总体设计审查要点'+'/'+'10-商业项目施工图审查要点-幕墙.xlsx')
# print(xl.sheet_names)
sheet_list = [
    ['1.1建筑'],
    [ '10.1幕墙'],
    [ '11.1导向标识'],
    [ '12.1夜景照明'],
    [ '2.1试桩、试锚', '2.3土方开挖',  '2.5结构-桩基、抗浮锚杆',  '2.7结构-地下室',  '2.9 结构-上部结构',  '2.11结构-幕墙、采光顶',  '2.13结构加固改造',  '2.15地质勘察', '2.16基坑支护及降水'],
    [ '3.1 给排水'],
    [ '4.1暖通'],
    [ '5.1电气'],
    [ '6.1弱电'],
    [ '7.1内装'],
    [ '审查要点'],
    [ '9.1室外管线综合']
]
file_name('总体设计审查要点')