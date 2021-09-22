class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or sum(nums) % k != 0 or max(nums) > sum(nums) // k:
            return False
        nums.sort()
        avg = sum(nums) // k
        visited = [False] * len(nums)
        return self.dfs(nums, k, avg, 0, visited, 0, 0)
    
    def dfs(self, nums, k, target, groups, visited, total, start_ind):
        if groups == k:
            return True
        if groups > k or total > target:
            return False
        if target == total:
            return self.dfs(nums, k, target, groups + 1, visited, 0, 0)
        
        for i in range(start_ind, len(nums)):
            if visited[i]:
                continue
            
            visited[i] = True
            if self.dfs(nums, k, target, groups, visited, total + nums[i], i + 1):
                return True
            visited[i] = False
        return False