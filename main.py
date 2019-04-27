import jieba
import numpy as np
import pandas as pd

import math
# #先不考虑停用词
import os

#注释：python3没有has_key

def stop_words_list(filepath):
    with open(filepath,'r',encoding='utf-8') as file:
        stop_words = [line.strip() for line in file.readlines()]
        # print(stop_words[:100])
        return stop_words

def get_words_freq(stop_words, sentence1, sentence2):
    #参数：两个文本字符串
    #返回结果：所有词语出现的次数(分别用字典的形式存储)
    #待调参数：var_len = 15  var_sim = 0.1设定两个文本的长度相差var_len以上时相似度为var_sim
    words1 = jieba.cut(sentence1.strip())
    words1 = [word for word in words1]
    words2 = jieba.cut(sentence2.strip())
    words2 = [word for word in words2]

    var_len = 20  
    var_sim = 0.1
    if abs(len(words1) - len(words2)) > var_len:
        return var_sim

    #分词之后要进行停用词去除
    for word in words1:
        if word in stop_words:
            words1.remove(word)
    for word in words2:
        if word in stop_words:
            words2.remove(word)
    
    word1_freq_dict = cal_fre(words1)
    word2_freq_dict = cal_fre(words2)
    word1_freq_dict, word2_freq_dict = merge_dict_array(word1_freq_dict, word2_freq_dict)
    # print("word1_freq_dict是：----------------------------")
    # print(word1_freq_dict)
    # print("word2_freq_dict是：-----------------------------")
    # print(word2_freq_dict)
    sim = cal_sim(word1_freq_dict, word2_freq_dict)
    threshold = 0.7
    if sim > threshold:
        print("相似度是"+str(sim))
    return sim

    
def cal_fre(word_array):
    #输入：词语数组
    #输出：统计词语出现次数的字典
    word_freq_dict = {}
    if len(word_array) == 0:
        return word_freq_dict
    for word in word_array:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1
    return word_freq_dict

def merge_dict_array(dict1, dict2):
    #输入：两个字典
    #返回：两个新的字典
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    new_dict1 = dict1
    new_dict2 = dict2
    for key2 in keys2:
        if key2 in keys1:
            pass
        else:
            new_dict1[key2] = 0
    
    for key1 in keys1:
        if key1 in keys2:
            pass
        else:
            new_dict2[key1] = 0
    # print("new_dict1是：————————————————————————————————————————")
    # print(new_dict1)
    # print("new_dict2是：————————————————————————————————————————")
    # print(new_dict2)
    
    return new_dict1, new_dict2
    

def cal_sim(dict1, dict2):
    #首先保证键值排序
    # https://www.cnblogs.com/xiaxiaoxu/p/9743357.html
    sorted_dict1 = dict(sorted(dict1.items(),key=lambda x:x[0]))
    sorted_dict2 = dict(sorted(dict2.items(),key=lambda x:x[0]))
    # print("sorted_dict1----------------------------------------------")
    # print(sorted_dict1)
    # print("sorted_dict2----------------------------------------------")
    # print(sorted_dict2)
    vector1 = list(sorted_dict1.values())
    vector2 = list(sorted_dict2.values())
    # print("vector1-------------------------------------")
    # print(vector1)
    # print("vector2-------------------------------------")
    # print(vector2)
    sim = cosVector(vector1, vector2)
    # print("相似度是"+str(sim))
    return sim

def cosVector(x,y):
    if(len(x)!=len(y)):
        print('error input,x and y is not in the same space')
        return 0
    if len(x) == 0:
        return 0
    result1=0.0
    result2=0.0
    result3=0.0
    for i in range(len(x)):
        result1+=x[i]*y[i]   #sum(X*Y)
        result2+=x[i]**2     #sum(X*X)
        result3+=y[i]**2     #sum(Y*Y)
    if result2*result3 == 0:
        return 0
    cos = result1/((result2*result3)**0.5)
    return cos


def read_file(file_path):
    #输入：文件名
    #返回：审查内容的列表
    excel_content = pd.read_excel(io = file_path).values
    print("excel内容是：")
    print(excel_content)
    check_points = list(pd.DataFrame(excel_content).iloc[:, 3].values)
    #多轮去除nan
    for i in check_points:
        # print(type(i))
        if isinstance(i, float) and np.isnan(i):
            check_points.remove(i)
    for i in check_points:
        if isinstance(i, float) and np.isnan(i):
            check_points.remove(i)
            # print("存在nan")
    for i in check_points:
        if isinstance(i, float) and np.isnan(i):
            # print(type(i))
            check_points.remove(i)
            # print("存在nan")
    with open('excel1.txt', 'w') as f:     # 打开test.txt   如果文件不存在，创建该文件。
        f.write(str(check_points))  # 把变量var写入test.txt。这里var必须是str格式，如果不是，则可以转一下。
    return check_points

def read_excel_file(file_name, sheet_name_list):
    #输入：文件名, 所有审查内容所在的表（list类型）
    #根据文件名来读取某个excel文件中的某一个sheet下的内容
    
    xl = pd.ExcelFile(file_name)
    print(xl.sheet_names)
    total_items = []
    for sheet_name in sheet_name_list:
        sheet = xl.parse(sheet_name)
        total_items += list(sheet.iloc[:, 2].values)
        print("sheetname是"+sheet_name+"------------------")
        for i in list(sheet.iloc[:, 2].values):
            print(i)
    exists_nan = True
    while exists_nan:
        #除掉所有nan
        exists_nan = False
        for i in total_items:
                if isinstance(i, float) and np.isnan(i):
                    exists_nan = True
                    total_items.remove(i)
    # print("除掉所有nan后的total_items是--------------------------")
    # for item in total_items:
    #     print(item)
    # print(total_items)
    return total_items


def read_txt(file_path):
    f = open(file_path,"r")   
    lines = f.readlines()      #读取全部内容 ，并以列表方式返回  
    for line in lines:  
        line=line.strip('\n')
        # print(line)
    return lines

        # line=line.strip('\n')
        # if len(line) > 0:
        #     print (line) 
        # else:
        #     lines.remove(line)
    # with open(file_path, 'w') as f:     # 打开test.txt   如果文件不存在，创建该文件。
    #     f.write(str(lines))  # 把变量var写入test.txt。这里var必须是str格式，如果不是，则可以转一下。

def compare(stop_words,lines1, lines2):
    #输入：2个字符串数组
    #输出：2个相似得语句集合
    threshold = 0.7
    order = 1   #统计下标从1开始
    for line1 in lines1:
        similar_sentences = []
        for line2 in lines2:
            if get_words_freq(stop_words,line1, line2) > threshold:
                similar_sentences.append(line2)
        if len(similar_sentences) > 0:
            similar_sentences.append(line1)
            print("相似度%f以上的语句有----------------------------"%threshold)
            print(similar_sentences)

def test():
    file_dir = '总体设计审查要点'
    files = get_file_names('file_dir')
    stop_words =  stop_words_list("stop_words.txt")
    file_num = len(files)
    append_lines =""
    for file1 in range(file_num-1):
        for file2 in range(file1+1, file_num):
            lines1 = read_txt(files[file1])
            lines2 = read_txt(files[file2])
            info = files[file1][:2]+"和"+files[file2][:2]+"的相同审查内容有-------------------------------------"
            print(info)
            compare(stop_words, lines1, lines2)
            
        
def append_lines(file_path, lines):
    pass
    #输入:文件路径和

def get_file_names(file_dir):   
    #file_dir为文件夹路径
    file_names = []
    for root, dirs, files in os.walk(file_dir):  
        # print(root) #当前目录路径  
        # print(dirs) #当前路径下所有子目录  
        file_names = files
        # print(files) #当前路径下所有非目录子文件
        # print("----------------------------------------------------------------------")
    
    legal_file_count = 0
    file_num = len(file_names)
    for i in range(file_num):
        if '~$' in file_names[i]:
            # print("临时文件名是"+file_names[i])
            file_names.remove(file_names[i])        #删除临时文件
            continue 
        file_names[i] = file_dir + "/" + file_names[i]
        legal_file_count += 1
    # print("文件总数为"+str(legal_file_count))
    # print("所有文件名是：")
    # print(file_names)
    return file_names

# test()
sheet_list = [
    ['1.1建筑'],
    [ '10.1幕墙'],
    [ '11.1导向标识'],
    [ '12.1夜景照明'],
    [ '2.1试桩、试锚', '2.3土方开挖',  '2.5结构-桩基、抗浮锚杆',  '2.7结构-地下室',  '2.9结构-上部结构',  '2.11结构-幕墙、采光顶',  '2.13结构加固改造',  '2.15地质勘察', '2.16基坑支护及降水'],
    [ '3.1 给排水'],
    [ '4.1暖通'],
    [ '5.1电气'],
    [ '6.1弱电'],
    [ '7.1内装'],
    [ '审查要点'],
    [ '9.1室外管线综合']
]

read_excel_file("总体设计审查要点/2-商业项目施工图审查要点-结构.xlsx", [ '2.1试桩、试锚', '2.3土方开挖',  '2.5结构-桩基、抗浮锚杆',  '2.7结构-地下室',  '2.9结构-上部结构',  '2.11结构-幕墙、采光顶',  '2.13结构加固改造',  '2.15地质勘察', '2.16基坑支护及降水'])





