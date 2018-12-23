# 1.导入读取csv文件的代码库
import csv
import os


def read():
    # 2.确定文件的位置
    # 字母r表示忽略路径中所有的转义斜杠
    # path = r"C:\Users\51Testing\Desktop\testdata.csv"、
    # path = r"C:\Users\51Testing\PycharmProjects\selenium1208\data\testdata.csv"
    # os是操作系统的意思，path是路径的意思，dir是文件夹，是directory的缩写
    # __file__是当前代码文件的意思
    # 合起来的意思就是：当前代码文件的目录
    base_path = os.path.dirname(__file__)
    print(base_path)
    path = r"C:\Users\51Testing\PycharmProjects\selenium1208\data\testdata.csv"
    print(path)
    # 3.通过代码打开csv文件
    # file = open(path)
    with open(path) as file:    # with....as....可以在file打开以后，当不再使用时，自动关闭文件
        # file.close()
        # 4.读取csv文件中数据
        data = csv.reader(file)
        # 5.遍历数据表格，以一行一行方式展现
        # for row in data:
        #     print(row)
        list = []    # 声明一个空列表，然后往里填充除了一行以外的其他数据
        i=0 # 为for循环准备一个计数器，从0开始，表示第一行
        for row in data:
            if i == 0:
                pass    # 如果是第一行数据，我们什么也不做
            else:
                list.append(row)
            i=i+1
    return list     # 最后list和data的区别就是少了第一行数据
# 很多测试数据都需要读取csv文件，那么就应该把这段读取csv的代码单独封装成一个方法，避免每次重新读取csv文件都重新写一遍这段代码

#想想一下新的情景，在公司里面，一个项目的测试用例，一般会分给不同的人完成
# 我们应该把csv文件放在我们的项目中