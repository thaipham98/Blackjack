import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


def deal(deck):
  hand = []
  for i in range(2):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11: card = "J"
    if card == 12: card = "Q"
    if card == 13: card = "K"
    if card == 14: card = "A"
    hand.append(card)
  return hand

def total(hand):
  total = 0
  for card in hand:
    if card == "J" or card == "Q" or card == "K":
      total += 10
    elif card == "A":
      if total >= 11:
        total += 1
      else:
        total += 11
    else:
      total += card
  return total


def hit(hand):
  card = deck.pop()
  if card == 11: card = "J"
  if card == 12: card = "Q"
  if card == 13: card = "K"
  if card == 14: card = "A"
  hand.append(card)
  return hand

def blackjack(dealer_hand, player_hand):
  if total(player_hand) == 21:
    print("Player wins!")
    print("Blackjack!")
  elif total(dealer_hand) == 21:
    print("Dealer wins!")
    print("Blackjack!")
    
def score(dealer_hand, player_hand):
  blackjack(dealer_hand, player_hand)
  if total(player_hand) > 21:
    print(f"Player busts with {total(player_hand)}")
    print("Dealer wins")
  elif total(dealer_hand) > 21:
    print(f"Dealer busts with {total(dealer_hand)}")
    print("Player wins")

def final_score(dealer_hand, player_hand):
  if total(player_hand) < total(dealer_hand):
    print("Dealer Wins!")
    print(
      f"{display_hand_summary(dealer_hand)} to Player's {display_hand_summary(player_hand)}"
    )
  elif total(player_hand) > total(dealer_hand):
    print("Player Wins!")
    print(
      f"{display_hand_summary(player_hand)} to Dealer's {display_hand_summary(dealer_hand)}"
    )
  else: 
    print("Draw!")


def display_hand_summary(hand):
  return f"{' '.join([str(item) for item in hand])} = {total(hand)}"


def play():
  choice = 0
  dealer_hand = deal(deck)
  player_hand = deal(deck)
  done = False

  print(f"Dealer has: {str(dealer_hand[0])} ? = ?")
  print("Player has: " + display_hand_summary(player_hand))
  blackjack(dealer_hand, player_hand)
  choice = input("Would you like to [H]it or [S]tand: ").lower()
  print()
  while not done:
    if choice == "h":
      hit(player_hand)
      print("Player has: " + display_hand_summary(player_hand))
      if total(player_hand) >= 21:
        score(dealer_hand, player_hand)
        break
      print(f"Dealer has: {str(dealer_hand[0])} ? = ?")  
    elif choice == "s":
      print("Player stands with: " + display_hand_summary(player_hand))
      print()


      print("Dealer has: " + display_hand_summary(dealer_hand))
      if total(dealer_hand) >= 21:
        score(dealer_hand, player_hand)
        break
        
      while total(dealer_hand) < 17:
        hit(dealer_hand)
        print("Dealer hits")
        print("Dealer has: " + display_hand_summary(dealer_hand))
      
      if total(dealer_hand) >= 21:
        score(dealer_hand, player_hand)
        break

      print("Dealer stands")
      print()
      done = True
    if done:
      final_score(dealer_hand, player_hand)
      break
    choice = input("Would you like to [H]it or [S]tand: ").lower()
    print()

if __name__ == "__main__":
  play()
