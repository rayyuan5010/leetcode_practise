'''
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 
'''
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        output = []
        while a or b:
            # find who go first
            append_a = False
            if len(output) >= 2 and output[-1] == output[-2]:
                append_a = output[-1] == 'b'
            else:
                append_a = a>=b
                
                
            if append_a:
                a-=1
                output.append('a')
            else:
                b-=1
                output.append('b')
        return ''.join(output)

print(Solution().strWithout3a3b(6,4))
'''
6 4 
aabbaabbaa

8 a 3 b 

aabaabaabaa


'''

