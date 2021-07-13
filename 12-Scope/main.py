################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def game():
    def drink_potion():
        potion_strength = 2 # local scope
        print(potion_strength)
        # now drink_potion() is local to game()
# print(potion_strength) #This will not be able to be accessed because potion strength is a local scope

#Global scope
player_health = 10

def drink_potion2():
    potion_strength = 2
    print(player_health) # this is possible because player health is a global variable

drink_potion2()

# There is no Block scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
# this will print out because blocks like if while or loops, you are not creating a local Scope

# Modifying Global Scope

def increase_enemies2():
  # enemies = 2 # this becomes another variable - you are not modifying a global scope
  # print(f"enemies inside function: {enemies}")
  global enemies # this helps you modify global code
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies2()
print(f"enemies outside function: {enemies}")

# usually its not good to edit global variable in a function
# it is better to return the value and re-assign it to the global variable


#Global constants
#usually you use uppercase - reminding yourself not to modify it
PI = 3.14156
URL = "https://myportfolio.com"
NAME = "Audrey Patricia"
