class Solution:
    def searchInsert( nums, target) -> int:
        if target==0:
            return 0
        for i in range(0,len(nums),1):
         
            if target <= nums[i]:
        
                return i
        return len(nums)
print(Solution.searchInsert([1,3],2))
