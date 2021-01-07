#tfidf

import os
import math
import numpy as np

ROOTPATH='C:\\Users\92994\Desktop\sy2\clean_data2.1'
global categories#=  ['健康', '商业', '娱乐', '教育', '文化', '游戏', '烦恼', '生活', '电脑', '社会']#注意不可改变顺序！！！！
global cateCount
global CATENUM#类别总数
global VOCABULARYNUM
global bigDic
global gmatrix
global idfBook;

# 构造所有类别的词典
def form_big_dic():
    global bigDic,categories
    bigDic = dict()
    contents = os.listdir(ROOTPATH)  # 电脑、烦恼、健康。。。。
    categories=[]
    for each in contents:  # each是电脑、烦恼、健康等某一类
        if os.path.isdir(ROOTPATH + '\\' + each):  # 判断是文件夹，打开
            categories.append(each)
            bigDic[each] = read_file(ROOTPATH + '\\' + each + '\\' + 'dict.txt')
    # print(bigDic)
    # print(len(bigDic['电脑']))


#读一个字典向量文件，返回一个字典
def read_file(filepath):
    with open(filepath) as fp:
        content=fp.read();
        book=content.split('\n')
        d=dict();
        for each in book:
            if each:#each不为空
                temp=each.split()
                # print(temp)
                if len(temp)==2:
                    d[temp[0]]=float(temp[1])
                else:
                    d[temp[0]] =0
    return d


def P(word,vj):
    # P(wk|vj)=(nk+1) / (n+|Vocabulary|)
    nk=bigDic[vj].get(word,0)#单词wk出现在Textj中的次数，若没有出现，则为0
    n=cateCount[vj]
    ans=(nk+1) / (n+VOCABULARYNUM)
    return ans

# V为所有类的向量，text为待分类文本string，返回值为分类结果
def Vnb(text,V):
    max=-9999999999999999999999999999999999999
    tans=0
    retu=''
    l=text.split()
    for j in V:#对于每一类
        for word in l:#对弈一篇文本中的每一个单词
            idf=idfBook.get(word,math.log(50000,10))
            # print(idf)
            p=P(word,j)
            tans=tans+math.log(p*idf,10)
        # print("tans=",tans)
        if tans>max:
            max=tans
            retu=j
        tans=0
    # print("j=",retu,"max=",max)
    return retu

def cal_cateCount(categories):
    n=0
    for vj in categories:#each为健康等类别
        for key in bigDic[vj]:
            # print("key=",key)
            n = n + bigDic[vj][key]

        cateCount[vj]=n
        n=0

# 打印混淆矩阵
def print_matrix(matrix):
    print('{:>8}'.format(''), end='')
    for label in range(len(categories)):
        print('{:>7}'.format(categories[label]), end='')
    print('\n')
    for row in range(len(categories)):
        print('{:>8}'.format(categories[row]), end='')
        for col in range(len(categories)):
            print('{:>8}'.format(matrix[row][col][0]), end='')
        print('\n')

def classify_all_texts(rootpath,matrix):
    contents = os.listdir(rootpath)  # 电脑、烦恼、健康。。。。
    print(contents)
    for each in contents:  # each是电脑、烦恼、健康等某一类
        if os.path.isdir(rootpath + '\\' + each):  # 判断是文件夹，打开
            texts = os.listdir(rootpath + '\\' + each + '\\' + 'test')
            for text in texts:
                with open(rootpath + '\\' + each + '\\' + 'test' + '\\' + text, encoding='utf-8') as fp:
                    string = fp.read()
                    vj = Vnb(string, categories)
                    i = categories.index(each)  # 实际值
                    j = categories.index(vj)  # 预测值
                    matrix[i][j][0] += 1
    # print(matrix)
    print_matrix(matrix)

def cal_precision_and_recall(matrix):
    precisionList = []
    recallList = []
    f1List=[]
    for j in range(CATENUM):  # 先对列进行遍历
        sum = 0
        for i in range(CATENUM):
            sum = sum + matrix[i][j][0]

        a = matrix[j][j][0]
        recall = a / 5000
        precision = a / sum
        f1=(2*precision*recall)/(precision+recall)
        precisionList.append(precision)
        recallList.append(recall)
        f1List.append(f1)
        print("类别：", categories[j])
        # print("a:", a)
        # print("sum:", sum)
        print("precision={:.6f} , recall={:.6f},f1={:.6f}".format(precision, recall,f1))

    total_precision = np.mean(precisionList)
    total_recall = np.mean(recallList)
    total_f1=np.mean(f1List)
    print("total_precision={:.6f} , total_recall={:.6f},total_f1={:.6f}".format(total_precision, total_recall,total_f1))


if __name__ == '__main__':
    # 计算十万篇文本的单词总数
    book=read_file(ROOTPATH+'\\'+"total_dict.txt")
    VOCABULARYNUM=len(book)
    # print(book)
    print("VOCABULARY=",VOCABULARYNUM)

    idfBook=read_file(ROOTPATH+'\\'+"idf.txt")
    #构造所有类别的词典
    form_big_dic()

    #计算每一类的位置总数
    cateCount=dict()
    cal_cateCount(categories)
    CATENUM=len(cateCount)
    print(cateCount)

    #对所有文章进行分类
    gmatrix = [[[0] for j in range(CATENUM)] for i in range(CATENUM)]
    classify_all_texts(ROOTPATH,gmatrix)

    #计算准确率和召回率
    cal_precision_and_recall(gmatrix)