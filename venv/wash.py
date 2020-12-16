import os
NUM=5000
def wash_all_file(rootpath):

    def wash_file(path, type):
        files = os.listdir(path)
        i = 1
        for file in files:
            try:
                used_name = path + '\\' + file
                ## 因为文件名里面包含了文件的后缀，所以重命名的时候要加上
                new_name = path + '\\' + type + str(i) + '.' + file.split('.')[1]
            except:
                ## 跳过一些系统隐藏文档
                pass
            if i <= NUM:
                os.rename(used_name, new_name)
            else:
                os.remove(used_name)
            i += 1

    contents=os.listdir(rootpath)#电脑、烦恼、健康。。。。
    # print("contents=",contents)
    for each in contents:#each是电脑、烦恼、健康等某一类
        if  os.path.isdir(rootpath+'\\'+each):  # 判断是文件夹，打开
            types=os.listdir(rootpath+'\\'+each)
            for type in types:#type是test或train
                if os.path.isdir(rootpath+'\\'+each+'\\'+type):
                    # articles=os.listdir(type)
                    wash_file(rootpath+'\\'+each+'\\'+type,type)

if __name__ == '__main__':
    wash_all_file("D:\机器学习数据\sy发的数据\clean_data")