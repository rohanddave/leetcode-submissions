class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_arr = [int(value) for value in version1.split('.')]
        v2_arr = [int(value) for value in version2.split('.')]

        print(v1_arr, v2_arr)

        diff = len(v2_arr) - len(v1_arr)
        print(diff)
        if diff > 0: 
            v1_arr.extend([0] * abs(diff))
        elif diff < 0:
            v2_arr.extend([0] * abs(diff))
        
        print(v1_arr, v2_arr)
            
        for i in range(len(v1_arr)):
            if v1_arr[i] < v2_arr[i]:
                return -1
            elif v1_arr[i] > v2_arr[i]:
                return 1
        
        return 0
        