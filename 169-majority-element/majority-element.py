class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_element, max_freq = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] == max_element: 
                max_freq += 1
            else: 
                max_freq -= 1
                if max_freq == 0:
                    max_element = nums[i]
                    max_freq = 1
        return max_element




        