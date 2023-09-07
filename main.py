import sys

# Coffee Mach State
mach_water = 400
mach_milk = 540
mach_beans = 120
mach_cups = 9
mach_money = 550

def buy(mach_water, mach_milk, mach_beans, mach_cups, mach_money):
  print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
  choice = input()
  print("")
  if choice == "1":  
    water_need = 250
    beans_need = 16
    if mach_water >= water_need and mach_beans >= beans_need and mach_cups >= 1:
      mach_water -= water_need
      mach_beans -= beans_need
      mach_cups -= 1
      mach_money += 4
      print("I have enough resources, making you a coffee!")
      action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
    elif mach_water < water_need:
      print("Sorry, not enough water!")
    elif mach_beans < beans_need:
      print("Sorry, not enough beans!")
    elif mach_cups < 1:
      print("Sorry, not enough cups!")
    print("")
    action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
  if choice == "2":
    water_need = 350
    milk_need = 75
    beans_need = 20
    if (mach_water >= water_need and mach_milk >= milk_need
        and mach_beans >= beans_need and mach_cups >= 1):
      mach_water -= water_need
      mach_milk -= milk_need
      mach_beans -= beans_need
      mach_cups -= 1
      mach_money += 7
      print("I have enough resources, making you a coffee!")
      action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
    elif mach_water < water_need:
      print("Sorry, not enough water!")
    elif mach_milk < milk_need:
      print("Sorry, not enough milk!")
    elif mach_beans < beans_need:
      print("Sorry, not enough beans!")
    elif mach_cups < 1:
      print("Sorry, not enough cups!")
    print("")
    action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
  if choice == "3":
    water_need = 200
    milk_need = 100
    beans_need = 12
    if (mach_water >= water_need and mach_milk >= milk_need
        and mach_beans >= beans_need and mach_cups >= 1):
      mach_water -= water_need
      mach_milk -= milk_need
      mach_beans -= beans_need
      mach_cups -= 1
      mach_money += 6
      print("I have enough resources, making you a coffee!")
      action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
    elif mach_water < water_need:
      print("Sorry, not enough water!")
    elif mach_milk < milk_need:
      print("Sorry, not enough milk!")
    elif mach_beans < beans_need:
      print("Sorry, not enough beans!")
    elif mach_cups < 1:
      print("Sorry, not enough cups!")
    print("")
    action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
  if choice == "back":
    print("")
    action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
    
def fill(mach_water, mach_milk, mach_beans, mach_cups, mach_money):
  print("Write how many ml of water you want to add: ")
  add_water = int(input())
  mach_water += add_water
  print("Write how many ml of milk you want to add: ")
  add_milk = int(input())
  mach_milk += add_milk
  print("Write how many grams of coffee beans you want to add")
  add_beans = int(input())
  mach_beans += add_beans
  print("Write how many disposable cups you want to add: ")
  add_cups = int(input())
  mach_cups += add_cups
  print("")
  action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

def take(mach_water, mach_milk, mach_beans, mach_cups, mach_money):
  print("I gave you ${}".format(mach_money))
  mach_money = 0
  print("")
  action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

def status(mach_water, mach_milk, mach_beans, mach_cups, mach_money):
  print("The coffee machine has:")
  print("{} ml of water".format(mach_water))
  print("{} ml of milk".format(mach_milk))
  print("{} g of coffee beans".format(mach_beans))
  print("{} disposable cups".format(mach_cups))
  print("${} of money".format(mach_money))
  print("")
  action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

def action(mach_water, mach_milk, mach_beans, mach_cups, mach_money):
  print("Write action (buy, fill, take, remaining, exit): ")
  action = input()
  if action == "buy":
    buy(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

  elif action == "fill":
    fill(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

  elif action == "take":
    take(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

  elif action == "remaining":
    status(mach_water, mach_milk, mach_beans, mach_cups, mach_money)
    
  elif action == "exit":
    sys.exit()

def main():
  # Start
  action(mach_water, mach_milk, mach_beans, mach_cups, mach_money)

if __name__ == "__main__":
  main()
