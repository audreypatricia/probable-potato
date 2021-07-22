class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe() # call on the super class methods 'breathe'
        print("doing this underwater") # then modify the function and do something else

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()  # this is possible because we inherit from the Animal class
print(nemo.num_eyes)  # I can also access the attributes from the super class

# Slice method
arr = [1, 2, 3, 4, 5, 6, 7]
print(arr[2:5])  # you will get 3,4,5
print(arr[2:])  # emitting the last value means you get
# everything after the position 2
print(arr[:5])  # this means you get everything up to pos 5
print(arr[2:5:2])  # the third argument provides the step
# you will get [2,5]
print(arr[::2])  # go from beg to end in steps of 2
# get [1,3,5,7]
print(arr[::-1])  # reverse the list, increments are by -1
# get [7,6,5,4,3,2,1]

# also works with tuples
piano_tuple = ("do", "re", "mi", "fa", "sol", "la", "si")
print(piano_tuple[2:5])
