import os
import binascii
import struct
misc = open("secret.png","rb").read()
# a =  misc[12:16] + struct.pack('>i',1)+ misc[20:29]
# # print(a)
image_Crc = int(misc[29:33].hex(),16)
# print(image_Crc,type(image_Crc))

# print(hex(int(a.hex(),16)))
# 爆破宽
for i in range(1024):
    data = misc[12:16] + struct.pack('>i',i)+ misc[20:29]  #IHDR数据
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == image_Crc: #IHDR块的crc32值
        print("hex:"+hex(i))
        print('宽：',i)
        

# 爆破高       
for i in range(1024):
    data = misc[12:20] + struct.pack('>i',i)+ misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == image_Crc:
        print("hex:"+hex(i))
        print('高',i)