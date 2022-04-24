from typing import List




class Solution:
    def max_area(self, array: List[int]) -> int:
        max_array = 0
        for left in range(len(array)):
            for right in range(len(array)):
                mr = (right - left) * min(array[left] , array[right])
                if mr > max_array:
                    max_array = mr
        return max_array



print(Solution().max_area([1,8,6,2,5,4,8,3,7]))