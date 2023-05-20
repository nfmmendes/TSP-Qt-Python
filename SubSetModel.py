import pulp as pl
import random

class SubSetModel():
    def __init__(self, numberOfCities):
        self.cityPositions = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(numberOfCities)]
        self.subsets =  self.get_subsets([i for i in range(numberOfCities)])
        
        model = pl.LpProblem("TSP With subsets")

        x = { i: { j: pl.LpVariable("x({} , {})".format(i, j), cat = pl.LpBinary) for j in range(numberOfCities) if i !=j } for i in range(numberOfCities) }

        model += pl.lpSum( [x[i][j]*self.distance(i, j) for i in x for j in x[i]])

        for i in x:
            model += pl.lpSum( [x[i][j] for j in x[i] ] ) == 1
        for j in range(numberOfCities):
            model += pl.lpSum( [x[i][j] for i in x if j in x[i]]) == 1
        
        for subset in self.subsets:
            model += pl.lpSum( [x[i][j] for i in x for j in x[i] if i in subset and j in subset] ) == len(subset) - 1

        print(model)
        model.solve()
    
    def distance(self, i, j) -> int:
        return (self.cityPositions[i][0] - self.cityPositions[j][0])**2 + (self.cityPositions[i][1] - self.cityPositions[j][1])**2

    def get_subsets(self, nums):
        if not nums:
            return [[]]

        subsets = self.get_subsets(nums[1:])
        return subsets + [[nums[0]] + subset for subset in subsets]