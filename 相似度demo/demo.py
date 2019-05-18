import jieba
jieba.set_dictionary("./dict.txt")  #指定dict.txt加载路径，为了方便部署，使用相对路径。
jieba.initialize()                  #jieba库初始化。
# jieba.load_userdict("special_words.txt")
import sys
#注释：python3没有has_key

def stop_words_list(filepath):
    with open(filepath,'r',encoding='utf-8') as file:
        stop_words = [line.strip() for line in file.readlines()]
        # for line in stop_words:
        #     if "#" not in line:
        #         print(line)
        #     else:
        #         break
        return stop_words

def get_words_freq(stop_words, sentence1, sentence2):
    #参数：两个文本字符串
    #返回结果：所有词语出现的次数(分别用字典的形式存储)
    #待调参数：var_len = 0.2  var_sim = 0.1设定两个文本的长度相差较长者的var_len以上时相似度为var_sim
    words1= []
    words2= []
    try:
        words1 = jieba.cut(sentence1.strip())
        # print(words1)
        words1 = [word for word in words1]
        # print(words1)
        words2 = jieba.cut(sentence2.strip())
        # print(words2)
        words2 = [word for word in words2]
        # print(words2)
    except:
        print(sentence1)
        print(sentence2)
        print("jieba分词出错,程序退出！！！")
        return -1

    max_len = max(len(words1), len(words2))
    var_len = 0.2
    var_sim = 0.1
    # if abs(len(words1) - len(words2)) > var_len:
    #     return var_sim
    if abs(len(words1) - len(words2)) > int(max_len*var_len):
        return var_sim

    #因为输入源的不规范，所以特殊处理
    spe_words = ['审查内容', '修改设计', '审查合格', '一般规定','总体要求']
    for word in spe_words:
        if word in sentence1 or word in sentence2:
            return 0

    #分词之后要进行停用词去除
    for word in words1:
        if word in stop_words:
            words1.remove(word)
    for word in words2:
        if word in stop_words:
            words2.remove(word)
    print("文本1去除停用词后的分词结果是：")
    print(words1)
    print("文本2去除停用词后的分词结果是：")
    print(words2)

    comman_words = set(words1).intersection(set(words2))
    print("文本1和文本2共同的分词结果是：")
    print(comman_words)

    
    word1_freq_dict = cal_fre(words1)
    word2_freq_dict = cal_fre(words2)
    word1_freq_dict, word2_freq_dict = merge_dict_array(word1_freq_dict, word2_freq_dict)
    # print("word1_freq_dict是：----------------------------")
    # print(word1_freq_dict)
    # print("word2_freq_dict是：-----------------------------")
    # print(word2_freq_dict)
    sim = cal_sim(word1_freq_dict, word2_freq_dict)
    lower_bound = 0.7
    upper_bound = 0.99
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
    print("文本1的词向量是：")
    print(vector1)
    print("文本1的词向量是：")
    print(vector2)
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

def run():
    if len(sys.argv) < 3:
        print("exe后应该有两个空格分开的txt文件名!!!")
        return
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    f1 = open(filename1)               # 返回一个文件对象   
    line1 = f1.readline()               # 调用文件的 readline()方法 
    # print(line1)
    f2 = open(filename2)               # 返回一个文件对象   
    line2 = f2.readline()               # 调用文件的 readline()方法 
    # print(line2)
    stop_words = stop_words_list('stop_words.txt')
    sim = get_words_freq(stop_words,line1, line2)
    print("两个文本的相似度是：%.4f"%(sim))
    


run()

        












