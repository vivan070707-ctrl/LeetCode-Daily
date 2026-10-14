class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val < 0 or sum_val > 9 * num:
            return ""
        
        digits = []
        remaining_sum = sum_val
        
        for i in range(num):
            
            d = min(9, remaining_sum)
            digits.append(str(d))
            remaining_sum -= d
        if remaining_sum > 0:
            return ""
            
        return "".join(digits)

