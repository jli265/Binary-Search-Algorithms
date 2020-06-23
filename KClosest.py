class Solution(object):
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    # write your solution here
    if k == 0:
      return None
    else:
        left=0
        right=len(array)-1
        idx_closest = None
        while left < right -1:
          mid = (left+right) // 2
          if array[mid] < target:
             left = mid
          elif array[mid] > target:
             right = mid
          else:
             idx_closest = mid
             lst = [array[idx_closest]]
             break
        if not idx_closest:
            if abs(array[left] - target) < abs( array[right] - target):
               idx_closest = left 
            else:
               idx_closest = right 
            lst = [array[idx_closest] ]
        left, right = idx_closest - 1, idx_closest + 1 
        while len(lst) < k and left >=0 and right <= len(array)-1:
             if abs(array[left]- target) < abs(array[right]- target):
                lst.append(array[left])
                left -= 1
             else:
                lst.append(array[right])
                right += 1
        if len(lst) < k and left < 0:
            for i in range(right,(right + k-len(lst))):
                lst.append( array[i]  )
        if len(lst) < k and right > len(array)-1:
            for i in range(left,(left - k + len(lst)),-1):            
                lst.append( array[i] )
        return lst

