# 第一个注释
# 导入模块
import keyword
from operator import truediv
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
    
    
    # 数字类型
    # 1. 整形，Python3中只有int型，没有Long
    num = 1
    print("num的类型是")
