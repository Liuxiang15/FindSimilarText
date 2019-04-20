import jieba
# #先不考虑停用词

sentence1 = '应明确表示各出入口与市政道路标高、交通流线及站点之间关系。应与景观竖向设计一致。主要道路应设计公交车站和出租车泊接停靠站。'
sentence2 = '万达广场/万达茂如采用地下室停车，需沿不同方向主要道路设两个或两个以上车库出入口，以分解交通。不宜在商铺前横向设车道出入口。出入口坡道应双进双出，不得做单车道，且净宽不小于8米宜为9米。'
words1 = jieba.cut(sentence1.strip())
words2 = jieba.cut(sentence2.strip())
for word in words1:
    print(word)
# print(words1)
# print(words2)

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