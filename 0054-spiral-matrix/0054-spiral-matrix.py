class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=m-1
        top=0
        bottom=n-1
        lst=[]
        while (top<=bottom and left<=right):

            for i in range(left, right + 1):
                lst.append(matrix[top][i])
            top=top+1

            for i in range(top, bottom+1):
                lst.append(matrix[i][right])
            right=right-1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    lst.append(matrix[bottom][i])
                bottom=bottom-1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    lst.append(matrix[i][left])
                left=left+1

        return lst