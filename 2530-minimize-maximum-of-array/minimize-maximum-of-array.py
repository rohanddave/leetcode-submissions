class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can(val, numbers): 
            for i in range(len(numbers) - 1, 0, -1):
                number_operations = numbers[i] - val
                if number_operations <= 0:
                    continue
                numbers[i] -= number_operations
                numbers[i - 1] += number_operations
            return max(numbers) <= val
            
        left, right = 0, max(nums)
        while left < right: 
            m = (left + right) // 2

            if can(m, nums.copy()):
                right = m
            else:
                left = m + 1
        return left