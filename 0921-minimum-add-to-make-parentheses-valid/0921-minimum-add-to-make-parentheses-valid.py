class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves=0
        balance=0
        
        for ch in s:
            if ch =="(":
                balance+=1
            else:
                if balance>0:
                    balance-=1
                else :
                    moves+=1
        moves+=balance
        return moves
        