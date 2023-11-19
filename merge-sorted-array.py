class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = m
        for i in range(n):
            nums1[l] = nums2[i]
            print(nums1)
            l += 1
        nums1.sort()
