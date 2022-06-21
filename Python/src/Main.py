# -*- coding: utf-8 -*-

# 第一个注释
# 导入模块
from base64 import encode
import keyword
from operator import truediv
from re import X
# 输出模块的内容
keyword.kwlist # 所有关键字信息

# 定义一个主函数
if __name__ == "__main__": 
    # 第一行代码
    print("第一行代码:\nHello, World")
    
    '''
    多行注释1
    多行注释2
    '''
    
    """
    多行注释3
    多行注释4
    """
    
    # 条件语句与缩进
    '''
        对于Python3来说无需使用大括号来定义代码块，
        只需要使用缩进即可，相同缩进默认处于同一代码块
    '''
    done = True
    if (done):
        print("doing")
        print("done...")
    else:
        print("not done...")
        # 缩进一致会导致错误
      # print("error...")
    print("------------------------------\n\n")
    #----------------
    
    # 数字类型
    # 1. 整形，Python3中只有int型，没有Long
    # 普通10进制整形
    num = 1
    print("num的类型是", type(num))
    
    # 可以使用_对整形进行分割，这里只是为了提升可读性
    num = 10_000_000
    print("num的数值是", num)
    
    # 2. 16进制数
    num = 0x1234
    print("num(16)的值是", num)
    #------------------
    
    # 字符串
    # 1. 单行字符串
    str = "这是一个单行字符串"
    
    # 2. 多行字符串
    str = """这
    是
    一
    个
    多
    行
    字
    符
    串
    """
    
    # 3. 字符串转义
    str = "Hello, world!\n"
    print(str)
    # 4. 不需要转义
    str = r"Hello, world!\n"
    # 5. 表示'\'
    str = "Hello, world!\\n"
    print(str)
    
    # 6. 字符串格式化
    print("""
          第一个参数：%d,
          第二个参数：%f,
          第三个参数：%s
          """ %(1, 2.0, "三"))
    # 7. ord获取字符的整数表现形式
    ascii = 'A'
    print(ord(ascii))
    
    # 8. chr获取对应ASCII编码的字符
    ascii = 66
    print(chr(ascii))
    
    # 9. 对字符串进行编码
    str = "hello world"
    print("字符编码：ASCII", str.encode("ascii"))  # ascii只能对英文进行编码
    str = "中文"
    print("字符编码：UTF-8", str.encode("utf-8"))  # 编码中文需要支持中文的字符集
    
    # 10. 对字符串进行解码
    str = b'hello world'
    print("字符解码：ASCII", str.decode("ascii"))
    str = b'\xe4\xb8\xad\xe6\x96\x87'
    print("字符解码：UTF-8", str.decode("utf-8"))
    
    # 11. 计算字符串长度
    str = "1234567"
    print("字符串\"%s\"长度：%d" %(str, len(str)))
    print("------------------------------\n\n")
    # ------------------------------
    
    # 有序可变列表List
    language = ["java", "kotlin", "python"]             # 定义
    length = len(language)                              # 计算长度
    print("列表元素：", language, "；长度：", length)
    
    # 1. 访问列表元素
    print("从前往后第一个：", language[0])
    print("从后往前第一个：", language[-1])
    
    # 2. 添加元素
    language.append("javascript")
    print("添加后的列表元素：", language)
    
    # 3. 在指定位置插入元素
    language.insert(1, "指定位置添加的元素")
    print("在指定位置添加元素后的列表：", language)
    
    # 4. 删除末尾的元素
    language.pop()
    print("删除末尾后的列表元素：", language)
    
    # 5. 删除指定位置元素
    language.pop(1)
    print("删除第二个元素后的列表元素：", language)
    
    # 6. 二维数组
    language = [["python", "java", "go"], ["kotlin", "groovy", "swift"], "java"]
    len(language) # 长度为3
    len(language[0]) # 长度为3
    print("------------------------------\n\n")
    # ------------------------------
    
    # 有序不可变列表tuple，不可变的元组相对于可变长的列表来说更加安全
    database = ("mysql", "nosql", "mongodb", "sqlite")      # 定义好之后元组内元素不可变
    length = len(database)                                  # 计算长度
    print("元组元素：", database, "长度：", length)
    # 由于元组不可变的属性，因此并无增删改的操作
    # 元组查询
    print("元组内的第一个元素：", database[0])
    print("元组内的最后一个元素：", database[-1])
    
    
    
    
    