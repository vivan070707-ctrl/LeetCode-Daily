class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        divisors = [i for i in range(1, n + 1) if n % i == 0]
        
        for k in divisors:
            chunks = [nums[i:i + k] for i in range(0, n, k)]
            possible = True
            prev_max = -float('inf')
            
            for chunk in chunks:
                
                drops = 0
                min_idx = 0
                for i in range(k):
                    if chunk[i] > chunk[(i + 1) % k]:
                        drops += 1
                        min_idx = (i + 1) % k
                
                if drops > 1:
                    possible = False
                    break
                chunk_min = chunk[min_idx]
                chunk_max = chunk[(min_idx - 1) % k]
                if chunk_min < prev_max:
                    possible = False
                    break
                
                prev_max = chunk_max
            
            if possible:
                total_sum += k
                
        return total_sum