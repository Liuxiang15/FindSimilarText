# import pandas as pd
# import numpy as np
# from numpy import *
# writer = pd.ExcelWriter(r'demo1.xlsx')
# files=['1-商业项目施工图审查要点-建筑.xlsx', '10-商业项目施工图审查要点-幕墙.xlsx', '11-商业项目施工图审查要点-导向标识.xlsx', '12-商业项目施工图审查要点-夜景照明.xlsx', '2-商业项目施工图审查要点-结构.xlsx', 
# '3-施工图设计质量管控标准-给排水.xlsx', '4-施工图设计质量管控标准-暖通.xlsx', '5-施工图设计质量管控标准-电气.xlsx', '6-施工图设计质量管控标准-弱电.xlsx', '7-商业项目施工图审查要点-内装.xlsx', '8-商业项目施工图审查要点-景观.xlsx', 
# '9-施工图设计质量管控标准-室外管线.xlsx']
# data = {}
# data["文件名"] = array(files)
# data_list = ["----------------"]*12
# for file in files:
#     data[file] = array(data_list)
# '''创建数据框1'''
# # df1 = pd.DataFrame({'V1':np.random.rand(3),
# #                     'V2 ':np.random.rand(3),
# #                     'V3':np.random.rand(3)})
# df1 = pd.DataFrame(data)
# df1.to_excel(writer,sheet_name='sheet1',index=False)

# # '''创建数据框2'''
# # df2 = pd.DataFrame({'V1':np.random.rand(3),
# #                     'V2 ':np.random.rand(3),
# #                     'V3':np.random.rand(3)})
# # df2.to_excel(writer,sheet_name='sheet2',index=False)

# # '''创建数据框3'''
# # df3 = pd.DataFrame({'V1':np.random.rand(3),
# #                     'V2 ':np.random.rand(3),
# #                     'V3':np.random.rand(3)})
# # df3.to_excel(writer,sheet_name='sheet3',index=False)

# '''数据写出到excel文件中'''
# writer.save()
# # sim = 67.34235
# # a = "(相似率%.3f)"%(round(sim, 3))
# # print(a)
# # print(str(a))
# # a=['1-商业项目施工图审查要点-建筑.xlsx', '10-商业项目施工图审查要点-幕墙.xlsx', '11-商业项目施工图审查要点-导向标识.xlsx', '12-商业项目施工图审查要点-夜景照明.xlsx', '2-商业项目施工图审查要点-结构.xlsx', 
# # '3-施工图设计质量管控标准-给排水.xlsx', '4-施工图设计质量管控标准-暖通.xlsx', '5-施工图设计质量管控标准-电气.xlsx', '6-施工图设计质量管控标准-弱电.xlsx', '7-商业项目施工图审查要点-内装.xlsx', '8-商业项目施工图审查要点-景观.xlsx', 
# # '9-施工图设计质量管控标准-室外管线.xlsx']
# # ['总体设计审查要点/1-商业项目施工图审查要点-建筑.xlsx', '总体设计审查要点/10-商业项目施工图审查要点-幕墙.xlsx', '总体设计审查要点/11-商业项目施工图审查要点-导向标识.xlsx', '总体设计审查要点/12-商业项目施工图审查要点-夜景照明.xlsx', '总体设计审查要点/2-商业项目施工图审查要点-结构.xlsx', '总体设计审查要点/3-施工图设计质量管
# # 控标准-给排水.xlsx', '总体设计审查要点/4-施工图设计质量管控标准-暖通.xlsx', '总体设计审查要点/5-施工图设计质量管控标准-电气.xlsx', '总体设计审查要点/6-施工图设计
# # 质量管控标准-弱电.xlsx', '总体设计审查要点/7-商业项目施工图审查要点-内装.xlsx', '总体设计审查要点/8-商业项目施工图审查要点-景观.xlsx', '总体设计审查要点/9-施工图
# # 设计质量管控标准-室外管线.xlsx']

file_num = 5
data_list = [[""]*file_num]*file_num
print
for i in range(len(data_list)):
    data_list[i] = ["---"]*file_num
    
print(data_list)
data_list[2][3] = "fffffffffffff"
print(data_list)