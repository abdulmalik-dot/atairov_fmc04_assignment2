def classify(value):
    if value < 498:
        return "Below range"
    elif value <= 502:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    return total / count


num_bags = int(input("Enter the number of rice bags: "))

total = 0
below = 0
in_range = 0
above = 0

for i in range(num_bags):
    weight = int(input("Enter the rice bag weight: "))
    result = classify(weight)
    print(result)

    total += weight

    if result == "Below range":
        below += 1
    elif result == "In range":
        in_range += 1
    else:
        above += 1

average = calculate_average(total, num_bags)

print(f"Total weight: {total} g")
print(f"Average weight: {average} g")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")