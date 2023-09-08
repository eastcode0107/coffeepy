class CoffeeMachine:

  def __init__(self):
    self.resources = {
        "water": 400,
        "milk": 540,
        "beans": 120,
        "cups": 9,
        "money": 550
    }

  def main(self):
    while True:
      user_choice = input("Write action (buy, fill, take, remaining, exit):\n")
      print("")
      if user_choice == "exit":
        break
      else:
        self.action(user_choice)

  def action(self, action):
    if action == "buy":
      self.buy()
    elif action == "fill":
      self.fill()
    elif action == "take":
      self.take()
    elif action == "remaining":
      self.status()

  def buy(self):
    choices = {
        "1": {
            "water": 250,
            "beans": 16,
            "cups": 1,
            "money": -4
        },
        "2": {
            "water": 350,
            "milk": 75,
            "beans": 20,
            "cups": 1,
            "money": -7
        },
        "3": {
            "water": 200,
            "milk": 100,
            "beans": 12,
            "cups": 1,
            "money": -6
        }
    }
    user_input = input(
"What do you want to buy? 1 - espresso,2 - latte, 3 - cappuccino, back - to main menu:\n"
    )
    if user_input == "back":
      return
    else:
      for resource, quantity in choices[user_input].items():
        if self.resources[resource] - quantity < 0:
          print("Sorry, not enough {}!\n".format(resource))
          return
        
      print("I have enough resources, making you a coffee!\n")
      for resource, quantity in choices[user_input].items():
        self.resources[resource] -= quantity

  def fill(self):
    self.resources["water"] += int(
        input("Write how many ml of water you want to add:\n"))
    self.resources["milk"] += int(
        input("Write how many ml of milk you want to add:\n"))
    self.resources["beans"] += int(
        input("Write how many grams of coffee beans you want to add:\n"))
    self.resources["cups"] += int(
        input("Write how many disposable cups you want to add:\n"))

  def take(self):
    print("I gave you ${}".format(self.resources['money']))
    self.resources['money'] = 0
    
  def status(self):
    print("The coffee machine has:")
    print("{} ml of water".format(self.resources['water']))
    print("{} ml of milk".format(self.resources['milk']))
    print("{} g of coffee beans".format(self.resources['beans']))
    print("{} disposable cups".format(self.resources['cups']))
    print("${} of money".format(self.resources['money']))
    print("")
    return

if __name__ == "__main__":
  CoffeeMachine().main()
