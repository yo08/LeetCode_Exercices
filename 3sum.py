from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        result = []

        # e1: 1st element in the list
        # e2: 2nd element in the list
        # e3: 3rd element in the list

        for e1 in range(N - 2):
            if e1 > 0 and nums[e1] == nums[e1 - 1]:
                continue
            e2 = e1 + 1
            e3 = N - 1
            while e2 < e3:
                if nums[e1] + nums[e2] + nums[e3] == 0:
                    result.append([nums[i], nums[e2], nums[e3]])
                    while e2 < e3 - 1 and nums[e3 - 1] == nums[e3]:
                        e3 -= 1
                    while e2 + 1 < e3 and nums[e2 + 1] == nums[e2]:
                        e2 += 1
                    e2 += 1
                    e3 -= 1
                elif nums[e1] + nums[e2] + nums[e3] > 0:
                    e3 -= 1
                else:
                    e2 += 1
        return result
