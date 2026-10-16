class Solution:
    def findMin(self, nums: List[int]) -> int:
        minele = float('inf')
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        return nums[l]

# [4,5,6,7]
# l = 0, nl = 4
# r=3, nr = 7
# m = 2, nm = 5

# r = 2, nr = 6
# m = 1, nm = 5

# r = 1, nr = 5
# m = 0, nm = 4
# r = 0