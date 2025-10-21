from typing import List


class Jump:
    def podePular(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False