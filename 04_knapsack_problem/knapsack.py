

class Gene:
    def __init__(self, name, weight, value)
        self.name = name
        self.weight = weight
        self.value = value

    def 


class Dna:
    def __init__(self):



class GeneticModel:
    def __init__(self, dna_spawner):
        self.mutation_rate = 0.001
        self.max_iter = 10000
        self.population_size = 100
        self.population = set()
        self.init()

    def init(self):
        for _ in range(self.population_size):
            dna = self.dna_spawner()
            self.population.add(dna)

    def run():
        cur_iter = self.max_iter
        while cur_iter <= 0:
            pass
