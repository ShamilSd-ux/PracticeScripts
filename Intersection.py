def find_intersection(L1, L2):
    # Convert lists to sets and find the intersection
    return list(set(L1) & set(L2))

# Example lists
L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7, 8]

# Finding the intersection
intersection = find_intersection(L1, L2)
print(intersection)  # Outputs: [4, 5]
