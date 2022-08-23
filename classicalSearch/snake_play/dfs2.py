import numpy as np
from algorithms.dfs import *
import random

# inititalize
list_direction = []
grid_size = 5
position_x, position_y = 1, 1
old_tail = [(position_x, position_y)]
food_x = food_y = -1
snake_body = 2
food = -1
snake_body_lenght = 1
# initialize valid_turn matrix contain all zero for the postion where movement is invalid
valid_turn = np.ones((grid_size+2, grid_size+2), dtype=np.int16)
valid_turn[:, 0] = valid_turn[0, :] = valid_turn[grid_size+1,
                                                 :] = valid_turn[:, grid_size+1] = np.zeros(grid_size+2, dtype=np.int16)
visit = np.copy(valid_turn)


######################################################################
food_x, food_y = 1,2
position_x, position_y = 5,4

valid_turn[food_x,food_y] = -1#food
valid_turn[position_x,position_y] = snake_body#start
valid_turn[position_x,position_y-1] = snake_body#body
valid_turn[position_x,position_y-2] = snake_body#body

########################################################################
loop = 400
d = Dfs(snake_body, food, np.copy(visit))
d.dfs(valid_turn, position_x, position_y)
d.printf()
print(valid_turn)
