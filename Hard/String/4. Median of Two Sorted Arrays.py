class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        new = []
        while i < len(nums1):
            while j < len(nums2) and nums2[j] < nums1[i]:
                new.append(nums2[j])
                j += 1
            new.append(nums1[i])
            i += 1
        new += nums2[j:]
        print(new)
        if len(new) % 2 == 1:
            return new[len(new) // 2]
        else:
            return (new[int(len(new) / 2) - 1] + new[int(len(new) / 2)]) / 2