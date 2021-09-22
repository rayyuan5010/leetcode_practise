"""
https://leetcode.com/problems/tallest-billboard/submissions/

You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.
"""

class Solution:
    mx=0
    def tallestBillboard(self, rods) -> int:
        sum = 0
        for i in rods:
            sum += i
        if not sum % 2 == 0:
            del rods[0]
            sum -= 1
        evg = sum // 2
        if evg  <  rods[len(rods)-1]:
            return 0
        # print(t)
        
        return evg 

        
    
    
print(Solution().tallestBillboard( [1,2,3,6]))