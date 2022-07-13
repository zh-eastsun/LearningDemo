# -*- coding: utf-8 -*-

def my_funcation(word):
    print("invoke my funcation：", word)
    return None

# 什么都不做的函数
def my_do_nothing(): 
    # 不带pass的话会报错
    pass

# 参数类型检查
def my_type_check(param): 
    if not isinstance(param, (str, int)):
        raise TypeError("类型错误")
    return param

# 函数参数
# 默认参数指向不变对象
def my_introduce(name="", age=0, origin="china"): 
    print("name =", name)
    print("age =", age)
    print("from =", origin)
    
# 可变长参数
def my_multiparam(*params):
    for param in params:
        print("接收到了参数：", param)