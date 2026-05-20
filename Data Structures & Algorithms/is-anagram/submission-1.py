class Solution:
    def isAnagram(self, s: str, t: str):
        s1_count = dict()
        s2_count = dict()
        for i in s:
            s1_count[i] = s1_count.get(i,0) + 1
        for k in t:
            s2_count[k] = s2_count.get(k,0) + 1
        return s1_count == s2_count
        
      

        
        

        
        