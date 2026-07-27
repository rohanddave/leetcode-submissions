class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''
        problem: 
        - locations[i] = position of city i 
        - move from locations[i] to locations[j] costs |locations[i] - locations[j]| fuel
        - fuel cannot be negative at any point 
        - given start, finish and fuel
        - allowed to visit a city more than once
        
        goal: return count of all possible routes from start to finish 

        observations: 
        - dfs function returns the number of possible rotues from current city to finish with fuel f 
        - 

        approach: 
        - base case would be when fuel == 0 we cannot move to any other city so return 1 if at finish else 0
        - if fuel != 0 then current number of ways = 1 if at finish else 0 and then try to move to every possible other city
        - when at city i iterate over all locations and if |locations[i] - locations[j]| <= fuel move to that city 

        '''
        MOD = 10**9 + 7
        memo = {}
        def dfs(i, fuel):
            if fuel == 0:
                return 1 if i == finish else 0
            if (i, fuel) in memo:
                return memo[(i, fuel)]
            
            ways = 1 if i == finish else 0
            for j in range(len(locations)): 
                if j == i:
                    continue 
                fuel_required = abs(locations[i] - locations[j])
                if fuel_required <= fuel: 
                    ways += dfs(j, fuel - fuel_required)
            memo[(i, fuel)] = ways
            return memo[(i, fuel)]
        return dfs(start, fuel) % MOD
            
