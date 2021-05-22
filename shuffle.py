import random


cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]
            
            
def shuffle_card(how_many_cards, *players):
	random.shuffle(cardList)
	if how_many_cards * len(players) > len(cardList):
		print("Mamy za mało kart!")
		return
	else:
		for player in players:
			container = []
			for shuffle in range(how_many_cards):
				card = cardList.pop()
				container.extend([card])
			print("Karty gracza", ":", container)


print("""Rozpiska: 
1. Aby zakończyć
""")

while True:
	menu = input("Podaj co chcesz zrobić, jeśli chcesz przejść dalej kliknij enter, jeśli chcesz zakończyc wpisz 1.")
	if menu == "1":
		break
	howManyCards = int(input("Podaj ile kart mam rozdać graczą: "))
	howManyPlayers = int(input("Wpisz ile chcesz graczy: "))
	for player in range(1, howManyPlayers + 1):
		shuffle_card(howManyCards, player)
