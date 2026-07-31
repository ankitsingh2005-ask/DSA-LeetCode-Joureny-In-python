from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        temp = []
        inserted = False

        #insert new interval in intervals 
        for interval in intervals:
            if not inserted and newInterval[0] < interval[0]:
                temp.append(newInterval)
                inserted = True
            
            temp.append(interval)

        if not inserted:
            temp.append(newInterval)

        # Code for merge intervals   
        temp.sort()
        result = []
        start1 = temp[0][0]
        end1 = temp[0][1]
        


        for i in range(1, len(temp)):
            
           

            start2 = temp[i][0]
            end2 = temp[i][1]
            if end1 >= start2:
                start1 = start1
                end1 = max(end1, end2)
                continue

            result.append([start1, end1])
            start1 = start2
            end1 = end2

        result.append([start1, end1])

        return result


#---------------------main program---------------------
if __name__ == "__main__":
    sol = Solution()

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    res = sol.insert(intervals, newInterval)
    print(intervals)
    print(res)

        