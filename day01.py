# print("my name is %s,my age is %d"%("zhuang",32))
# a = "zhuang12"
# b = 121
# print("my name is {0},my age is {0}".format("zhuang",12))
# a = 1
# while a <= 10:
#     print(a)
#     a+=1
#
# else:
#     print("bbbbb")
#
# for i in range(1,10):
#     print(i)
# else:
#     print("dd")
#
# print(dir("print"))


# a = "wedddd d"
# print(a[:5])
# print(a.capitalize())
# print(a.upper())
# print(a.upper())
# print(a.lower())
# print(a.swapcase())
# print(a.title())
# print(a.center(12, "d"))
# print(a.startswith("w",1,4))
# print(a.endswith("d"))
# print(a.find("dddd",))
# print(a.index("w", 1, 4))

# print(a.strip("we"))
# print(a.split("e"))
# print(a.count("d",))
# print(a.replace("d","f",))

# lis = ["a", 44, 3, 23, 65, 4, "dd"]
# lis.append("ff")
# lis.insert(2, "d", )
#
# lis.extend("mmmdd")
# print(lis)
# lis.pop()
# # lis.pop(22)
# lis.remove("d")
# print(lis)
# lis[1:4] = ("1", "2", "3")
# print(lis)
#
# print(lis.index("1"))
#
# a = "dddddd12"
# b = list(a)
# print(b.sort())
# print(b)
#

# lis = ["a", "dd", "ff"]
# s = "".join(lis)
# print(s)

# dic = {1:"dd", 2:"ff", 3:"gg"}
# dic[4] = "fd"
# dic.setdefault(5, "we")
# dic.pop(9, "d")
#
# dic.popitem()
# print(dic)
# del dic[4]
# print(dic)

# print(dic.keys())
# print(type(dic.values()))
# print(list(dic.items()))
# for k, v in dic.items():
#     print(k, v)

# lis = ["a", "dd", "ff"]
# dic = {1:"dd", 2:"ff", 3:"gg"}
# dd = dic.fromkeys(lis, "ff")
# print(dd, dic)

# s = {1, 2, "dd" , "ff","dg"}
# print(s)
# # s.add("gds")
# s.update("dfsg")
# # s.pop()
# print(s)
# for i in s:
#     print(i)

# s = "dfsd"
# print(s.encode("utf-32"))
# print(b'\xff\xfed\x00f\x00s\x00d\x00'.decode("utf-16"))


# f = open("./a.txt", mode="r+", encoding="utf-8")
# f.read()
# f.write("dfs")
# f.seek(0)
# print(f.read())
# for i in f:
#     print(i)

# with open("./a.txt", mode="r+", encoding="utf-8") as f1, \
#     open("./b.txt",mode="a",encoding="utf-8") as f2:
#     for i in f1:
#         s = i.replace("d", "g")
#         f2.write(s)
#         print(s)

# def func(name, age, *args, clas="4", **kwargs):
#     print(" my name is {},my age is {}".format(name, age))
#     print(clas)
#     print(list(args).append(5))
#     print(kwargs)
#
#

# def func(*args):
#     print(args)
# lis="asd"
# func(*lis)

# lis1 = [1, 2, 3, 4]
# dic = {"ff": "ff", "dd": "dd"}
# func("zhuang", "aa", lis1, clas="5", **dic)

# a = 12


# def outer(name):
#     def func():
#         print(func.__closure__)
#     return func
#
# outer("zhuang")()

# func = lambda k:k+1
# print(func(1))

# dic = {1: 1, 2: 2, 3: 4, 4: 0}
# print(max(dic, key=lambda k: dic[k]))

# def find(l,aim,start = 0,end = None):
#     end = len(l) if end is None else end
#     mid_index = (end - start)//2 + start
#     if start <= end:
#         if l[mid_index] < aim:
#             return find(l,aim,start =mid_index+1,end=end)
#         elif l[mid_index] > aim:
#             return find(l, aim, start=start, end=mid_index-1)
#         else:
#             return mid_index
#     else:
#         return '找不到这个值'
# lis = [1,2,3,4,5,6,44,53,34]
# s = find(l =lis, aim=5)
# print(s)

#
# with open("./a.txt",mode="r+",encoding="utf-8") as f1:
#     print(f1.__next__())
#     print(f1.__next__())
#
#
# lis = [1,2,3,4]
# it = lis.__iter__()
# while True:
#     try:
#         print(it.__next__())
#     except StopIteration:
#         break

# lis1 = [1, 2, 3, 4]
# g = [i for i in lis1 ]
# print(dir(g))
# g.__iter__()

# def genterd():
#     print(1)
#     a = yield
#     print(a)
#     print(2)
#     b = yield
#     print(b)
#     yield
#
# ret = genterd()
# ret.__next__()
# s = ret.send("dd")
# ret.send("ff")

# ret = [i for i in range(10) if i<=5]
# print(ret)

# from functools import wraps
# def wrapper(a):
#     def outer(func):
#         @wraps(func)
#         def inner(*args,**kwargs):
#             if a == 1:
#                 print("inner qian")
#                 ret = func(*args,**kwargs)
#                 print("inner hou")
#                 return ret
#             else:
#                 pass
#         return inner
#     return outer
#
#
# @wrapper(2)
# def func():
#     print("func")
#
# func()
#
# print(locals())
# print(globals())
# print(eval("[1,2,3,4]"))
# __import__("time")
#
# print(bytes("asdf", "utf-32"))
# print("asdf".encode("utf-32"))

# a = "abcd"
# b = [1,2,3,4,5]
# print(list(zip(a, b)))
# for i in zip(a,b):
#     print(i)
#
# print(list(filter(lambda k:k>2 , b)))
# for i in filter(lambda k:k>2 , b):
#     print(i)
#
# print(list(map(lambda k: k > 2, b)))
#
# print(sorted(a,key=  lambda k:k,reverse= False))


# c = 20
# d = [1, 2, 4, 5]
# class Person():
#     a = 50
#     d.append(5)
#     b = [1, 2, 3, 4]
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
#
#     def method1(self):
#         print(c)
#         print(self.name)
#
#     def method2(self):
#         print(self.age)
#
#     @classmethod
#     def method3(cls):
#         print(cls.a)
#
# Person.a = 20
# p1 = Person("zhuang", 23)
# p1.b.append(6)
# p1.method1()
# p2 = Person("jin", 20)
# print(p1.b, p2.b,Person.b)
#
#
# print(Person.d)


# class Person():
#
#     def __init__(self, name, age):
#
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         print("{} will walk".format(self.name))
#
#     def drink(self):
#         print("{} will drink".format(self.name))
#
#
# class Man(Person):
#
#     def walk(self):
#         super().walk()
#         print("in walk")
#
# m = Man("zhuang", 23)
# m.walk()
# print(Man.mro())


# from abc import abstractmethod,ABCMeta
# class Person(metaclass=ABCMeta):
#
#     @abstractmethod
#     def walk(self):
#         pass
#
# class Man(Person):
#     def walk(self):
#         pass
#
# m = Man()


# from abc import abstractclassmethod,ABCMeta,abstractmethod   #利用abc模块实现抽象类
#
# class Animal(metaclass=ABCMeta):  # 类似接口，只定义规范，不实现具体的代码
#     @abstractmethod
#     def run(self):
#         pass
#
#     @abstractclassmethod
#     def eat(self):
#         pass
#
#
# class People(Animal):
#     b = 20
#     @classmethod
#     def run(cls):  # 不符合规范，不允许实例化
#         print(cls.b)
#         print('people is walking')
#
#     @classmethod
#     def eat(cls):
#         print('people is eating')

# class Pig(Animal):
#     def run(self):
#         print('Pig is running')
#
#     def eat(self):
#         print('Pig is eating')
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is zouing')
#
#     def eat(self):
#         print('Dog is eating')

# peo1 = People()
#
#
# People.run()


# class Person():
#     a = 12
#     __b = [1, 2, 3, 4]
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def walk(self):
#         print(self.name, self.__age)
#
#     @classmethod
#     def eat(cls):
#         print(cls.a, cls.__b)
#
#     @staticmethod
#     def run():
#         pass
#
#     @property
#     def fei(self):
#         pass
#
# p1 = Person("zhuang", 20)
# p1.walk()
# p1.eat()


# class Person():
#
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def walk(self):
#         return self.name
#
#     @walk.setter
#     def walk(self, value):
#         self.name = value
#         print(self.name)
#
#     @walk.deleter
#     def walk(self):
#         print("dddd")
#         del self.name
#
# p1 = Person("zhuang")
# print(p1.walk)
# p1.walk = 20
# del p1.walk
#
# class B():
#     def f1(self):
#         print('from B')
#
# class A():
#     def f1(self):
#         print('from A')
#
#
#
# class C(A,B):
#     def f1(self):
#         print('from c')
#         super().f1()
#
# print(C.mro())
#
# C().f1()

# class Person():
#     age = 20
#     def __init__(self, name):
#         self.name = name
#
# class Man(Person):
#
#     def walk(self):
#         print("walk")
#
# p = Person("zhuang")
# m = Man("jin")
#
# print(isinstance(p, Person))
# print(issubclass(Man ,Person))
#
# s = getattr(p, "__init__")
# s("zhuang")
# print(getattr(Person, "age"))


# class Person():
#     b = 10
#     _a = False
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if not cls._a:
#             cls._a = object.__new__(cls)
#         return cls._a

# import sys
# print(sys.path)
#
# name = "帅哥"
# age = 12
# print(f"my name is {name},age is {age}")


# print(time.time())
# print(time.ctime())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# a = time.time()
# print(time.localtime(a))
# s = time.localtime(a)
# print(time.strftime("%Y-%m-%d %H:%M:%S",s))
# time.strftime("%Y-%m-%d %H:%M:%S")

# import random
#
# print(random.random())
# print(random.randint(1,30))

# import os
# print(__file__)
# print(os.getcwd())
#


# import time
# import threading
#
#
# def test_thread(para='hi', sleep=3):
#     """线程运行函数"""
#     time.sleep(sleep)
#     print(para)
#
#
# class Mythread(threading.Thread):
#     def __init__(self, func, args, name=""):
#         super().__init__()
#         self.func = func
#         self.args = args
#         self.name = name
#
#     def run(self):
#         self.func(*self.args)
# #
# # def main():
# #     # 创建线程
# #     thread_hi = Mythread(test_thread, ("he", 2), test_thread(__name__))
# #     thread_hello = Mythread(test_thread, ('hel', 1), test_thread(__name__))
# #     # 启动线程
# #     thread_hi.start()
# #     thread_hello.start()
# #
# #     print('Main thread has ended!')
#
# def main():
#     # 创建线程
#     thread_hi = threading.Thread(target=test_thread, args=("hi", 2))
#     thread_hello = threading.Thread(target=test_thread, args=('hello', 1))
#     # 启动线程
#     thread_hi.start()
#     thread_hello.start()
#
#     print('Main thread has ended!')
#
# main()



# import configparser
# config = configparser.ConfigParser()
# config["zhuang"] = {"1": 2, "jin": 3, "po": 4, "55": 4}
# with open("example.ini", "w", encoding="utf-8") as f1:
#     config.write(f1)

# import logging
#
# logger = logging.getLogger()
# fh = logging.FileHandler('log.log',encoding='utf-8')
# sh = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
#
# fh.setFormatter(formatter)
# sh.setFormatter(formatter2)
# logger.addHandler(fh)
# logger.addHandler(sh)
# logging.debug('debug message')       # 低级别的 # 排错信息
# logging.info('info message')


# import logging
# logger = logging.getLogger()
# fh = logging.FileHandler('log.log',encoding='utf-8')
# sh = logging.StreamHandler()    # 创建一个屏幕控制对象
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
# # 文件操作符 和 格式关联
# fh.setFormatter(formatter)
# sh.setFormatter(formatter2)
# # logger 对象 和 文件操作符 关联
# logger.addHandler(fh)
# logger.addHandler(sh)
# logging.debug('debug message')       # 低级别的 # 排错信息
# logging.info('info message')            # 正常信息
# logging.warning('警告错误')      # 警告信息
# logging.error('error message')
#
# import os
#
# print(os.path.abspath(os.path.dirname(os.path.realpath(__file__))))


# import  requests
#
# re = requests.get("http://www.baidu.com")
# print(re.status_code)
# re.encoding = "utf-8"
# print(re.text)
# print(re.cookies)


import openpyxl


wb = openpyxl.open("dd.xlsx")
ws = wb.active
d = ws.cell(1, 1)
d = ws["A1"]
print(d.value)


