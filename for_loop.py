# For loop with string
s1 = "Hello World"
for char in s1:
    print(char)
print("End of FOR loop with String\n\n")

# For loop with dictionary
emp = {'empid':1000,'name':"Vikas Tiwari",'department':"TS"}
for i in emp:
    print(f"{i}: {emp[i]}") #Here 'i' represents Key and emp[i] represent value.

# Using items
print(emp.items())
for j in emp.items():
    print(j)
    print(j[0], j[1])
print("End of dictionary-for loop\n\n")

