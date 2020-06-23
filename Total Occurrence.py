class Solution(object):
  def totalOccurrence(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array:
      return 0
    left=0
    right=len(array)-1
    sum=0
    while left < right -1:
      mid = (left+right)//2
      if array[mid] < target:
        left=mid+1
      elif array[mid] > target:
        right=mid-1
      else:
        for i in range(left,right+1):
          if array[i] == target:
            sum += 1
        return sum
    for i in range(left,right+1):
        if array[i] == target:
            sum += 1
    return sum