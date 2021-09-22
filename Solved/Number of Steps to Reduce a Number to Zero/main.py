class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while(not num == 0):
            num = self.run(num)
            count += 1
        return count
    def run(self,num):
        if num % 2 == 0:
            return num //2
        else:
            return num - 1