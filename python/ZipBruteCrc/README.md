### ZipBruteCrc

```
$ python.exe .\ZipBruteCrc.py -h
usage: ZipBruteCrc.py [-h] [-b BYTE] [-f FILE]

爆破CRC32的值（3bytes、4bytes、5bytes By --St4rry）

optional arguments:
  -h, --help            show this help message and exit
  -b BYTE, --byte BYTE  Choose Bytes【3 or 4 or 5】
  -f FILE, --file FILE  zip file name
```

- 举例：
  ```
  └─$ python.exe ZipBruteCrc.py -b 4 -f cccccrc.zip
  ['1.txt', '2.txt', '3.txt', '4.txt']
  0x67b2d3df
  0x628abed2
  0x6b073427
  0x8c8da10
  ============4 Bytes=============
  b'moec'----->正确
  b'tf{q'----->正确
  b'wq_c'----->正确
  b'rc!}'----->正确
  b'moectf{qwq_crc!}'
  ```

  

