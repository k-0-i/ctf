"""
-*- coding: utf-8 -*-
@Time    : 2023/9/20 21:05
@Author  : St4rry
@File    : web195.py
@Software: PyCharm
 """

import argparse
import string
import zipfile
import zlib
from itertools import product


# 获取文件的crc32的值
def getCRC(filename):
    is_zip = zipfile.is_zipfile(filename)
    crc_list = []
    if is_zip:
        namelist = zipfile.ZipFile(filename, 'r').namelist()
        print(namelist)
        for i in namelist:
            var = zipfile.ZipFile(filename, 'r').getinfo(i).CRC
            # print(bytes.hex(var))
            o2h = hex(var)
            crc_list.append(o2h)
            print(o2h)
    else:
        print("不是ZIP文件")
        exit(0)
    return crc_list


# 爆破 3bytes
def brute3bytes(crcs):
    flag = b""
    # 字典
    print("============3 Bytes=============")
    dic = string.printable  # 根据需求来修改
    for crc in crcs:
        for word in product(dic, repeat=3):
            # 转化为 bytes 类型
            word = "".join(word).encode()
            crcValue = zlib.crc32(word)
            if crcValue == int(crc, 16):
                print("{}----->正确".format(word))
                flag += word
                break
            else:
                continue
    print(flag)


# 爆破 4bytes
def brute4bytes(crcs):
    flag = b""
    # 字典
    print("============4 Bytes=============")
    dic = string.printable  # 根据需求来修改
    for crc in crcs:
        for word in product(dic, repeat=4):
            # 转化为 bytes 类型
            word = "".join(word).encode()
            crcValue = zlib.crc32(word)
            if crcValue == int(crc, 16):
                print("{}----->正确".format(word))
                flag += word
                break
            else:
                continue
    print(flag)


# 爆破 5bytes
def brute5bytes(crcs):
    flag = b""
    # 字典
    print("============5 Bytes=============")
    dic = string.printable  # 根据需求来修改
    for crc in crcs:
        for word in product(dic, repeat=4):
            # 转化为 bytes 类型
            word = "".join(word).encode()
            crcValue = zlib.crc32(word)
            if crcValue == int(crc, 16):
                print("{}----->正确".format(word))
                flag += word
                break
            else:
                continue
    print(flag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="爆破CRC32的值（3bytes、4bytes、5bytes\n By --St4rry）")
    parser.add_argument('-b', '--byte', type=int, help="Choose Bytes【3 or 4 or 5】")
    parser.add_argument('-f', '--file', type=str, help="zip file name")
    args = parser.parse_args()
    # filename = r"F:\CTF\moectf\2022\cccccrc.zip"
    # print(args.__dict__['byte'])
    crc_list = getCRC(args.file)
    # print(byte)
    if args.byte == 4:
        brute4bytes(crc_list)
    # brute4bytes(crc_list)
