# https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        
        result = ""
        brStack = []
        
        i = 0
        while i < len(s):
            if s[i] == "[":
                brStack.append(i)
            elif s[i] == "]":
                oldOffsetToEnd = len(s) - i
                left = brStack.pop(-1)
                numC = left-1
                while numC >= 0 and s[numC].isdigit() :
                    numC -= 1
                numC += 1
                num = int(s[numC:left])
                encoded_str = s[left+1: i]
                s=s[0:numC] + num * encoded_str + s[i+1:]
                i = len(s) - oldOffsetToEnd
            i+=1
        return s
        
#         while s:
            
#             if (left:=s.find("[")) > 0:
#                 numC = left-1
#                 while numC >= 0 and s[numC].isdigit() :
#                     numC -= 1
#                 numC += 1
#                 if numC > 0:
#     #                e.g. abc2[
#                     result += s[0:numC]
               
#                 num = int(s[numC:left])
#                 right = s.find("]")
#                 encoded_string = s[left+1: right]
#                 result += num*encoded_string
#                 if right+1 < len(s):
#                     s = s[right+1:]
#                 else:
#                     break

#             else:
#                 result += s
#                 break
            
        # return result
        