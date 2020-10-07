import random
deck = [[1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [2, 6], [2, 7], [2, 8], [2, 9],
        [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13],
        [3, 14], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14]]
p1_deck = []
p2_deck = []
random.shuffle(deck)
get_one = 1
card = 0
total_1 = 0
total_2 = 0

def next_card():
        global card
        card += 1

def get_value(rang, total):
        if rang in range(6, 11):
                return rang
        elif rang in range(11, 14):
                return 10
        elif rang == 14:
                if total <= 10:
                        return 11
                else:
                        return 1


def calculate_scores_1(deck):
        global total_1
        for c in deck:
                total_1 += get_value(c[1], total_1)


p1_deck.append(deck[card])
next_card()
p1_deck.append(deck[card])
next_card()
calculate_scores_1(p1_deck)
if total_1 <= 21:
        print("у вас - ", total_1)
        print("берете еще карту?")
        get_one = int(input())
else:
        print("вы проиграли")
while get_one > 0:
        p1_deck.append(deck[card])
        next_card()
        if total_1 <= 21:
                print("у вас - ", total_1)
                print("берете еще карту?")
                get_one = int(input())
        else:
                print("вы проиграли")
