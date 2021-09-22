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