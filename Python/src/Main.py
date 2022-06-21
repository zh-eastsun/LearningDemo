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
    print(str.encode("ascii"))  # ascii只能对英文进行编码
    str = "中文"
    print(str.encode("utf-8"))  # 编码中文需要支持中文的字符集
