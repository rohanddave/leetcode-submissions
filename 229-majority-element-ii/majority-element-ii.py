class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = 3
        candidates = {} 

        for num in nums: 
            if num in candidates: 
                candidates[num] += 1
            elif len(candidates) < k - 1: 
                candidates[num] = 1
            else: 
                remove = [] 
                for cand in candidates: 
                    candidates[cand] -= 1
                    if candidates[cand] == 0:
                        remove.append(cand)
                
                for cand in remove: 
                    del candidates[cand]

        actual_counts = {cand: 0 for cand in candidates.keys()}
        
        for num in nums: 
            if num in actual_counts: 
                actual_counts[num] += 1
        
        return [
            cand 
            for cand, freq in actual_counts.items() 
            if freq > len(nums) // k
        ]
        return list(candidates.keys())
        