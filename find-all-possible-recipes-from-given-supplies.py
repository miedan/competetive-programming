class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        count = defaultdict(int)
        graph = defaultdict(list)
        que = deque(supplies)
        print(que)
        output = []

        for i in range (len(recipes)): 
            for j in ingredients[i]:
                graph[j].append(recipes[i])
                count[recipes[i]] += 1

        while que:
             now = que.popleft()


             for recipe in graph[now]:
                 count[recipe] -= 1

                 if count[recipe] == 0:
                     que.append(recipe)
                     output.append(recipe)


        
        return output