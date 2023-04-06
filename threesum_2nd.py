from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[List[int]]:
        results = []
        triplets = list(combinations(nums, 3))

        for triplet_tuple in triplets:
            if triplet_tuple[0] + triplet_tuple[1] + triplet_tuple[2] == 0:
                triplet = sorted(triplet_tuple)
                if triplet not in results:
                    results.append(triplet)
        return results
