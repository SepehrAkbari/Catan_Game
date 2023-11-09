def subtract_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("List Size Error")
    result = [a - b for a, b in zip(list1, list2)]
    return result

def add_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("List Size Erro")
    result = [a + b for a, b in zip(list1, list2)]
    return result

def is_nonnegative(lst):
    return all(x >= 0 for x in lst)

def tabulate_resources(resources):
    resource_counts = []
    for resource in resources:
        count = int(input(f"How many {resource} cards do you have? "))
        resource_counts.append(count)
    return resource_counts

def vpoint_count_Catan(resource_counts):
    items = ["City", "Settlement", "Development Card", "Road"]
    resources_needed = [
        [1, 1, 3, 3, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 1, 0.25, 0.25, 0.25]
    ]
    victory_points = [2, 1, 0.75, 0.25]

    total_points = 0
    counts_to_purchase = [0] * len(items)

    for i in range(len(items)):
        while is_nonnegative(subtract_lists(resource_counts, resources_needed[i])):
            counts_to_purchase[i] += 1
            resource_counts = subtract_lists(resource_counts, resources_needed[i])

    for i in range(len(items)):
        total_points += counts_to_purchase[i] * victory_points[i]
        if counts_to_purchase[i] != 0:
            print(f"Purchase {counts_to_purchase[i]} {items[i]}")
    
    return total_points

def left_overs(resource_counts):
    items = ["City", "Settlement", "Development Card", "Road"]
    resources_needed = [
        [1, 1, 3, 3, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 1, 0.25, 0.25, 0.25]
    ]
    counts_to_purchase = [0] * len(items)

    for i in range(len(items)):
        while is_nonnegative(subtract_lists(resource_counts, resources_needed[i])):
            counts_to_purchase[i] += 1
            resource_counts = subtract_lists(resource_counts, resources_needed[i])
    
    return resource_counts

def exchange():
    """finds the points for the number of resource cards in Settlers of Catan without exchanges"""
    res_counts = [0, 0, 0, 0, 0]
    resources = ["Brick", "Wood", "Ore", "Wheat", "Sheep"]
    res_counts = tabulate_resources(resources)
    points = vpoint_count_Catan(res_counts)
    left = left_overs(res_counts)
    print("Expected points will be", points)
    print("Left over resources are...")
    for i in range(len(resources)):
        if left[i] != 0:
            print(resources[i], left[i])

if __name__ == "__main__":
    exchange()
