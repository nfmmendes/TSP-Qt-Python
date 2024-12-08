import pulp as pl

class FlowModel:
    def __init__(self, city_positions):
        number_of_cities = len(city_positions)
        if len(city_positions) == 0:
            return

        self.cityPositions = city_positions

        model = pl.LpProblem("TSP With Flow")

        variable_factory = lambda i, j : pl.LpVariable("x({} , {})".format(i, j), cat = pl.LpBinary)
        x = { i: { j: variable_factory(i, j) for j in range(number_of_cities) if i !=j } for i in range(number_of_cities) }
        f = [pl.LpVariable("f({})".format(i)) for i in range(number_of_cities)]

        model += pl.lpSum(self.distance(i, j)*x[i][j] for i in x for j in x[i])

        model += f[0] == number_of_cities
        
        for i in range(number_of_cities): 
            for j in range(1, number_of_cities):
                if i != j:
                    model += f[j] <= f[i] - 1 + 2*number_of_cities*(1 - x[i][j])

        for i in range(number_of_cities):
            model += pl.lpSum( [x[i][j] for j in x[i] ] ) == 1
        
        for j in range(number_of_cities):
            model += pl.lpSum( [x[i][j] for i in range(number_of_cities) if j in x[i]]) ==\
            pl.lpSum( [x[j][i] for i in range(number_of_cities) if i in x[j]])

        model.solve()
    
    def distance(self, i, j) -> int:
        return (self.cityPositions[i][0] - self.cityPositions[j][0])**2 + (self.cityPositions[i][1] - self.cityPositions[j][1])**2
