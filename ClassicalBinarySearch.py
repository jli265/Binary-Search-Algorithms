class Solution(object):
  def binarySearch(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array:
      return -1
    left=0
    right=len(array)-1
    while left<=right:
      mid = (left+right) // 2
      if array[mid] == target:
        return mid
      elif array[mid] > target:
        right= mid -1
      else:
        left=mid +1
    return -1
