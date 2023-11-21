class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = -1
        for i in range(k):
            nums.insert(0, nums[r])
            nums.pop()
