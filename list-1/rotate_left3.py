# coding=utf-8
"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

def rotate_left3(nums):
  a,b,c = nums
  return [b,c,a]

def rotate_left3_2(nums):
    tmp=nums[0]
    for i  in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[-1]=tmp
    return nums


print(rotate_left3_2([1,2,3]))
print(rotate_left3_2([5,11,9]))