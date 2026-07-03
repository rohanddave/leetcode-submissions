import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        '''
        goal: minimize maximum number of products given to any store

        n stores and m product types
        quantities[i] = quantity of ith product type 

        distribute all products under rules:
        - a store can be given at most one product type but any amount 

        observation: 
        - answer lies in the answer space [1, max(quantities)]
        - doesn't matter which store we give which product type only the quantity matters
        - can(x) returns true if all products can be distributed to n stores where each store does not receive more than x quantity else returns false 
        - answer space is monotonic (F F F T T T) because if x can be distributed then a higher value can also be distributed 

        approach:
        - bin search on answer space where the bounds are [1, max(quantities)]
        '''
        def can(x):
            nonlocal n
            total_number_of_stores = n
            for quantity in quantities: 
                number_of_stores = math.ceil(quantity / x)
                total_number_of_stores -= number_of_stores

            return total_number_of_stores >= 0

        # if the number of stores are less than the number of product types then not possible to distribute to all stores such that each store gets only one type of product
        if n < len(quantities): 
            return -1

        left, right = 1, max(quantities) 

        while left < right: 
            m = (left + right) // 2

            if can(m): 
                right = m
            else:
                left = m + 1
        return left