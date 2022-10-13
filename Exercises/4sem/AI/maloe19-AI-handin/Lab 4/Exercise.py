import random

p_mutation = 0.2
num_of_generations = 30


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    listOfDads = list(father)
    listOfMoms = list(mother)
    single_point = random.randint(0,2)
    while single_point<len(listOfMoms):
        listOfMoms[single_point], listOfDads[single_point] = listOfDads[single_point], listOfMoms[single_point]
        single_point += 1
    child = listOfDads
    return tuple(child)

def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    mutateIndividual = tuple([1 if random.random()>0.3 else 0 for bit in individual])
    return mutateIndividual
    #return mutation

def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """
    ordered_population = list(population)
    fitnessForPopulation = {}
    total = 0

    #the fitness of the population get added up and a dictionary with the individuals as keys and the fitness as values gets made
    for member in ordered_population:
        fitnessForPopulation[member] = (fitness_fn(member))  
        total += fitnessForPopulation[member] 
    percentageContribution = {}  
    individuals = []  

    #the dictionary from before gets sorted and the fitness persentage gets connected to the individuals as values
    for key, value in sorted(fitnessForPopulation.items(),key=lambda x: x[1],reverse=True):
        percentageContribution[key] = value / total * 100  

    #checks if there is 2 individuals found and randomly assigns a number between 0 and 100 (for the sum of the procentage)
    #the code after the else statement gets executed if the random number is either the same or smaller than tha value 
    # + if the length is not 2 or if the key havent been seen before in the list
    while not len(individuals)>=2: 
        select_individuals = random.uniform(0,sum(percentageContribution.values())) 
        if len(percentageContribution) == 2: 
            for key in percentageContribution.keys(): 
                individuals.append(key)
            return individuals
        else:  
            for key, value in percentageContribution.items():
                if select_individuals<=value and not (len(individuals) == 2): 
                   individuals.append(key)

    #this is done when 2 value have been found
    print(individuals)
    return individuals
    #return selected

def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual

    Explanation:
    enumerate(list) returns a list of pairs (position, element):

    enumerate((4, 6, 2, 8)) -> [(0, 4), (1, 6), (2, 2), (3, 8)]

    enumerate(reversed((1, 1, 0))) -> [(0, 0), (1, 1), (2, 1)]
    '''
    fitnessLevel = list(individual)
    decimalValue = int("".join(str(x) for x in fitnessLevel), 2)
    return decimalValue


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def main():
    minimal_fitness = 7

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    initial_population = {
        (1, 1, 0),
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0)
    }
    #initial_population = get_initial_population(3, 4)
    initial_population = get_initial_population(3, 4)

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))


if __name__ == '__main__':
    #pass
    main()
    #main()
