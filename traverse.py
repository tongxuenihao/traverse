#!/usr/bin/env python
# coding=utf-8

#使用os.walk()


import os
def traverse(path):
    files=[]
    for filepath,dirnames,filenames in os.walk(path):
        for dir in dirnames:
            files.append(os.path.join(filepath,dir))
        for file in filenames:
            files.append(os.path.join(filepath,file))
        return files


if __name__ == '__main__':
    path = '/root/python_study'
    files=traverse(path)
    for file in files:
        print(file)


