import random
from OrganismGenerator import generate_organism
def OrganismMatchup(population):
    population=list(population.values())
    organism_1=random.choice(population)
    population.remove(organism_1)
    organism_2=random.choice(population)
    population.remove(organism_2)
    pair=[organism_1, organism_2]
    return population,pair

population={}

for i in range (5):
    population[i]=generate_organism()


print(OrganismMatchup(population))