class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:
        N = len(nums)
        nums.sort()
        results = set()

        for first_index in range(N - 2):
            if nums[first_index] <= 0:
                target = -nums[first_index]
                second_index = first_index + 1
                third_index = N - 1
                while (second_index < third_index):
                    two_sum = nums[second_index] + nums[third_index]
                    if two_sum < target:
                        second_index += 1
                    elif two_sum > target:
                        third_index -= 1
                    else:
                        results.add((nums[first_index], nums[second_index], nums[third_index]))
                        second_index += 1
                        third_index -= 1
        return results
