import random

cards_to_back = []
counter = 0
card_list = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]
            
random.shuffle(card_list)
def shuffle_card(how_many_cards, *players):
	global counter
	if how_many_cards * len(players) > len(card_list):
		print("Mamy za mało kart!")
	else:
		counter += 1
		for player in players:
			container = []
			for shuffle in range(how_many_cards):
				card = card_list.pop()
				container.append(card)
				cards_to_back.append(card)
			print("Karty gracza", counter, ":", container)
				

print("Rozpiska: \n1. Aby zakończyć")

while True:
	try:
		menu = input("Podaj co chcesz zrobić, jeśli chcesz przejść dalej kliknij enter, jeśli chcesz zakończyc wpisz 1.")
		if menu == "1":
			break
		how_many_cards = int(input("Podaj ile kart mam rozdać graczą: "))
		how_many_players = int(input("Wpisz ile chcesz graczy: "))
		for player in range(1, how_many_players + 1):
			shuffle_card(how_many_cards, player)
		counter = 0
		for index in cards_to_back:
			card_list.append(index)
		cards_to_back.clear()
		random.shuffle(card_list)
	except ValueError:
		print("Podałeś znaki zamiast cyfr lub nie podałes niczego!")
	except:
		print("Wystąpił nieznany błąd!")
