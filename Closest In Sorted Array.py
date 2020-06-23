class Solution(object):
  def closest(self, array, target):
      """
      input: int[] array, int target
      return: int
      """
      # write your solution here
      if not array:
       return -1
      left=0
      right=len(array)-1
      while left < right - 1:
        mid = (left+right) // 2
        if array[mid] < target:
          left= mid
        elif array[mid] > target:
          right = mid
        else:
          return mid
      if abs(array[left] - target) < abs(array[right] - target):
        return left
      else:
        return right
