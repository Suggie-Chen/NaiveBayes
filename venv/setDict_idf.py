from collections import Counter
import os
import re
import operator
import math
# setDict_idf：在clean_data目录下生成idf.txt，里面的总文档数要根据选的类别数量改一下
# setDict_tfidf_fre：找出每类每个词出现的频率，乘上idf后排序取前n个，在每个类的目录下生成一个dict
# union_words：把每个类里的dict所有的词合到一个总词典total_dict里，放在clean_data目录下
'''path这里改成clean_data文件夹的位置'''
path='C:\\Users\92994\Desktop\sy2\clean_data2.1'
# total_dic={}
tf={}
idf={}

'''索引每一类路径'''
for file in os.listdir(path):
    type=file
    file_path = path+'/'+file
    tf_sum = 0
    tf={}

    if os.path.isdir(file_path):
        i = 1

        # f_idf=open('idf.txt','w')
        file_path+='/train'

        '''进入每一类的train文件夹'''
        for each_file in os.listdir(file_path):
            sp = []
            each_path=file_path+'/'+each_file
            f=open(each_path,'r', encoding='utf-8')
            # print(type+'\t'+each_file)
            rf=f.readlines()

            '''将所有词加入列表sp中'''
            for each in rf:
                sp+=each.split()
            f.close()

            for each in set(sp):
                if each in idf.keys():
                    idf[each] += 1
                else:
                    idf[each] = 1

'''输出'''
f=open(path+'/idf.txt','w')
for (word, count) in idf.items():
    s = '%s %7lf' % (word, math.log(50001/count,10))#50000为总文档数，+1防止log1导致idf=0
    f.write(s + '\n')

f.close()
