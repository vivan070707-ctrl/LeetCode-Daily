from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squared = sorted([x * x for x in nums])
        
        n = len(squared)
        k = n // 2  
        
        score = 0
        for i in range(k):
            score -= squared[i]
            
        for i in range(k, n):
            score += squared[i]
            
        return score