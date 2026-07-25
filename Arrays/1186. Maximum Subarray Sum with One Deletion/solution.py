from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        no_del = arr[0]
        one_del = float('-inf')
        res = arr[0]

        for i in range(1, len(arr)):
            prev_no_del = no_del
            prev_one_del = one_del

            no_del = max(no_del + arr[i], arr[i])

            v1 = prev_no_del
            v2 = prev_one_del + arr[i]

            one_del = max(v1, v2)

            res = max(res ,no_del, one_del)

        return res

#----------------main program---------------------

if __name__ == "__main__":
    sol = Solution()
    arr = [1,-2,0,3]
    result = sol.maximumSum(arr)

    print(result)