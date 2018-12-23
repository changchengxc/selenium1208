import csv
import os


# 不同的测试用例读不同的文件，所以在公共方法中，需要接受文件名作为参数
def read(filename):
    base_path = os.path.dirname(__file__)
    path = base_path.replace("day5", "data/"+filename)
    # print(path)
    # file = open(path)
    list2 = []
    with open(path) as file:
        data = csv.reader(file)
    #   这时数据中，包含了第一行表头
        i = 0
        for row in data:
            if i == 0:
                pass
            else:
                list2.append(row)
            i = i + 1
    return list2


# read("testdata.csv")
# main语句的作用是什么
# 当其他文件调用该文件时，不会执行多余的代码
if __name__ == '__main__':
    list1 = read("testdata.csv")
    print(list1)
