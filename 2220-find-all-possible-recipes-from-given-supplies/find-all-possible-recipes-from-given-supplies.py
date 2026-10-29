class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        recipes_set = set(recipes)
        supplies_set = set(supplies)

        adj = collections.defaultdict(list)
        for i, recipe in enumerate(recipes):
            adj[recipe].extend(ingredients[i])
        
        BLACK, WHITE, GREY = 0, 1, 2
        colors = collections.defaultdict(lambda: WHITE)

        @cache
        def dfs(recipe):
            if colors[recipe] == GREY:
                return False
            if recipe not in recipes_set:
                return recipe in supplies_set
            
            res = True
            colors[recipe] = GREY
            for ing in adj[recipe]:
                res = res and dfs(ing)
            colors[recipe] = BLACK
            return res
        
        res = [] 
        for recipe in recipes:
            if dfs(recipe):
                res.append(recipe)
        return res