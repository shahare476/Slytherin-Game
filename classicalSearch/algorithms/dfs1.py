#dfs

# find possible valid action according to walls
# and body then do a turn and call dfs again

# 20X20 grid or matrix valid_turn matrix which contains 0 on the cell if 
# not to move in that direction
import numpy as np

grid_size = 5

food_x, food_y = 1, 2
position_x, position_y = 3,1

snake_body = 2

turns = np.ones((grid_size+2,grid_size+2))
turns[:,0] = turns[0,:] = turns[grid_size+1,:] = turns[:,grid_size+1] = np.zeros(grid_size+2)
visited = np.copy(turns)
turns[food_x,food_y] = -1#food
turns[position_x,position_y] = snake_body#start
turns[position_x+1,position_y] = snake_body#body
turns[position_x+1,position_y+1] = snake_body#body
#turns[position_x,position_y-2] = snake_body#body
#turns[position_x+1,position_y-1] = snake_body#body
#turns[position_x+1,position_y-2] = snake_body#body


food = -1

list_direction = []

def dfs(valid_turn, i, j):
    if i == 0 or j == 0 :
        return(False)
    
    if visited[i,j] == 0:#1 means not visited and 0 means visited
        return(False)
    else:
        visited[i,j] = 0
    
    if valid_turn[i,j] == 0:
        return(False)
    
    if valid_turn[i,j] == food:
        return(True)
    
    if valid_turn[i,j-1] != snake_body and dfs(valid_turn, i, j-1) == True:
        list_direction.append("l")
        return(True)

    if valid_turn[i,j+1] != snake_body and dfs(valid_turn, i, j+1) == True:
        list_direction.append("r")
        return(True)

    if valid_turn[i-1,j] != snake_body and dfs(valid_turn, i-1, j) == True:
        list_direction.append("u")
        return(True)

    if valid_turn[i+1,j] != snake_body and dfs(valid_turn, i+1, j) == True:
        list_direction.append("d")
        return(True)

   ##snake collision condition not checked or may be not implemented

dfs(turns, position_x,position_y)
print(turns)
print(list_direction[::-1])
