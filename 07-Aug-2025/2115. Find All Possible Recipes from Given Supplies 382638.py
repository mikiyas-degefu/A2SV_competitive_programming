# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available_suplies = set(supplies)

        #queue to process recipe indices
        recipe_queue = deque(range(len(recipes)))
        created = []
        last_size = -1

        while len(available_suplies) > last_size:
            last_size = len(available_suplies)
            queue_size = len(recipe_queue)

            while queue_size > 0:
                queue_size -= 1
                idx = recipe_queue.popleft()

                if all (ingredient in available_suplies for ingredient in ingredients[idx]):
                    available_suplies.add(recipes[idx])
                    created.append(recipes[idx])
                else:
                    recipe_queue.append(idx)
        
        return created




        
        
        


        