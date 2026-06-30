class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        '''
        goal: return number of range sums lie in [lower, upper]

        range sum S(i, j) = sum of elements between indices i, j 
        '''
        n = len(nums)
        prefix = [0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)

        values = sorted(set(prefix))
        index = {
            val: i + 1
            for i, val in enumerate(values)
        }
        seen = FenwickTree(len(values))
        seen.update(index[0], 1)

        count = 0
        curr_sum = 0
        for num in nums: 
            curr_sum += num 
            left_val, right_val = curr_sum - upper, curr_sum - lower

            left_idx = bisect_left(values, left_val) + 1
            right_idx = bisect_right(values, right_val)

            count += seen.range_query(left_idx, right_idx)

            seen.update(index[curr_sum], 1)


        return count
