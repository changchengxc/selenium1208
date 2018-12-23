# 1.导入读取csv文件的代码库
import csv
import os


def read(filename):
    # os.path.dirname(__file__) 的意思是，获取当前代码文件的目录
    base_path = os.path.dirname(__file__)
    print(base_path)
    # path = base_path - day4 + data/testdata.csv
    path = base_path.replace("day4","data/" + filename)
    print(path)
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

# 加上main语句表明，下面两行代码只有在当前文件运行时，才会执行
# 在别的文件，引用read()方法时，下面两行代码不执行
if __name__ == '__main__':
    # 一个项目中，可能有多个测试用例都需要读csv文件，每个测试用例，对应不同的csv文件
    # 但是我们这个read方法现在只能读取testdata.csv文件，
    # 我们需要接受一个文件名，根据不同的文件名找不同的文件
    list = read("testdata2.csv")
    print(list)
