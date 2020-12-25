import os
from collections import Counter

'''此处改成clean_data的位置'''
path='C:\\Users\92994\Desktop\sy2\clean_data2.1'
idf={}

f=open(path+'\idf.txt','r')
p = f.readlines()
for each in p:
    idf[each.split()[0]]=float(each.split()[1])
f.close()

'''索引每一类路径'''
for file in os.listdir(path):
    type=file
    file_path = path+'/'+file
    tf={}

    if os.path.isdir(file_path):
        i = 1
        sp=[]
        f_dict = open(file_path + '/dict.txt', 'w')
        file_path+='/train'

        '''进入每一类的train文件夹'''
        for each_file in os.listdir(file_path):
            each_path=file_path+'/'+each_file
            f=open(each_path,'r', encoding='utf-8')
            print(type+'\t'+each_file)
            rf=f.read()

            '''将所有词加入列表sp中'''
            sp = [one for one in rf.split()]
            f.close()

            for each in sp:
                if each in tf.keys():
                    tf[each] += 1
                else:
                    tf[each] = 1

        '''找出前2000,根据tfidf降维'''
        tf=dict((sorted(tf.items(), key = lambda kv:((kv[1]*idf[kv[0]]), kv[0]),reverse=True))[0:2000])

        '''写单类dict，输出单词 词频'''
        for (word,fre) in tf.items():
            s='%s %7d'%(word,fre)
            f_dict.write(s+'\n')

        f_dict.close()
