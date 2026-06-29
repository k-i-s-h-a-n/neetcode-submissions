class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s)!=len(t):
            return False
            
        ds1={}
        ds2={}

        for i in s:
            ds1[i]=s.count(i)

        for i in t:
            ds2[i]=t.count(i)

        ans=0
        for i in ds1:
            if i in ds1 and i in ds2:
                print(i)
                if ds1[i] == ds2[i]:
                    ans=1
                else:
                    ans=0
            else:
                return False
                break           
            
        if ans == 1:
            return True
        else:
            return False