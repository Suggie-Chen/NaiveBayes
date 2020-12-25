import os

'''path这里改成data文件夹的位置'''
path='C:\\Users\92994\Desktop\sy2\clean_data2.1'
total_dict=set()

'''索引每一类路径'''
for file in os.listdir(path):
    type=file
    file_path = path+'/'+file

    if os.path.isdir(file_path):
        i = 1
        sp=[]
        f=open(file_path+'/dict.txt','r')
        print(type+'\tdict.txt')
        p = f.readlines()
        for each in p:
            total_dict.add(each.split()[0])
        f.close()

'''将每一类的dict合并为total_dict'''
f=open(path+'/total_dict.txt','w')
for word in total_dict:
    f.write(word + '\n')
f.close()