class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i , j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        res.extend(nums2[j:])
        res.extend(nums1[i:])

        print(res)
        
        if len(res) % 2 == 0:
           median = (res[(len(res)//2) - 1] + res[(len(res))//2]) / 2
        else:
           median =  res[len(res) // 2]
        return median