def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5))

def calculate(n, **kwargs):
    print(kwargs)  # the kwargs become a disctionary with keyword arguments
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get('model')  # similar to using square brackets but it wound cause an error of this key
        # is not found in the dictionary


my_car = Car(make="Nissan", model='GT-R')
print(my_car.model)
