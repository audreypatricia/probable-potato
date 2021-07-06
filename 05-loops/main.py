# For loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)

print(fruits) # This is not in the loop, identation is important

# For loops with ranger
for number in range(1, 10): # numbers between 1 and 10, not including 10
    print(number)

for number in range(1, 11, 3): # this changes the step to 3
    print(number) # results in 1,4,7,10

#add up 1 to 100
number = 0
for number in range(1, 101):
    total += number
print(total)
