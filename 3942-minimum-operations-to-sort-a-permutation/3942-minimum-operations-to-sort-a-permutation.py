from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        target = list(range(n))
        
        if nums == target:
            return 0
            
        target_states = set()
        
        for i in range(n):
            if nums[i] == 0:
                shifted = nums[i:] + nums[:i]
                if shifted == target:
                    target_states.add((0, i))
                    
        rev_nums = nums[::-1]
        for i in range(n):
            if rev_nums[i] == 0:
                shifted = rev_nums[i:] + rev_nums[:i]
                if shifted == target:
                    target_states.add((1, i))
                    
        if not target_states:
            return -1
            
        dist = {(0, 0): 0}
        q = deque([(0, 0)])
        
        while q:
            type_, i = q.popleft()
            d = dist[(type_, i)]
            
            if (type_, i) in target_states:
                return d
                
            ntype1 = type_
            ni1 = (i + 1) % n
            if (ntype1, ni1) not in dist:
                dist[(ntype1, ni1)] = d + 1
                q.append((ntype1, ni1))
                
            ntype2 = 1 - type_
            ni2 = (-i) % n
            if (ntype2, ni2) not in dist:
                dist[(ntype2, ni2)] = d + 1
                q.append((ntype2, ni2))
                
        return -1