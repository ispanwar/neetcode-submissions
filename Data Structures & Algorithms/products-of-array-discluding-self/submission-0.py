class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix = 1,1
        n = len(nums)
        result = [1]*n

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        for j in range(n-1,-1,-1):
            result[j] *= suffix
            suffix *= nums[j]

        return result