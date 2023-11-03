class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        years = defaultdict(int)
        
        
        logs.sort()

        for birth, death in logs:
            for year in range(birth, death):
                years[year] += 1

        max_population = 0
        max_year = 0
        
        for year, population in years.items():
            if population > max_population:
                max_population = population
                max_year = year

        return max_year


   