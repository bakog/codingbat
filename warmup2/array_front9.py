# coding=utf-8
"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
 The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
  count=0
  for n in nums:
    if n==9 and count<3:
      return True
    count+=1
  return False


def array_front9_orginal(nums):
    # First figure the end for the loop
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):  # loop over index [0, 1, 2, 3]
        if nums[i] == 9:
            return True
    return False