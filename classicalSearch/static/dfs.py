# dfs

# find possible valid action according to walls
# and body then do a turn and call dfs again

# 20X20 grid or matrix valid_turn matrix which contains 0 on the cell if
# not to move in that direction
import numpy as np

grid_size = 5

food_x, food_y = 5, 5
position_x, position_y = 1, 1

snake_body = 2

turns = np.ones((grid_size+2, grid_size+2))
turns[:, 0] = turns[0, :] = turns[grid_size+1,
                                  :] = turns[:, grid_size+1] = np.zeros(grid_size+2)
visited = np.copy(turns)
turns[food_x, food_y] = -1  # food
turns[position_x, position_y] = snake_body  # start
turns[position_x, position_y-1] = snake_body  # body
turns[position_x+1, position_y-1] = snake_body  # body
turns[position_x+1, position_y-2] = snake_body  # body


food = -1

list_direction = []


def dfs(valid_turn, i, j):
    if i == 0 or j == 0:
        return(False)

    if visited[i, j] == 0:  # 1 means not visited and 0 means visited
        return(False)
    else:
        visited[i, j] = 0

    if valid_turn[i, j] == 0:
        return(False)

    if valid_turn[i, j] == food:
        return(True)

    if valid_turn[i, j-1] != snake_body and dfs(valid_turn, i, j-1) == True:
        list_direction.append("l")
        return(True)

    if valid_turn[i, j+1] != snake_body and dfs(valid_turn, i, j+1) == True:
        list_direction.append("r")
        return(True)

    if valid_turn[i-1, j] != snake_body and dfs(valid_turn, i-1, j) == True:
        list_direction.append("u")
        return(True)

    if valid_turn[i+1, j] != snake_body and dfs(valid_turn, i+1, j) == True:
        list_direction.append("d")
        return(True)

   # snake collision condition not checked or may be not implemented


dfs(turns, position_x, position_y)
print(turns)
print(list_direction[::-1])


##################################################
# bfs

grid_size = 5

food_x, food_y = 5, 5
position_x, position_y = 2, 3

snake_body = 2

turns = np.ones((grid_size+2, grid_size+2))
turns[:, 0] = turns[0, :] = turns[grid_size+1,
                                  :] = turns[:, grid_size+1] = np.zeros(grid_size+2)
visited = np.copy(turns)
turns[food_x, food_y] = -1  # food
turns[position_x, position_y] = snake_body  # start
turns[position_x, position_y-1] = snake_body  # body
turns[position_x+1, position_y-1] = snake_body  # body
turns[position_x+1, position_y-2] = snake_body  # body


food = -1

list_direction = []


class Bfs:
    snake_body = 0
    food = 0
    queue = []
    list_direction = []
    # contains dictionary {str((i,j)):str((added first by which coordinate))}
    added_first = {}

    def __init__(self, snake_body_int, food_int, q):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}

    def initialize_attributes(self, snake_body_int, food_int, q):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}

    def get_direction_list(self):
        return(self.list_direction)

    def printf(self):
        print("########################")
        print(self.list_direction[::-1],
              self.snake_body, self.food, self.queue)
        print("########################")

    def bfs(self, valid_turn, i, j):
        if i == 0 or j == 0:
            return(False)

        # if valid_turn[i,j] == 0:
            # return(False)

        if valid_turn[i, j] == self.food:
            return(True)
        # enquing all valid turns of w.r.t. current turns
        if valid_turn[i, j-1] != self.snake_body and valid_turn[i, j-1] != 0:
            key = str((i, j-1))
            if key not in self.added_first.keys():
                self.added_first(key) = str((i, j))
            self.queue.append([i, j-1, "l"])

        if valid_turn[i, j+1] != self.snake_body and valid_turn[i, j+1] != 0:
            #print(i, j+1, "R")
            key = str((i, j+1))
            if key not in self.added_first.keys():
                self.added_first(key) = str((i, j))
            self.queue.append([i, j+1, "r"])

        if valid_turn[i-1, j] != self.snake_body and valid_turn[i-1, j] != 0:
            key = str((i-1, j))
            if key not in self.added_first.keys():
                self.added_first(key) = str((i, j))
            self.queue.append([i-1, j, "u"])

        if valid_turn[i+1, j] != self.snake_body and valid_turn[i+1, j] != 0:
            key = str((i+1, j))
            if key not in self.added_first.keys():
                self.added_first(key) = str((i, j))
            self.queue.append([i+1, j, "d"])

        if len(self.queue) != 0:
            (curr_i, curr_j, t) = self.queue.pop(0)
        else:
            return(False)
        print(curr_i, curr_j, t)
        new_valid_turn = np.copy(valid_turn)
        # if we are going to left then for that recusive call right will be invalid
        if t == "u" and valid_turn[curr_i+1, curr_j] != self.snake_body:
            new_valid_turn[curr_i+1, curr_j] = 0
        elif t == "d" and valid_turn[curr_i-1, curr_j] != self.snake_body:
            new_valid_turn[curr_i-1, curr_j] = 0
        elif t == "l" and valid_turn[curr_i, curr_j+1] != self.snake_body:
            new_valid_turn[curr_i, curr_j+1] = 0
        elif t == "r" and valid_turn[curr_i, curr_j-1] != self.snake_body:
            valid_turn[curr_i, curr_j-1] = 0

        # bfs search again on this popped turn
        if self.bfs(new_valid_turn, curr_i, curr_j) == True:
            self.list_direction.append(t)
            return(True)

    def initiate_bfs(self, turns, position_x, position_y):
        cx_cy = str((position_x, position_y))
        if self.bfs(turns, position_x, position_y) == True:
            # back track the path using dictionnary
            tmp = [cx_cy]
            for i in self.added_first:
                new_key = self.added_first(tmp)
                tmp.append(new_key)
                tmp = new_key
        print(tmp)


b = Bfs(snake_body, food, [])
b.initiate_bfs(turns, position_x, position_y)
print(turns)
print(b.list_direction[::-1])
