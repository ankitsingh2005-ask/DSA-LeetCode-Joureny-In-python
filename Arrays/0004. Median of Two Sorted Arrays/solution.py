class Solution():

    # Function to merge two sorded array and then find there median 
    def findMedianOfSortedArray(self, nums1, nums2):

        i = j = 0
        res = []

        # while i is less then len nums1 and j is less then len nums2
        while i < len(nums1) and j < len(nums2):
            #if the element of nums1 is less or equal to the element of nums2 then
            if nums1[i] <= nums2[j]:
                #then add the element of nums1 to result
                res.append(nums1[i])
                #increment the i by one 
                i += 1

            else:
                res.append(nums2[j])
                #increment j by one
                j += 1

        # Now loop for the j if there is no any element left in the nums1
        while j < len(nums2):
            res.append(nums2[j])
            #increment j by one in until no element left in the array 
            j += 1

        # this one for i if there no element left in nums2
        while i < len(nums1):
            res.append(nums1[i])
            #And increment i until no element left in nums1
            i += 1

        n = len(res)

        # if the element in the array is odd 
        if n % 2 == 1:
            return float(res[n // 2])
        
        # if the element in the array is even
        else:
            return (res[n // 2 - 1] + res[n // 2]) / 2.0

# --------main program--------

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2]
    nums2 = [3,4]

    result = solution.findMedianOfSortedArray(nums1, nums2)

    print(result)

    
    