# coding=utf-8
"""
Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""

def has23(nums):
  if (2 in nums) or (3 in nums):
    return True
  return False

def has23_2(nums):
    return (2 in nums) or (3 in nums)

print(has23_2([1,2,6]))