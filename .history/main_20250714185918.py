from random import seed
from datetime import datetime

number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
kind = {"heart", "diamond", "spade", "club"}

deck = set()

def hand_value(hand):
    value = 0
    ace = False
    for card in hand:
        if( card[0] == "jack" or card[0] == "queen" or card[0] == "king" ):
            value += 10
        elif(card[0] == "ace"):
            ace = True
            value += 1
        else:
            value += card[0]

    if ace and value + 10 <= 21:
        value += 10
    
    return value

def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())
    
    value = hand_value(hand)
    print(f"Player value: {value}")
    if (value >= 21):
        return value
    
    while True:
        choice = input("Hit-h or Stand-s: ")
        if (choice == "h"):
            hand.add(deck.pop())
            value = hand_value(hand)
            print(hand)
            print(f"Player value: {value}")
            if (value >= 21):
                return value
        elif (choice == "s"):
            return hand_value(hand)
        
def computer(hand, player_value):
    hand.add(deck.pop())
    hand.add(deck.pop())
    
    value = hand_value(hand)

    while True:
        if value >= 21:
            print(hand)
            print(f"Computer value: {value}")
            return value
        elif value >= player_value:
            print(hand)
            print(f"Computer value: {value}")
            return value
        else:
            hand.add(deck.pop())
            value = hand_value(hand)

def main():
    global deck

    seed(datetime.now().timestamp())

    deck = {(n,k) for n in number for k in kind}

    rounds = 1
    score = [0,0]

    while True:
        print(f"===== Round:{rounds} =====")
        player_hand = set()
        player_value = player(player_hand)

        if (player_value > 21):
                print("Player lose!")
                score[1] += 1
        elif (player_value == 21):
                print("Player win!")
                score[0] += 1
        else:
            computer_hand = set()
            computer_value = computer(computer_hand, player_value)
            if (computer_value > 21):
                print("Computer lose!")
                score[0] += 1
            elif(player_value > computer_value):
                print("Player win!")
                score[0] += 1
            else:
                print("Computer win!")
                score[1] += 1
            
        print(f"\nScore:\nPlayer: {score[0]} - Computer: {score[1]}")

        while True:
            choice = input("Do you want to continue (Yes-y or No-n):\n")
            if choice == "y":
                rounds += 1
                break
            elif choice == "n":
                print("Bye bye!!!")
                return
            else:
                print("Invalid input, please enter 'y' or 'n'.")


main()