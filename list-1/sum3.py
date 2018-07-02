# coding=utf-8
"""
Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""

def sum3(nums):
  s=0
  for num in nums:
    s+=num
  return s

def sum3_2(nums):
    return sum(nums)


print(sum3_2([1,2,3]))