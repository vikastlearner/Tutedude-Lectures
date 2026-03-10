scores = [2,17,19,77,0,100,121,0,1]

# Sum of the scores using loop and sum()
total = 0
for score in scores:
    total += score
print(f"Sum using for loop: {total}")
print("Sum using for sum function: ", sum(scores))
print("\n")

# Maximum scores using loop and max()
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
print(f"Highest score using for loop: {highest}")
print("Highest score using for max function: ", max(scores))
print("\n")

# Minimum scores using loop and min()
lowest = scores[0]
for score in scores:
    if score < lowest:
        lowest = score
print(f"Lowest score using for loop: {lowest}")
print("Lowest score using for min function: ", min(scores))

