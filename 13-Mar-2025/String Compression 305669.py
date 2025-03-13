# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        pos1 = 0
        pos2  = 0
        cur = chars[0]
        count = 0


        while pos2 < len(chars):
            if cur == chars[pos2]:
                count+=1
                pos2+=1
            else:
                chars[pos1] = cur
                pos1+=1
                cur = chars[pos2]
                if count != 1:
                    count = str(count)
                    while len(count) != 0:
                        chars[pos1] = count[0]
                        count = count[1:]
                        pos1+=1              
                count = 0
                
        chars[pos1] = cur
        pos1+=1
        print(count)
        if count != 1:
            count = str(count)
            while len(count) > 0:
                chars[pos1] = count[0]
                count = count[1:]
                pos1+=1 
    
        chars = chars[:pos1]
        return pos1

            




        