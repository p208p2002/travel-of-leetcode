class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        p1, p2, p3 = 0, 1, len(nums)-1
        while p1 < len(nums)-2:
            key = -nums[p1]
            if nums[p3] + nums[p3 - 1] < key:
                p1 += 1
                p2 = p1 + 1
                continue
            while p2 < p3:
                if nums[p2] + nums[p3] < key:
                    p2 += 1
                elif nums[p2] + nums[p3] > key:
                    p3 -= 1
                else:
                    ans.add(tuple([nums[p1],nums[p2],nums[p3]]))
                    p2 += 1
                    p3 -= 1
            p1 += 1
            p2 = p1 + 1
            p3 = len(nums) - 1
        return [list(i) for i in ans]
