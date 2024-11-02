from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in d:
                return [d[needed], i]
            d[nums[i]] = i
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([5,5], 10))
    print(solution.twoSum([2,7,4,5], 9))