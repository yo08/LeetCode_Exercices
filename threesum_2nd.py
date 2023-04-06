from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[List[int]]:
        results = []
        triplets = list(combinations(nums, 3))
        # print(type(triplets))
        # print(triplets)
        # return triplets

        for triplet_tuple in triplets:
            triplet = sorted(triplet_tuple)
            if triplet in results:
                pass
            elif triplet[0] + triplet[1] + triplet[2] == 0:
                results.append(triplet)
        return results
