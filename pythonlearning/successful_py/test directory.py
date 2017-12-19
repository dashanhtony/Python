import os
rootdir = "D:\git项目"
x = u'统计文件大小.csv'
f = open(os.path.join(rootdir,x), "w+")
list1=[]
list2=[]
for dirname in os.listdir(rootdir):
    Dir = os.path.join(rootdir, dirname)    #路径补齐
    count = 0
    if (os.path.isdir(Dir)):           #判断是否为目录
        for r, ds, files in os.walk(Dir): #遍历目录下所有文件根，目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath,
            # dirnames, filenames)【文件夹路径, 文件夹名字, 文件名称】
            for file in files:      #遍历所有文件
                size = os.path.getsize(os.path.join(r, file)) #获取文件大小
                count += size/1024/1024
                size=float('%.2f' % count)#大小转换成MB
        tuple1=(dirname,size)#将文件夹名字和大小配对成元组
        list1.append(tuple1)
    else:
        continue
list1=sorted(list1, key=lambda b:b[1], reverse=True)#对list按照每个key元组的第二个值即文件大小从大到小排序
func1=lambda a:str(a[1])+'MB'
func2=lambda a:os.path.join(rootdir,a)
for key in list1:
    list2.append((key[0],func1(key))) #对每个大小值加上MB单位
for key in list2:
    dirname=func2(key[0]) #对每个文件夹加上具体路径
    print(dirname +'\t\t' + key[1])
    f.write(dirname +','+ key[1])
f.close()