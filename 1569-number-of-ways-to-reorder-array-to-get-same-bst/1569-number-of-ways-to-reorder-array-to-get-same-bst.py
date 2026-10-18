import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            n = len(arr)
            if n <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            
            ways_comb = math.comb(len(left) + len(right), len(left)) % MOD
            
            ways_left = helper(left)
            ways_right = helper(right)
            
            return (ways_comb * ways_left * ways_right) % MOD

        return (helper(nums) - 1) % MOD