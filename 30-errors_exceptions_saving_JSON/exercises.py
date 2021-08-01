fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
  make_pie(4)
except:
  print("Fruit Pie")


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


# We've got some buggy code, try running the code. The code will crash and give you a KeyError. This is because some of ' \
#   'the posts in the facebook_posts don't have any "Likes".


total_likes = 0

for post in facebook_posts:
    try:
      post['Likes']
    except KeyError:
      post['Likes'] = 0

    finally:
      total_likes = total_likes + post['Likes']

print(total_likes)