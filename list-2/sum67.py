# coding=utf-8
"""
Return the sum of the numbers in the array, except ignore sections of
 numbers starting with a 6 and extending to the next 7 (every 6 will be
  followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
def sum67(nums):
  sum=0
  if len(nums)==0:
    return 0
  else:
    index=0
    while index<=len(nums)-1:
      if nums[index]!=6:
        sum+=nums[index]
        index+=1
      else:
        while nums[index]!=7:
          index+=1
        index+=1
    return sum


#print(sum67([1, 2, 2]))
#print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))