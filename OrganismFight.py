import random
from OrganismGenerator import generate_organism
def OrganismMatchup(population):
    unused=list(population.items())
    organism_1=random.choice(unused)
    unused.remove(organism_1)
    organism_2=random.choice(unused)
    unused.remove(organism_2)
    print(unused)
    pair={organism_1, organism_2}
    print(pair)

population={}

for i in range (5):
    population[i]=generate_organism()
print(population)

OrganismMatchup(population)