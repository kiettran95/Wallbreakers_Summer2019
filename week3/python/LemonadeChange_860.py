class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes=dict()
        changes[5]=0
        changes[10]=0
        changes[20]=0
        for bill in bills:
            if bill==5:
                changes[5]+=1
            elif bill==10:
                changes[5]-=1
                if changes[5]<0:
                    return False
                else:
                    changes[bill]+=1
            else:
                if changes[10]>0 and changes[5]>0:
                    changes[10]-=1
                    changes[5]-=1
                elif changes[5]>2:
                    changes[5]-=3
                else:
                    return False
                changes[bill]+=1

        return True
                
        
