import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#play = input("Do you want to play a game of Blackjack? Type y' or 'n':").lower()
#if play == "y":
#    print("\n" * 20)
#else: 
#    print("You are missing out!")

def deal_card():
    random_card = random.choice(cards)
    return random_card

#Fucntion to calculate the total score
def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
        
    total = 0
    for score in list:
        total += score
    return total    

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "You lose!"
    elif u_score == 0:
        return "You win!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and current score {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
            if more_cards == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()