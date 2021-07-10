# need a clear function each time a bid is created
import art

print(art.logo)
print("Welcome to the secret auction program.")

def ask_questions():
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  keep_running = input("Are there any other bidders? Type 'yes' or 'no'. ")
  return [name, bid, keep_running]

# ask_questions()
run_program = True
bidding = {}
max_bid = 0
highest_bidder = ""

while run_program == True:
  results = ask_questions()
  print(results)
  bidding[results[0]] = results[1]
  if results[2] == 'yes':
    run_program = True
  else:
    run_program = False
    for bidder in bidding:
      bid_amount = int(bidding[bidder])
      if bid_amount > int(max_bid):
        max_bid = bidding[bidder]
        highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${max_bid}")
