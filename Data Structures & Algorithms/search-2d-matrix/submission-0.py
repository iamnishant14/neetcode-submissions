class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        start,end = 0,rows*cols-1 
        while start<=end:
            mid = start+ (end-start)//2
            row,col = mid//cols,mid%cols
            if target > matrix[row][col]:
                start=mid+1
            elif target< matrix[row][col]:
                end=mid-1
            else:
                return True
        return False
