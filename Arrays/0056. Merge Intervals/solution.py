from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        start1 = intervals[0][0]
        end1= intervals[0][1]
        res = []

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:
                start1 = start1
                end1 = max(end1, end2)
                continue
            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2

        res.append([start1,end1])

        return res

#-----------------main program-----------------------
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    res = sol.merge(intervals)
    print(intervals)
    print(res)


