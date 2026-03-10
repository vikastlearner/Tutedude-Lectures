# range() - builtin function for range
# SYNTAX: range(start, stop, step): Step is number of interval. Stop is excluded
# start by default is 0
# step by default is 1

# range(1 to 10 with 1 step)
for i in range(1,11,1):
    print(i)

print("\n")
# range(1 to 10 with 2 step)
for i in range(1,11,2):
    print(i)

# Generate even number between 1 and 10
print("\n The even numbers between 1 and 10:")
for i in range(2,10,2):
    print(i)

# Print in reverse order from 20 to 10 (Excl 10)
print("\n The numbers are in reverse:")
for i in range(20,10,-1):
    print(i)
