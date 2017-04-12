#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2/10/16 base trans. wrote by srcdog on 20th, April, 2009
# ld elements in base 2, 10, 16.

import os,sys

# global definition
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]

# bin2dec
# 二进制 to 十进制: int(str,n=10)
def bin2dec(string_num):
  return int(string_num, 2)

# hex2dec
# 十六进制 to 十进制
def hex2dec(string_num):
  return str(int(string_num.upper(), 16))

# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
  num = int(string_num)
  mid = []
  while True:
    if num == 0: break
    num,rem = divmod(num, 2)
    mid.append(base[rem])

  return ''.join([str(x) for x in mid[::-1]])

# dec2hex
# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
  num = int(string_num)
  mid = []
  while True:
    if num == 0: break
    num,rem = divmod(num, 16)
    mid.append(base[rem])

  return ''.join([str(x) for x in mid[::-1]])

# hex2tobin
# 十六进制 to 二进制: bin(int(str,16))
def hex2bin(string_num):
  return dec2bin(hex2dec(string_num.upper()))

# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
  return dec2hex(bin2dec(string_num))
