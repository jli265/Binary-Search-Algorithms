class Solution(object):
  def sqrt(self, x):
    """
    input: int x
    return: int
    """
    # write your solution here
    if x == 0:
      return 0
    elif x <= 3:
      return 1
    else:
       left=1
       right=x/2
       while left <= right:
         mid = (left+right)//2
         if (mid+1)**2 <= x:
           left= mid +1
         elif mid**2>x:
           right = mid -1
         else:
           return mid
