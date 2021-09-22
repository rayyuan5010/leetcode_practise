'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].

'''
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        #nums = sorted(nums,reverse=True)
        target_number = total // k
        if total % k != 0: return False
        output = [[] for i in range(k)] 
       
        for i,v in enumerate(nums):
            for j in output:
                sum_  = sum(j)
                print(f"v : {v} \r\n sum : {sum_}")
                if sum_ < target_number and (sum_ + v) <= target_number:
                    j.append(v)
                    nums[i] == -1
                    break
        print(f" nums : {nums} output : {output}")
        for i in output:
            if not sum(i) == target_number:
                return False
                
        return not self.is_someone_empty(output)

    def is_someone_empty(self,datas):
        for i in datas:
            if len(i) ==0:
                return True
        return False


print(Solution().canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269],5))