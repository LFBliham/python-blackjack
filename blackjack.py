# Importing required modules
import random
import matplotlib.pyplot as plt
import csv

# Simulation Mode
def simulation():
  # Initializing variables
  def deal_card():
    # Deal a card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  
  def compare(computer1_score, computer2_score):
    # Comparing scores
    if computer1_score > 21 and computer2_score > 21:
      return "Draw"
    
    if computer1_score == computer2_score:
      return "Draw"
    elif computer2_score == 0:
      return "C2 Win"
    elif computer1_score == 0:
      return "C1 Win"
    elif computer1_score > 21:
      return "C2 Win"
    elif computer2_score > 21:
      return "C1 Win"
    elif computer1_score > computer2_score:
      return "C1 Win"
    else:
      return "C2 Win"

  # Function that plays the game in its entirety    
  def play_game():
    computer1_cards = []
    computer2_cards = []
    is_game_over = False
    for _ in range(2):
      computer1_cards.append(deal_card())
      computer2_cards.append(deal_card())
    while not is_game_over:
      computer1_score = calculate_score(computer1_cards)
      computer2_score = calculate_score(computer2_cards)
      print(f"   Computer 1's cards: {computer1_cards}, current score: {computer1_score}")
      print(f"   Computer 2's first card: {computer2_cards[0]}")

      if computer1_score == 0 or computer2_score == 0 or computer1_score > 21:
        is_game_over = True
      else:
        # Strategy for computer 1
        if computer1_score < 16:
          computer1_cards.append(deal_card())
          computer1_score = calculate_score(computer1_cards)
          print("Computer 1 drew another card.")
        else:
          print("Computer 1 chose to pass.")
        # Stratagey for computer 2  
        if computer2_score < stand_number:
          computer2_cards.append(deal_card())
          computer2_score = calculate_score(computer2_cards)
          print("Computer 2 drew another card.")
        else:
          print("Computer 2 chose to pass.")
  
        if computer1_score >= 16 and computer2_score >= stand_number:
          is_game_over = True

    # Printing results
    print(f"   Computer 1's final hand: {computer1_cards}, final score: {computer1_score}")
    print(f"   Computer 2's final hand: {computer2_cards}, final score: {computer2_score}")
    winner = compare(computer1_score, computer2_score)
    print (winner) 
    
    # Preparing csv file 17
    if csv17 == True:
      roundstatsSIM = ["SIM17", computer1_score, computer2_score, winner]
      file = open("Game_scores17.csv", "a", newline='')
      db = csv.writer(file)
      db.writerow(roundstatsSIM)
      file.close()
  
      file = open("Game_scores17.csv","r")
      records = list(csv.reader(file))
      file.close()
       
      C1_score = []
      C2_score = []
      sim_winner = []
      for record in records[1:]:
        C1_score.append(record[1])
        C2_score.append(record[2])
        sim_winner.append(record[3])
      
       
      # Counting how many times each player won or drew
      frequencyofwins17 = []
      frequencyofwins17.append(sim_winner.count("C1 Win"))
      frequencyofwins17.append(sim_winner.count("C2 Win"))
      frequencyofwins17.append(sim_winner.count("Draw"))
      print("Number of Wins:", frequencyofwins17)
      
      # Determining % computer 2 won because computer 2 is acting as the house 
      percentage_of_times_C2_won17 = (frequencyofwins17[1]/sum(frequencyofwins17)) * 100
      percentage_of_times_C2_won17 = round(percentage_of_times_C2_won17, 2)
      print("Computer 2 is now winning", percentage_of_times_C2_won17, "% of the time")
      print()
      print("--------------------------------------------------")
      print()
      
    # Preparing csv file 18
    elif csv18 == True:
      roundstatsSIM = ["SIM18", computer1_score, computer2_score, winner]
      file = open("Game_scores18.csv", "a", newline='')
      db = csv.writer(file)
      db.writerow(roundstatsSIM)
      file.close()
  
      file = open("Game_scores18.csv","r")
      records = list(csv.reader(file))
      file.close()
  
      C1_score = []
      C2_score = []
      sim_winner = []
      for record in records[1:]:
        C1_score.append(record[1])
        C2_score.append(record[2])
        sim_winner.append(record[3])
    
      # Counting how many times each player won or drew
      frequencyofwins18 = []
      frequencyofwins18.append(sim_winner.count("C1 Win"))
      frequencyofwins18.append(sim_winner.count("C2 Win"))
      frequencyofwins18.append(sim_winner.count("Draw"))
      print("Number of Wins:", frequencyofwins18)

      # Determining % computer 2 won because computer 2 is acting as the house 
      percentage_of_times_C2_won18 = (frequencyofwins18[1]/sum(frequencyofwins18)) * 100
      percentage_of_times_C2_won18 = round(percentage_of_times_C2_won18, 2)
      print("Computer 2 is now winning", percentage_of_times_C2_won18, "% of the time")
      print()
      print("--------------------------------------------------")
      print()

    # Run simulation for Computer 2 standing on 17 and Computer 1 standing on 16
    if choice == "y" and stand_number == 17:
      # (Bar Graph) Plotting the results when computer 2 stands on 17 and computer 1 stands on 16
      plt.figure(figsize=(100,100))
      plt.bar(["Computer 1 Wins","Computer 2 Wins","Draws"], frequencyofwins17)
      plt.grid(color = "grey", linestyle = "--", linewidth = 2, axis = "y", alpha = 0.5)
      plt.ylabel("Frequency of Wins")
      plt.xlabel("Player's Wins")
      plt.yticks(range(0, max(frequencyofwins17)+10, 10))
      plt.title("How many times each computer won or drew when the house (computer 2) has to stand on 17 and when computer 1 (the user) has to stand on 16")
      plt.savefig("Sim17")
      plt.close()
      
      # (Pie Chart) Plotting the results when computer 2 stands on 17 and computer 1 stands on 16
      plt.figure(figsize=(15,15))
      plt.pie(frequencyofwins17, labels=["Computer 1 Wins","Computer 2 Wins","Draws"], autopct="%0.2f%%", startangle=90)
      plt.title("How many times each computer won or drew when the house (computer 2) has to stand on 17 and when computer 1 (the user) has to stand on 16")
      plt.savefig("Sim17_Pie_Chart")
      plt.close()
      
    # Run simulation for Computer 2 standing on 18 and Computer 1 standing on 16  
    elif choice == "y" and stand_number == 18:
      # (Pie Chart) Plotting the results when computer 2 stands on 18 and computer 1 stands on 16
      plt.figure(figsize=(15,15))
      plt.pie(frequencyofwins18, labels=["Computer 1 Wins","Computer 2 Wins","Draws"], autopct="%0.2f%%", startangle=90)
      plt.title("How many times each computer won or drew when the house (computer 2) has to stand on 18 and when computer 1 (the user) has to stand on 16")
      plt.savefig("Sim18")
      plt.close()
      
  # Looping the entire game 100 times  
  i = 0
  while i < 100:
    print()
    print("Do you want to play a game of blackjack? Type 'y' or 'n': y")
    play_game()
    i  += 1 

###################################################
    
# Multiplayer Mode
def multiplayer():
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)

  def compare(user1_score, user2_score):
    if user1_score > 21 and user2_score > 21:
      return "Draw"

    if user1_score == user2_score:
      return "Draw"
    elif user1_score == 0:
      return "U1 Win"
    elif user2_score == 0:
      return "U2 Win"
    elif user1_score > 21:
      return "U2 Win"
    elif user2_score > 21:
      return "U1 Win"
    elif user1_score > user2_score:
      return "U1 Win"
    else:
      return "U2 Win"  

  def play_game():
    user1_cards = []
    user2_cards = []
    is_game_over = False
    for _ in range(2):
      user1_cards.append(deal_card())
      user2_cards.append(deal_card())
    while not is_game_over:
      user1_score = calculate_score(user1_cards)
      user2_score = calculate_score(user2_cards)
      print(f"   User 1 cards: {user1_cards}, current score: {user1_score}")
      print(f"   User 2 cards: {user2_cards}, current score: {user2_score}")
      if user1_score == 0 or user2_score == 0 or user1_score > 21 or user2_score > 21:
        is_game_over = True
      else:
        user_should_deal = input("User 1: Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal.lower() == "y":
          user1_cards.append(deal_card())
        else:
          user_should_deal = input("User 2: Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal.lower() == "y":
            user2_cards.append(deal_card())
          else:
            is_game_over = True

    print(f"   User 1 final hand: {user1_cards}, final score: {calculate_score(user1_cards)}")
    print(f"   User 2 final hand: {user2_cards}, final score: {calculate_score(user2_cards)}")

    user1_score = calculate_score(user1_cards)
    user2_score = calculate_score(user2_cards)
    winner = compare(user1_score, user2_score)
    print (winner)
    multiplayer()
    
    roundstatsM = ["MP", user1_score, user2_score, winner]
    file= open("Game_scores.csv", "a", newline='')
    db = csv.writer(file)
    db.writerow(roundstatsM)
    file.close()

    file = open("Game_scores.csv","r")
    records = list(csv.reader(file))
    file.close()

    First_score = []
    Second_score = []
    winner = []
    for record in records[1:]:
      First_score.append(record[1])
      Second_score.append(record[2])
      winner.append(record[3])


    # Counting how many times each player won or drew
    frequencyofwinsM = []
    frequencyofwinsM.append(winner.count("U1 Win"))
    frequencyofwinsM.append(winner.count("U2 Win"))
    frequencyofwinsM.append(winner.count("Draw"))
      
    plt.figure(figsize=(15,15))
    plt.bar(["User 1 Wins","User 2 Wins","Draws"], frequencyofwinsM)
    plt.grid(color = "grey", linestyle = "--", linewidth = 2, axis = "y", alpha = 0.5)
    plt.ylabel("Frequency of Wins")
    plt.xlabel("Player's Wins")
    plt.yticks(range(0, max(frequencyofwinsM)+10, 10))
    plt.title("How many times each player won or drew")
    plt.savefig("Multiplayer")
    
  while True:
    mode_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if mode_game.lower() == "y":
      play_game()
    elif mode_game.lower() == "n":
      print ("That's ok, come back next time")
      exit_game = input ("Exit Game? (y/n): ")
      if exit_game == "y":
        break
      elif exit_game == "n":
        continue
      break
    else:
      print("Invalid input")
      continue
    break

###################################################

# Singleplayer Mode
def singleplayer():
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)

  def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
      return "Draw"

    if user_score == computer_score:
      return "Draw"
    elif computer_score == 0:
      return "C Win"
    elif user_score == 0:
      return "U Win"
    elif user_score > 21:
      return "C Win"
    elif computer_score > 21:
      return "U Win"
    elif user_score > computer_score:
      return "U Win"
    else:
      return "C Win"  

  def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    while not is_game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"   Your cards: {user_cards}, current score: {user_score}")
      print(f"   Computer's first card: {computer_cards[0]}")
      if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
      else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal.lower() == "y":
          user_cards.append(deal_card())
          continue
        elif user_should_deal.lower() == "n":
          is_game_over = True
        else:
          print("Invalid input")
          continue
        break
        
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
      
    user_score = calculate_score(user_cards)  
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    winner = compare(user_score, computer_score)
    print (winner)
    singleplayer()

    roundstats = ["SP", user_score, computer_score, winner]
    file = open("Game_scores.csv", "a", newline='')
    db = csv.writer(file)
    db.writerow(roundstats)
    file.close()

    file = open("Game_scores.csv","r")
    records = list(csv.reader(file))
    file.close()

    First_score = []
    Second_score = []
    winner = []
    for record in records[1:]:
      First_score.append(record[1])
      Second_score.append(record[2])
      winner.append(record[3])
  
  while True:
    mode_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if mode_game.lower() == "y":
      play_game()
    elif mode_game.lower()== "n":
      print ("That's ok, come back next time")
      exit_game = input ("Exit Game? (y/n): ")
      if exit_game == "y":
        break
      elif exit_game == "n":
        continue
      break
    else:
      print("Invalid input")
      continue
    break

    
while True:
  play_type = input("Type S for singleplayer, M for multi, SIM for simulation: ")
  if play_type.upper() == "S":
    singleplayer()
  elif play_type.upper() == "M":
    multiplayer()
  elif play_type.upper() == "SIM":
    # Prompt user for their choice of simulation
    while True:
      csv17 = False
      csv18 = False
      stand_number = input("Between the numbers 17 and 18 inclusive, what number would you like computer 2 to stand on?")
      if stand_number == ("17"):
        csv17 = True
        stand_number = 17
      elif stand_number == ("18"):
        csv18 = True
        stand_number = 18
      else:
        print("Invalid input")
        continue
      break
    while True:
      choice = input("Would you like to run the simulation of the graphs? (y/n)").lower()
      if choice == "y":
        simulation()
      elif choice == "n":
        csv17 and csv18 == False
        simulation()
      else:
        print("Invalid Input")
        continue
      break
  else:
    print ("Invalid Input")
    continue
  break
