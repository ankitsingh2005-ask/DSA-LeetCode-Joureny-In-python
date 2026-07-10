class Solution():

    # Function to merge two sorted array
    def merge(self, nums1, m, nums2, n):

        i = j = 0
        res = []

        # while i is less then m and j is less then n
        while i < m and j < n:

            # check is the nums1 element at the zero position is less then the element of the nums2 at the zero position
            if nums1[i] <= nums2[j]:
                # if yes then add that element to the result array at zero position
                res.append(nums1[i])
                # And then increse the i by one
                i += 1

            # else if the element of the nums1 is >= then add the element of the nums2 in result
            else:
                res.append(nums2[j])
                # and then increment the j by one 
                j += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        for k in range(m + n):
            nums1[k] = res[k]


# -------main program-----
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    solution.merge(nums1, m, nums2, n)

    print(nums1)

