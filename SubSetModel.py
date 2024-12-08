import pulp as pl

class SubSetModel():
    def __init__(self, city_positions):
        numberOfCities = len(city_positions)
        if len(city_positions) == 0:
            return

        self.cityPositions = city_positions

        self.subsets =  self.get_subsets([i for i in range(numberOfCities)])
        
        model = pl.LpProblem("TSP With subsets")

        variable_factory = lambda i, j : pl.LpVariable("x({} , {})".format(i, j), cat = pl.LpBinary)
        x = { i: { j: variable_factory(i, j) for j in range(numberOfCities) if i !=j } for i in range(numberOfCities) }

        model += pl.lpSum(self.distance(i, j)*x[i][j] for i in x for j in x[i])

        for i in range(numberOfCities):
            model += pl.lpSum( [x[i][j] for j in x[i] ] ) == 1
        
        for j in range(numberOfCities):
            model += pl.lpSum( [x[i][j] for i in range(numberOfCities) if j in x[i]]) ==\
            pl.lpSum( [x[j][i] for i in range(numberOfCities) if i in x[j]])

        for subset in self.subsets:
            if len(subset) <= 1 or len(subset) == numberOfCities:
                continue
            model += pl.lpSum( [x[i][j] for i in x for j in x[i] if i in subset and j in subset] ) <= len(subset) - 1

        print(model)
        model.solve()
        self.solution_status = pl.LpStatus[model.status]
    
    def distance(self, i, j) -> int:
        return (self.cityPositions[i][0] - self.cityPositions[j][0])**2 + (self.cityPositions[i][1] - self.cityPositions[j][1])**2

    def get_subsets(self, nums):
        if not nums:
            return [[]]

        subsets = self.get_subsets(nums[1:])
        return subsets + [[nums[0]] + subset for subset in subsets]