class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        '''
        minutes hand:
        60 divisions = 360 degrees
        1 division = ?
        360 / 60 degrees 

        360 degrees = 12 hours 
        x degrees = y hours

        60 mins = 1 hours
        m mins = ?
        '''
        one_min_angle = 6
        one_hour_angle = 30
        minutes_angle = minutes * one_min_angle
        hours_angle = ((minutes / 60) * one_hour_angle) +  hour * one_hour_angle
        diff = abs(hours_angle - minutes_angle)
        return min(diff, 360 - diff)
        