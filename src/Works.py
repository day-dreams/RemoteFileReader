#! coding:utf8


"""
    这里是具体的业务逻辑代码
"""

import os

class RemoteFileReader(object):
    @staticmethod
    def check_if_file_exists(filename):
        """
            返回一个bool值，表示文件是否存在
        """
        return os.path.exists(filename)

    @staticmethod
    def read(filename):
        """
            返回一个生成器，用于迭代文件中的每一行
        """
        f=open(filename,'r')
        while True:
            line=f.readline()
            if line=="":
                return
            yield line
