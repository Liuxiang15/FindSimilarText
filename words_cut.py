import jieba

jieba.load_userdict("TsinghuaDict.txt")

class wordsCut:
    #创建停用词表
    @classmethod
    def stop_words_list(cls,filepath):
        with open(filepath,'r',encoding='utf-8') as file:
            stop_words = [line.strip() for line in file.readlines()]
            return stop_words

    #对搜索语句进行中文分词
    @classmethod
    def sentence_seg(cls,query):
        query_seg = jieba.cut(query.strip())
        stop_words = cls.stop_words_list('stop_words.txt')
        keywords = []
        for word in query_seg:
            if word not in stop_words and word != '\t':
                keywords.append(word)
        return keywords
