class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        '''
        goal: find the first overlapping interval of size atleast dur. if none return []

        observations: 
        - slots for each person don't overlap 
        - slots are sorted by start time 

        approach: 
        - maintain a pointer for each list i, j
        - if does_overlap(slots1[i], slots2[j])
            overlap_start = max(slots1[i][0], slots2[j][0])
            overlap_end = min(slots1[i][1], slots2[j][1])
            overlap_duration = overlap_end - overlap_start 
            if overlap_duration >= dur:
                return [overlap_start, overlap_start + dur]
            else:

        - else:
            if slots1[i][1] < slots2[j][1]
                i += 1
            elif slots2[j][1] < slots1[i][1]:
                j += 1
            else:
                i+= 1
                j += 1

        complexity: 
        TC: O(len(slots1) + len(slots2))
        SC: O(1)
        '''
        def does_overlap(a, b): 
            return not (a[1] < b[0] or a[0] > b[1])
        
        slots1.sort()
        slots2.sort() 
        
        i, j = 0, 0 
        while i < len(slots1) and j < len(slots2):
            slot_A, slot_B = slots1[i], slots2[j]
            if does_overlap(slot_A, slot_B):
                overlap = (max(slot_A[0], slot_B[0]),  min(slot_A[1], slot_B[1]))
                overlap_duration = overlap[1] - overlap[0]
                if overlap_duration >= duration:
                    return [overlap[0], overlap[0] + duration]

            if slot_A[1] < slot_B[1]:
                i += 1
            elif slot_B[1] < slot_A[1]:
                j += 1
            else:
                i+= 1
                j += 1
        return []

        