from random import seed
from datetime import datetime

number = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"}
kind = {"heart", "diamond", "spade", "club"}

deck = set()

def main():
    global deck

    seed(datetime.now().timestamp())

    deck = {(n,k) for n in number for k in kind}


main()