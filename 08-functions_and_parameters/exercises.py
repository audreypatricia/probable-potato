## Area Calc
# # Instructions
#
# You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
#
# number of cans = (2 ✖️ 4) ÷ 5
#
#                          = 1.6
#
# But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans.
import math

def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width) / cover)
  print(f"You'll need {number_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


## Prime Numbers

# Instructions

# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# **You need to write a function** that checks whether if the number passed into it is a prime number or not.

def prime_checker(number):
  isPrime = True
  for i in range(2, number):
    if number % i == 0:
      print(i)
      isPrime = False

  if(isPrime):
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
