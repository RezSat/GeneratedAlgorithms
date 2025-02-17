import random

def genetic_algorithm_equation(target, population_size, generations):
    # Initialize the population with random solutions
    population = []
    for _ in range(population_size):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        population.append((x, y))

    def calculate_fitness(chromosome):
        # Fitness is the absolute difference between x + y and the target
        x, y = chromosome
        return abs(x + y - target)

    def selection(population):
        # Select the best chromosomes based on fitness (lower fitness is better)
        ranked_population = sorted(population, key=calculate_fitness)
        return ranked_population[:population_size // 2]  # Select top 50%

    def crossover(parent1, parent2):
        # Create offspring by combining the genetic material of the parents
        x1, y1 = parent1
        x2, y2 = parent2
        child1 = (x1, y2)
        child2 = (x2, y1)
        return child1, child2

    def mutation(chromosome):
        # Introduce random mutations
        x, y = chromosome
        if random.random() < 0.1:  # 10% chance of mutation
            x += random.randint(-5, 5)
        if random.random() < 0.1:
            y += random.randint(-5, 5)
        return (x, y)

    for _ in range(generations):
        # Evaluate fitness
        fitnesses = [calculate_fitness(chromosome) for chromosome in population]

        # Check if a solution is found
        if 0 in fitnesses:
            best_index = fitnesses.index(0)
            return population[best_index]

        # Selection
        parents = selection(population)

        # Crossover and Mutation
        offspring = []
        while len(offspring) < population_size:
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child1, child2 = crossover(parent1, parent2)
            offspring.append(mutation(child1))
            offspring.append(mutation(child2))

        # Replace the old population with the new population
        population = offspring[:population_size]

    return None  # No solution found

# Example usage:
# solution = genetic_algorithm_equation(50, 100, 1000)
# if solution:
#     print(f"Solution found: x = {solution[0]}, y = {solution[1]}")
# else:
#     print("No solution found")
