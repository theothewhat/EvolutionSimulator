import random 


def generate_organism():
    ## initial organism generator and population maker
    last_names=["Lowrey","Cartman","Crude","Bine","Murray","Williams"]
    colour=["Green","Blue","Red","Pink","Grey","Yellow","Black"]
    traits=["Strong","Fast","Fruitful"]

    trait_amount=random.randint(0,len(traits))

    chosen_traits=[]
    for i in range(trait_amount):
        singular_trait=random.choice(traits)
        traits.remove(singular_trait)
        chosen_traits.append(singular_trait)

    organism={"Last name": random.choice(last_names),
              "Colour": random.choice(colour),
              "Traits": chosen_traits}


    return organism




print(generate_organism())