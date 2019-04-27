import jieba
# #先不考虑停用词

def get_words_freq(sentence1, sentence2):
    #参数：两个文本字符串
    #返回结果：所有词语出现的次数(分别用字典的数组形式存储)
    sentence1 = '应明确表示各出入口与市政道路标高、交通流线及站点之间关系。应与景观竖向设计一致。主要道路应设计公交车站和出租车泊接停靠站。'
    sentence2 = '万达广场/万达茂如采用地下室停车，需沿不同方向主要道路设两个或两个以上车库出入口，以分解交通。不宜在商铺前横向设车道出入口。出入口坡道应双进双出，不得做单车道，且净宽不小于8米宜为9米。'
    words1 = jieba.cut(sentence1.strip())
    words1 = [word for word in words1]
    words2 = jieba.cut(sentence2.strip())
    words2 = [word for word in words2]
    word1_freq_array = cal_fre(word1)
    word2_freq_array = cal_fre(word2)

    
def cal_fre(word_array):
    #输入：词语数组
    #输出：统计词语出现次数的字典数组
    word_freq_array = []
    if len(word_array) == 0:
        return word_freq_array
    for word in word_array:
        if word_freq_array.has_key(word):
            word_freq_array[word] += 1
        else:
            word_freq_array[word] = 1
    return word_freq_array

def merge_dict_array(dict_array1, dict_array2):
    #输入：两个字典数组
    #返回：两个新的字典数组,参数本身已经修改
    keys1 = list([dict.keys() for dict in dict_array1])
    keys1 = [key for key in keys for keys in keys1]
    keys2 = list([dict.keys() for dict in dict_array2])
    keys2 = [key for key in keys for keys in keys2]
    #[dict_keys(['a']), dict_keys(['b'])]=>([['a'],['b']]) =>['a','b']
    for key in keys2:
        if key in keys1:
            pass
        else:
            dict_array1.append({key:0})

    for key in keys1:
        if key in keys2:
            pass
        else:
            dict_array2.append({key:0})

def cal_sim(dict_array1, dict_array2):
    #首先保证键值顺序
    
    return 0

def cosVector(x,y):
    if(len(x)!=len(y)):
        print('error input,x and y is not in the same space')
        return
    result1=0.0
    result2=0.0
    result3=0.0
    for i in range(len(x)):
        result1+=x[i]*y[i]   #sum(X*Y)
        result2+=x[i]**2     #sum(X*X)
        result3+=y[i]**2     #sum(Y*Y)
    simalariy =  result1/((result2*result3)**0.5))
    

# import numpy as np
# import pandas as pd

# file_path = '1-商业项目施工图审查要点-建筑.xlsx'
# excel_ori = pd.read_excel(io = file_path)
# a = excel_ori.values
# print(a)
# a = a[a[:, 7] > a[:, 8]]
# data_df = pd.DataFrame(a)
 
# data_df.columns = ['单据号','商品编码','商品售价','销售数量','消费金额','消费产生的时间','收银机号','实际收费','消费金额']
# data_df.index = ['a','b','c','d','e','f','g','h']
 
# writer = pd.ExcelWriter('ret.xlsx')
# data_df.to_excel(writer, 'page_1', index=False)
# writer.save()