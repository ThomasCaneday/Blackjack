import random 

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
deck = [(card, category) for category in card_categories for card in cards_list] 

def card_value(card): 
	if card[0] in ['Jack', 'Queen', 'King']: 
		return 10
	elif card[0] == 'Ace': 
		return 11
	else: 
		return int(card[0]) 

random.shuffle(deck) 
player_card = [deck.pop(), deck.pop()] 
dealer_card = [deck.pop(), deck.pop()] 

while True: 
	player_score = sum(card_value(card) for card in player_card) 
	dealer_score = sum(card_value(card) for card in dealer_card) 
	print("Cards Player Has:", player_card) 
	print("Score Of The Player:", player_score) 
	print("First Dealer Card:", dealer_card[0], "\n") 
	choice = input('What do you want? ["hit" to request another card, "stand" to stop]: ').lower() 
	if choice == "hit": 
		new_card = deck.pop() 
		player_card.append(new_card)
	elif choice == "stand": 
		break
	else: 
		print("Invalid choice. Please try again.") 
		continue

	if player_score > 21: 
		print("Cards Dealer Has:", dealer_card) 
		print("Score Of The Dealer:", dealer_score) 
		print("Cards Player Has:", player_card) 
		print("Score Of The Player:", player_score) 
		print("Dealer wins (Player Loss Because Player Score is exceeding 21)") 
		break

while dealer_score < 17: 
	new_card = deck.pop() 
	dealer_card.append(new_card) 
	dealer_score += card_value(new_card) 

if player_score > 21:
    print("Cards Player Has:", player_card) 
    print("Score Of The Player:", player_score) 
    print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
    exit()

if dealer_score > 21: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player_card) 
	print("Score Of The Player:", player_score) 
	print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)") 
elif player_score > dealer_score: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player_card) 
	print("Score Of The Player:", player_score) 
	print("Player wins (Player Has Higher Score than Dealer)") 
elif dealer_score > player_score: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player_card) 
	print("Score Of The Player:", player_score) 
	print("Dealer wins (Dealer Has Higher Score than Player)") 
else: 
	print("Cards Dealer Has:", dealer_card) 
	print("Score Of The Dealer:", dealer_score) 
	print("Cards Player Has:", player_card) 
	print("Score Of The Player:", player_score) 
	print("It's a tie.")
