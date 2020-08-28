def tower_builder(n_floors):
    largest_floor = (2 * n_floors) - 1
    cache = []
    for i in range(1, n_floors + 1):
        cache.append((int((largest_floor - (2*i - 1))/2) * " ") 
                     + ((2*i - 1) * "*") 
                     + (int((largest_floor - (2*i - 1))/2) * " "))
    return cache