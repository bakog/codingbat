# coding=utf-8
"""
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'


"""
def double_char(str):
  newstring=''
  for char in str:
    newstring+=char*2
  return newstring