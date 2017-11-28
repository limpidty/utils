# -*-coding:utf-8-*-
import os


def scan_dir(path):
    os.chdir(path)  # 改变工作路径为path
    # 获取当前的目录
    for obj in os.listdir(os.curdir):
        # 若为文件则执行操作
        if os.path.isfile(obj):
            pass  # 执行所需操作
        if os.path.isdir(obj):
            scan_dir(obj)
            os.chdir(os.pardir)  # 返回上一级目录
