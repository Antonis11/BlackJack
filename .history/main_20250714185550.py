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

    player_hand = set()
    player_value = player(player_hand)

    computer_hand = set()
    computer_value = computer(computer_hand, player_value)


main()