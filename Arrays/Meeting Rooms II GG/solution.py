class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()

        n = len(start)
        rooms = 0
        res = 0
        i = 0
        j = 0

        # Iterate through all the meetings
        while i < n and j < n:
            # If a meeting has started, allocate a room
            if start[i] < end[j]:
                rooms += 1
                res = max(res, rooms)
                i += 1

            # If a meeting has ended, free up a room
            else:
                rooms -= 1
                j += 1

        return res


#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    start = [0, 5, 13, 24]
    end = [2, 10, 23, 25]

    res = sol.minMeetingRooms(start, end)
    print(res)
