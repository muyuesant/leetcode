# https://leetcode.com/problems/evaluate-division/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(root, target, eqMap, visit) -> float:
            # print(root,target)
            if root not in visit:
                visit.add(root)
                if root not in eqMap:
                    return -1.0
                elif root == target:
                    return 1.0
                else:
                    temps= []
                    for child, val in eqMap[root]:
                        if target == child:
                            return val
                        else:
                            temps.append( val * dfs(child, target,eqMap, visit) )
                    temps = list(filter(lambda x: x > 0 or x == 0.0, temps))
                    if len(temps) > 0:
                        return temps[0]
                    else:
                        return -1.0
                            
                            
            else:
                return -1.0
                    
        eqMap = {}
        for i in range(len(equations)):
            a,b = equations[i]
            if a not in eqMap:
                eqMap[a] = [[b, values[i]]]
            else:
                eqMap[a].append([b, values[i]])
            if b not in eqMap:
                eqMap[b] = [[a, 1 / values[i]]]
            else:
                eqMap[b].append([a, 1/ values[i]])
        # print(eqMap)  
        result = []
        
        for c,d in queries:
            visit = set()
            temp = dfs(c,d,eqMap, visit)
            result.append(temp)
            # print()
        return result
        
        # eqMap = {}
#         for i in range(len(equations)):
#             aMap = {}
#             bMap = {}
#             for c in equations[i][0]:
#                 if c not in aMap:
#                     aMap[c] = 1
#                 else:
#                     aMap[c] += 1
                
#             for c in equations[i][1]:
#                 if c not in bMap:
#                     bMap[c] = 1
#                 else:
#                     bMap[c] += 1
            
#             for c in aMap.keys():
#                 if c in bMap:
#                     # if aMap[c] == bMap[c]:
#                     #     aMap[c] = 0
#                     #     bMap[c] = 0
#                     # else:
#                     sub = min(aMap[c], bMap[c])
#                     aMap[c] = aMap[c] - sub
#                     bMap[c] = bMap[c] - sub
#             a = ""
#             aCoe = 1
#             b = ""
#             bCoe = 1
#             for k, v in aMap.items():
#                 if v > 0:
#                     a += k
#                     aCoe *= v
#             for k, v in bMap.items():
#                 if v > 0:
#                     b += k
#                     bCoe *= v
#             if a not in eqMap:
#                 eqMap[a] = [[b, values[i] * bCoe / aCoe]]
#             else:
#                 eqMap[a].append([b, values[i] * bCoe / aCoe])
#             if b not in eqMap:
#                 eqMap[b] = [[a, aCoe / bCoe / values[i]]]
#             else:
#                 eqMap[b].append([a, aCoe / bCoe / values[i]])
#         print(eqMap)
#         result = []
#         for query in queries:
#             if query[0] not in eqMap:
#                 result.append(-1.0)
#             elif query[0] == query[1]:
#                 result.append(1.0)
#             else:
#                 for c, coe in eqMap[query[0]]:
#                     something
        # return result