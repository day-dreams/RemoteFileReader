#! coding:utf8


"""
    这里是具体的业务逻辑代码
"""

import os
import time
import RemoteFileReader_pb2


class RemoteFileReader(object):
    """
        具体业务类
    """

    def __init__(self, jsonobject):
        self.files = {}  # {logic_name:physical_name}
        for f in jsonobject['server']['files']:
            self.files[f['logic_filename']] = f['physical_filename']

    def check_if_file_exists(self, filename):
        """
            返回一个bool值，表示文件名是否存在
            文件名逻辑存在且物理存在时返回true
        """
        if filename not in self.files.keys():  # 文件逻辑名是否存在
            return RemoteFileReader_pb2.FileStatus(file_exits=False)
        else:  # 文件物理名是否存在
            physical_name = self.files[filename]
            flag = os.path.exists(physical_name)
            return RemoteFileReader_pb2.FileStatus(file_exits=flag)

    def read(self, filename):
        """
            返回一个生成器，用于迭代文件中的每一行
        """
        physical_filename = self.files[filename]
        f = open(physical_filename, 'r')
        while True:
            line = f.readline()
            if line == "":
                return
            yield RemoteFileReader_pb2.FileLine(line=line)

    def get_all_filestatus(self):
        for logicname in self.files.keys():
            exits = os.path.exists(self.files[logicname])
            if not exits:
                yield RemoteFileReader_pb2.FileStatus(file_exits=exits, logic_filename=logicname)
            else:
                last_modified_time = os.stat(self.files[logicname]).st_mtime
                last_modified_time=time.ctime(last_modified_time)
                yield RemoteFileReader_pb2.FileStatus(file_exits=exits, last_modified_time=last_modified_time, logic_filename=logicname)
