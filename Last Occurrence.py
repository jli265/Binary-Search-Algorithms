class Solution(object):
  def lastOccur(self, array, target):
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
      mid = (left+right)//2
      if array[mid] < target:
         left = mid + 1
      elif array[mid] > target:
         right = mid - 1
      else:
         left = mid
    if array[right] == target:
      return right
    elif array[left] == target:
      return left
    else:
      return -1
