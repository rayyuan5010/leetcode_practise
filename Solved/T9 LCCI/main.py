'''
On old cell phones, 
users typed on a numeric keypad and the phone would provide a list of words that matched these numbers. 
Each digit mapped to a set of 0 - 4 letters. Implement an algo­rithm to return a list of matching words, 
given a sequence of digits. You are provided a list of valid words. 
The mapping is shown in the diagram below:
'''
class Solution:
    def getValidT9Words(self, num: str, words):
        output = words   
        for i,v in enumerate(num):
            output = self.check_number(i,v,output)
        return output
    def check_number(self,index , num ,words):
        keyboard = [
          None,None,  "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"
        ]
        return_values = []
        for i in words:
            if i[index] in keyboard[int(num)]:
                return_values.append(i)
        return return_values