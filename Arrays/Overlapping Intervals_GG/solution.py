class Solution:
    def isIntersect(self, intervals):

        intervals.sort()

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            start1 = intervals[i][0]
            end1 = intervals[i][1]

            if start1 <= end:
                return True

            start = start1
            end = end1

            
        return False

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [5, 7], [2, 4], [6, 8]]
    res = sol.isIntersect(intervals)
    print(res)
