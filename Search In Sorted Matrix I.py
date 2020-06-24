class Solution(object):
    def search(self, matrix, target):
        """
    input: int[][] matrix, int target
    return: int[]
    """
        # write your solution here
        M, N = len(matrix), len(matrix[0])
        if M==0 or N==0:
          return [-1,-1]
        left, right = 0, M * N - 1
        while left < right - 1:
            mid = (left + right) // 2
            mid_i, mid_j = mid // N, mid % N
            if matrix[mid_i][mid_j] < target:
                left = mid + 1
            elif matrix[mid_i][mid_j] > target:
                right = mid - 1
            else:
                return [mid_i, mid_j]
        left_i, left_j = left // N, left % N
        right_i, right_j = right // N, right % N
        if matrix[left_i][left_j] == target:
            return [left_i, left_j]
        elif matrix[right_i][right_j] == target:
            return [right_i, right_j]
        else:
            return [-1, -1]

matrix=[[1,2],[2,3]]
target=3
a=Solution()
b=a.search(matrix,target)
print(b)