import random

cardsToBack = []
counter = 0
cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]
            
random.shuffle(cardList)
def shuffle_card(how_many_cards, *players):
	global counter
	if how_many_cards * len(players) > len(cardList):
		print("Mamy za mało kart!")
		return
	else:
		counter += 1
		for player in players:
			container = []
			for shuffle in range(how_many_cards):
				card = cardList.pop()
				container.append(card)
				cardsToBack.append(card)
			print("Karty gracza", counter, ":", container)
				

print("Rozpiska: \n1. Aby zakończyć")

while True:
	try:
		menu = input("Podaj co chcesz zrobić, jeśli chcesz przejść dalej kliknij enter, jeśli chcesz zakończyc wpisz 1.")
		if menu == "1":
			break
		howManyCards = int(input("Podaj ile kart mam rozdać graczą: "))
		howManyPlayers = int(input("Wpisz ile chcesz graczy: "))
		for player in range(1, howManyPlayers + 1):
			shuffle_card(howManyCards, player)
		counter = 0
		for index in cardsToBack:
			cardList.append(index)
		cardsToBack.clear()
		random.shuffle(cardList)
	except ValueError:
		print("Podałeś znaki zamiast cyfr lub nie podałes niczego!")
	except:
		print("Wystąpił nieznany błąd!")
