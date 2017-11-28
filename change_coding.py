# -*-coding:utf-8-*-
import chardet


def change_coding(text, coding):
    charset = chardet.detect(text)['encoding']  # 读取字符串的编码
    if charset != coding.upper() and charset != coding.lower():  # 判断字符编码是否需要转换
        text = text.decode(charset).encode(coding)
    return text
