from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        a = firstList
        b = secondList
        res = []
        i = 0
        j = 0

        while (i < len(a) and j < len(b)):
            start1 = a[i][0]
            end1 = a[i][1]
            start2 = b[j][0]
            end2 = b[j][1]

            if max(start1, start2) <= min(end1, end2):    
                s = max(start1, start2)
                e = min(end1,end2)
                res.append([s,e])
                
                        
            if end1 <= end2:
                i += 1
            else:
                j += 1

        return res        

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    res = sol.intervalIntersection(firstList, secondList)
    print(res)

        