from .algorithms.action import *
from .env import *



def get_data(search):
	all_direction_char, all_food_position = game_play(search)
	all_direction_int = []

	for item in all_direction_char:
	    all_direction_int.append(action(item))

	print(all_direction_int, all_food_position)
	return(all_direction_int, all_food_position)

