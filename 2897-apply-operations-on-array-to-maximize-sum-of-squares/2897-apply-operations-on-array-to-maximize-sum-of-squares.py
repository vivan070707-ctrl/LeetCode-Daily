class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        for x in nums:
            for bit in range(31):
                if (x & (1 << bit)):
                    bit_counts[bit] += 1
                    
        new_nums = [0] * k
        for i in range(k):
            current_val = 0
            for bit in range(31):
                if bit_counts[bit] > 0:
                    current_val |= (1 << bit)
                    bit_counts[bit] -= 1
            new_nums[i] = current_val
            
        ans = 0
        for x in new_nums:
            ans = (ans + x * x) % MOD
            
        return ans