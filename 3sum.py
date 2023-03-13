class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        result = []
        for i in range(N - 2):
                   if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    j = i + 1
                    k = N - 1
                    while j < k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            result.append([nums[i], nums[j], nums[k]])
                            while j < k - 1 and nums[k -1] == nums[k]:
                                k -= 1
                            while j + 1 < k and nums[j +1] == nums[j]:
                                j += 1
                            j += 1
                            k -= 1
                        elif nums[i] + nums[j] + nums[k] > 0:
                            k -= 1
                        else:
                            j += 1
        return result
