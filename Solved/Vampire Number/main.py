class Solution:
    def is_vampire_number(self, num:int):
        return self.find_all(num,1)
        
        
    def find_all(self,num,f): 
        s = num // f
        if f > s:
            return False
        if f * s == num and self.all_char_in_num_str(num,f,s):
            return True
        else:
            return self.find_all(num,f+1)
    
    def all_char_in_num_str(self,num,f,s):
        str_num = list(str(num))
        for i in str(f):
            if i in str_num :
                str_num.remove(i)
            else:
                return False
        for i in str(s):
            if i in str_num:
                str_num.remove(i)
            else:
                return False
        return True
print(Solution().is_vampire_number(688 ))