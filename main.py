import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10, 10]

class Player():
    def __init__(self, name):
        self.name = name
        self.card = []
player = Player('Player')
dealer = Player('dealer')

def draw_card(): 
    return random.choice(CARDS)

def count_score(card):
    total = 0
    for i in card:
        total += i
    return total

def check_dealer(dealer):
    if count_score(dealer) < 17:
        return True
    else:
        return False

    
def winner(player, dealer):
    player_total = count_score(player)
    dealer_total = count_score(dealer)
    if player_total <=21 and player_total > dealer_total or dealer_total > 21:
        print(f"\n[SYSTEM] Your cards: {player}\n[SYSTEM] Dealer cards: {dealer}")
        print(f"[SYSTEM] Your score: {count_score(player)}\n[SYSTEM] Dealer's score: {count_score(dealer)}\n")
        print(f"[SYSTEM] You've won! Congratualations! \n")
        

    elif dealer_total <= 21 and dealer_total > player_total or player_total > 21:
        print(f"\n[SYSTEM] Your cards: {player}\n[SYSTEM] Dealer cards: {dealer}")
        print(f"[SYSTEM] Your score: {count_score(player)}\n[SYSTEM] Dealer's score: {count_score(dealer)}\n")
        print("[SYSTEM] You've lost! Dealer wins\n")
    return True
    


def game(player, dealer): 

    print (f"\n[SYSTEM] Your cards: {player} current score: {count_score(player)}")
    print (f"\n[SYSTEM] Dealer's first card: {dealer[0]}")
    print() 


is_game = True
    
while is_game:
    choice = input("\n > Do you want to play blackjack? y or n: ").lower()
    if choice == 'y':
        for i in range(0,2):
                player.card.append(draw_card())
                dealer.card.append(draw_card())
        if check_dealer(dealer.card):
            dealer.card.append(draw_card())
        game(player.card, dealer.card)
        choice1 = input(f"\n > Do you want to add another card? y/n: ").lower()
        if choice1 == "y":
            player.card.append(draw_card())
            if winner(player.card, dealer.card):
                dealer.card, player.card = [], []
            
        elif choice1 == "n":
            if winner(player.card, dealer.card):
                dealer.card, player.card = [], []
            
    elif choice == 'n':
        print(f'\nThank you for playing the game\n')
        break
    else:

        print(f'\nPlease enter "y" for yes or "n" for no\n')
            

