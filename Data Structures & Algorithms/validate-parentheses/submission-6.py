class Solution:
    def isValid(self, s: str) -> bool:
        s_dict={")":"(",
                "}":'{',
                "]":"["
        }
        s_list=[]
        for chr in s:
            if chr not in s_dict.keys():
                s_list.append(chr)
            else:
                if len(s_list)==0:
                    return False
                else:
                    chr1=s_list.pop()
                    if chr1!=s_dict.get(chr):
                        return False
                
        if len(s_list)==0:
            return True
        else:
            return False
        
        

        



        
        


        