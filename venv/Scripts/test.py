from libsvm.commonutil import *
from libsvm.svm import *
from libsvm.svmutil import *


file_path = r'E:\大三\课件和code\人工智能原理\实验\小组实验资料'  # 存放数据文件夹的父目录
label_list = ['电脑', '烦恼', '健康', '教育', '商业', '社会', '生活', '文化', '游戏', '娱乐']


# 打印混淆矩阵
def print_matrix(matrix):
    print('{:>8}'.format(''), end='')
    for label in range(10):
        print('{:>8}'.format(label_list[label]), end='')
    print('\n')
    for row in range(10):
        print('{:>8}'.format(label_list[row]), end='')
        for col in range(10):
            print('{:>8}'.format(matrix[row][col]), end='')
        print('\n')


# 输出预测结果，每类和总的的准去率、召回率，f-score
def test_result(label):   # label为列表
    matrix = [[0 for i in range(10)] for i in range(10)]  # 10*10二维矩阵
    predict_list = []
    for i in range(10):
        predict_list.append(label[i*5000:i*5000+5000])
    for col in range(10):
        matrix[0][col] = predict_list[col].count(1.0)
        matrix[1][col] = predict_list[col].count(2.0)
        matrix[2][col] = predict_list[col].count(3.0)
        matrix[3][col] = predict_list[col].count(4.0)
        matrix[4][col] = predict_list[col].count(5.0)
        matrix[5][col] = predict_list[col].count(6.0)
        matrix[6][col] = predict_list[col].count(7.0)
        matrix[7][col] = predict_list[col].count(8.0)
        matrix[8][col] = predict_list[col].count(9.0)
        matrix[9][col] = predict_list[col].count(10.0)
    print_matrix(matrix)

    # 每一行每一列的和
    row_sum = []
    col_sum = []
    for i in range(10):
        row_sum_temp = 0
        col_sum_temp = 0
        for j in range(10):
            row_sum_temp += matrix[i][j]
            col_sum_temp += matrix[j][i]
        row_sum.append(row_sum_temp)
        col_sum.append(col_sum_temp)

    # 计算每一类以及总的的准确率precision和召回率recall
    precision_list = []
    recall_list = []
    total_precision = 0
    total_recall = 0
    for kind in range(10):
        precision_list.append(matrix[kind][kind] / row_sum[kind])
        recall_list.append(matrix[kind][kind] / col_sum[kind])
        total_precision += precision_list[kind]
        total_recall += recall_list[kind]
    total_precision /= 10
    total_recall /= 10

    # 输出准确率precision和召回率recall
    for kind in range(10):
        print(label_list[kind]+":")
        print("precision={},recall={}".format(precision_list[kind], recall_list[kind]))
        print("f-score={}".format(2*precision_list[kind]*recall_list[kind] / (precision_list[kind]+recall_list[kind])))
    print("total_precision={},total_recall={}".format(total_precision, total_recall))
    print("total_f-score={}".format(2*total_precision*total_recall / (total_precision+total_recall)))


# 测试分类器并输出分类结果
def main():
    y, x = svm_read_problem(file_path+r'\testFilecipin.txt')
    m = svm_load_model('libsvm.model')  # model为train.py生成的文件，放在当前python文件同录下
    [lable, acc, val] = svm_predict(y, x, m)   # lable返回一个列表，包含预测的类别
    test_result(lable)


if __name__ == '__main__':
    main()



