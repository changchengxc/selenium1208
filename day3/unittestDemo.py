import unittest
# unittest是python内置的代码库，不需要下载
# 最常用代码库，会在python sdk中准备好，不需要通过第三方下载
# 说明unittest比selenium更常用，更重要

# 类名最好和文件名之间，只差一个首字母的大小写问题，类名首字母大写，文件名首字母小写
# python中用小括号表示继承
# 让我们自己的类，继承unittest代码库中的TestCase类，表示当前类也是一个测试用例类
# 1.继承unittest代码库中的TestCase类
class UnittestDemo(unittest.TestCase):
    # 2.重写父类的方法：setUp和tearDown
    # setUp方法是一个钩子方法，不需要调用，自动执行，在什么条件下自动执行呢？
    # 在测试用例正式开始之前，首先自动执行setUp方法，类似于手工测试中的预置条件

    # 在python中，遇到冒号，下一行，必定要缩进4个空格
    def setUp(self):
        print(1)

    # tearDown也是一个钩子方法,不需要调用,自动执行,在什么条件下执行呢?
    # 在测试用例执行完毕以后,自动执行tearDown方法,一般用于做测试环境工作
    def tearDown(self):
        print(2)


    def test_login(self):
        # 如何调用类中的其他方法
        # self英文是自己的意思
        # 在这里，self代表类本身
        self.login()

    # 在unittest中,如果一个方法名以test开头,说明这是一个测试用例访法,
    # 测试用例方法也是不需要调用,可以直接执行
    def test_z(self):
        print(3)

    #考虑一下,说在selenium中,setUp和tearDown都写什么代码呀?
    # setUp里面可能会写打开浏览器，以浏览器的一些设置
    # tearDown里面可能会写关闭浏览器

# 只有test开头的方法，才是测试用例方法
    def login(self):
        print(4)

        # 如果光标在一个测试方法之内，那么只运行一个测试方法
        # 如果光变在所有测试方法之外，那么就运行所有测试方法
        # 在同一个类中，方法的执行顺序，取决于方法名的字母顺序

# 方法的重写，说明父类中已经存在了同名方法
# 所以，要想重写父类的方法，需要查看源代码

    @classmethod
    def setUpClass(cls):
        "在类中所有的测试用例执行之前，setUpClass方法会首先执行一次"
        print(5)

    @classmethod
    def tearDownClass(cls):
        "在类中所有的测试用例方法执行之后，tearDownCLass方法会执行一次"
        print(6)

    # setUp和setUpClass可以都有，也可以只有一个，取决于以后的，具体的测试用例

