class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        points[i] = [x start, x end] denotes the start and end of balloon 
        arrows can be show vertically upwards from any x 
        a balloon is burst if x start <= x = x end 
        return minimum number of arrows to burst all balloons 

        to minimize number of arrows we try to burst max balloons with one arrow
        for an arrow we choose x with maximum overlap 

        so overlapping intervals are burst with one arrow
        we merge intervals and find the length of non overlapping intervals 
        '''
        points.sort() 

        # intersection list
        curr = points[0]
        count = 1

        # helper function to check if there is an overlap 
        def does_overlap(a, b): 
            return not (a[1] < b[0] or a[0] > b[1])

        for i in range(1, len(points)):
            point = points[i]
            if does_overlap(curr, point):
                curr = [max(curr[0], point[0]), min(curr[1], point[1])]
            else:
                curr = point
                count += 1
        return count




        
        