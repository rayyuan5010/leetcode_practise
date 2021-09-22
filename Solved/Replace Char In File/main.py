import os 
class Solution:
    def find_file(self,path,target:str,file_name):
        path_list = os.listdir(path)
        for i in path_list:
            new_path = os.path.join(path,i)
            if not '.txt' in i:
                self.find_file(new_path,target,file_name)
            else:
                if not i == file_name:
                    continue
                else:
                    self.read_file(new_path,target)
                    #return True
    def read_file(self,path,target:str):
        file_data = None
        #print(path)
        with open(path,'r') as f:
            file_data= f.read()
        file_data = file_data.replace(target,target.upper())
        with open(path,'w') as f:
            f.write(file_data)

        
Solution().find_file('C:\\Users\\rayyu\\Documents\\leetcode\\testing','apple','rrr.txt')
                    