# 问题： 给定空格区分的词串，返回最后一个非空词的长度（开头结尾去空格）
s="q w e rwe "
print((s.strip().split(" ")[-1]))
print(len(s.strip().split(" ")[-1]))