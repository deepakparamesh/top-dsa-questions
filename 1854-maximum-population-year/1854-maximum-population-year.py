class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_count = {}
    
        # Populate the population_count dictionary.
        for birth, death in logs:
            for year in range(birth, death):  # Note the death year is not included.
                population_count[year] = population_count.get(year, 0) + 1

        # Find the year with the maximum population.
        max_population = max(population_count.values())
        max_population_years = [year for year, count in population_count.items() if count == max_population]

        # Return the earliest year with the maximum population.
        return min(max_population_years)
