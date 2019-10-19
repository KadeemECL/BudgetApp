print("Welcome to the simple budget app!")

name = input("Let's get started with your name. ")

cost = input("Ok %s, how much is the item you want to buy? " % name)

income = input("Great %s, and how much money do you have? " % name)

if cost > income:
    print("You do not have enough money \n")
else:
    print("You have enough money!")

print("This may seem very childish and simple, but you would be surprised"
      "by how many people struggle with this.")

print("Anyways, thanks for using this. Come back soon!")