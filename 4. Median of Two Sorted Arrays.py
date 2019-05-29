class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ary = nums1+nums2
        ary.sort()
        midIndex = len(ary)/2.0
        if(len(ary)%2 != 0):
            midIndex = int(midIndex)
            return ary[midIndex]
        else:
            midIndex = int(midIndex)
            lowIndex = midIndex-1
            upIndex = midIndex
            return (ary[lowIndex] + ary[upIndex])/2.0