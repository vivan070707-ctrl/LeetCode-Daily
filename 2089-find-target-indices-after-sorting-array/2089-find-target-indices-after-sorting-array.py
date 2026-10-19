class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums = sorted(nums)
        output = []
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
                if nums[i] <= len(nums) and nums[i] != target :
                    break
        return output
            
        