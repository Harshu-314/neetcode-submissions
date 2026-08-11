class Solution:
    def isValid(self, s: str) -> bool:
        brackets={"[":"]","{":"}","(":")"}
        h=[]
        for char in s:
            if char in brackets.keys():
                h.append(char)
            else:
                if not h:#means stack is empty
                    return False
                elif brackets[h.pop()]!=char:
                    return False
        return len(h)==0
            
            
             