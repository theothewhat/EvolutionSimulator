from OrganismGenerator import generate_organism
from OrganismFight import OrganismDecider

## file where organisms are generated and handled. They are meant to be sent off to other files/ functions to preform the calculations of actions such as death and reproduction




def main():
    resources=3
    population={}
    for i in range(5):
        population[i]=(generate_organism())

    
    


