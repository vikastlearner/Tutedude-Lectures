# Continue: Skip the rest of the current iteration and move to the next iteration.
# Break: Exit the loop completely

# Continue
print("Continue")
for num in range(10):
    if num % 3 == 0:
        continue
    print(num)

# Break
print("\nBreak")
for a in range(1,10):
    if a % 3 == 0:
        break
    print(a)