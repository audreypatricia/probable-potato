# creating a class - use pascal case for class names
# use "pass" to say that after ':' there is nothing at the moment
class User:
    # constructors specify what should happen when objects are initialised - this is done using the init function
    def __init__(self, user_id, username):
        print("new user being created") # this will be run for every object created
        self.id = user_id
        self.username = username
        self.followers = 0 # deafult attributes - all new users will get the default value of 0 for followers
        self.following = 0

    # methods
    def follow(self, user): # always have self as the first argument so it knows which object has called it
        user.followers += 1
        self.following += 1


# user_1 = User()

# adding an attribute
# doing this for all objects is error prone - to do this easily use constructors
# user_1.id = '001'
# user_1.username = "audrey"
# print(user_1.username)
#
# user_2 = User()
#
# user_2.id = '002'
# user_2.username = 'michelle'

# because of the parameters in the init contructor we need to pass in arguments to set as attributes and create objects
user_3 = User('003', 'bernice')
# print(user_3.username)
# print(user_3.followers)

user_4 = User('004', 'marchia')

user_3.follow(user_4)

print(user_3.following)
print(user_3.followers)
print(user_4.following)
print(user_4.followers)




