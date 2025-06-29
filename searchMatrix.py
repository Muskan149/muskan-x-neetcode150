class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        # while top <= bottom:
        while top <= bottom:
            # find a middle row
            mid = (top + bottom) // 2
            # start from middle row's middle index mid
            midRow = matrix[mid]
            # if row.0 <= target <= row.end
                # do binary search within elem
            if midRow[0] <= target <= midRow[-1]:
                left, right = 0, len(midRow) - 1
                # for elem in midRow:
                #     if elem == target:
                #         return True
                # return False
                while left <= right:
                    mid = (left + right) // 2
                    midNum = midRow[mid]
                    if midNum > target:
                        right = mid - 1
                    elif target > midNum:
                        left = mid + 1
                    else:
                        return True
                return False
            # else if row.0 > target:
                # change bottom to row - 1
            elif midRow[0] > target:
                bottom = mid - 1
            # if target > row.end
                # change top to row + 1 
            elif midRow[-1] < target:
                top = mid + 1

        return False
