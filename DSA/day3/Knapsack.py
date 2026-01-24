def knapsack_frac(weights, values, capacity):
    prof_per_weight = []
    for i,j in zip(weights, values):
        prof_per_weight.append(j / i)
    items = list(zip(weights, values, prof_per_weight))
    items.sort(key=lambda x: x[2], reverse=True)
    print(items)

    total_value = 0
    max_weight = capacity
    for weight, value, ratio in items:
        if max_weight <= 0:
            break
        elif weight <= max_weight:
            total_value += value
            max_weight -= weight
        else:
            part_value = ratio * max_weight
            total_value += part_value
            max_weight = 0
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = knapsack_frac(weights, values, capacity)
print(f"Maximum value in Knapsack = {max_value}")