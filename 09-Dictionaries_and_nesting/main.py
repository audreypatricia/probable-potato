# Dictionaries in python is like object in javascript
# syntax => {Key: , Value: }
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# keys are strings or numbers - and so you need "" or use a data variable

# retrieve an item - keys need to be typed correctly
programming_dictionary["Bug"]
print(programming_dictionary["Bug"])

# adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# you can create an empty dictionary and add to it later
empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}

#edit an item in the dictionary
programming_dictionary["Bug"] = "This is changed"
#if it cannot find that key then it will just create a new key value pair

# loop through a dictionary
# doing
# for thing in programming_dictionary - "thing" will be the keys

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])



# Nesting
# you can nest lists and dictionaries together

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuggart"],
}

# nesting dictionary in dictionary
travel_log = {
    "France": { "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12 },
    "Germany": ["Berlin", "Hamburg", "Stuggart"],
}

# nesting dictionaries in lists

travel_log = [
    {
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country" : "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuggart"],
        "total_visits" : 5,
    },
]
