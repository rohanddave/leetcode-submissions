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

        for i, num in enumerate(nums):
            prefix.append(prefix[-1] + num)

        # co-ordinate compression for efficient fenwick tree
        values = sorted(set(prefix))
        index = {
            val: i + 1
            for i, val in enumerate(values)
        }

        # create fenwick tree with compressed co-ordinates 
        # NOTE: fenwick tree stores the frequency of prefix sum at compressed co-ordinate index; tree[i] = val means the compressed co-ordinate index is i and the val is the frequency of the prefix sum
        seen = FenwickTree(len(values))
        seen.update(index[0], 1)

        count = 0
        for i in range(1, len(prefix)):
            left_val, right_val = prefix[i] - upper, prefix[i] - lower

            # we need binary search because left_val and right_val might not exist exactly in fenwick tree, binary search gives us the position of arbitary values 
            # NOTE: fenwick tree is 1 indexed so binary search bounds needs to be handled accrodingly since it return 0 based index
            left_idx = bisect_left(values, left_val) # first greater than equal to 
            right_idx = bisect_right(values, right_val) - 1 # bisect_right = first greater than x; bisect_right - 1 = last less than equal to

            count += seen.range_query(left_idx + 1, right_idx + 1) # converting 0 based index to 1 based index

            seen.update(index[prefix[i]], 1) # increment the freq of prefix[i] by 1


        return count
