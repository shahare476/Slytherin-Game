import numpy as np
import sys
x=1000000

class Bfs:
    snake_body = 0
    food = 0
    queue = []
    list_direction = []
    # contains dictionary {str((i,j)):str((added first by which coordinate))}
    added_first = {}
    food_x, food_y = 0, 0 

    def __init__(self, snake_body_int, food_int, q):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}
        food_x, food_y = 0, 0 

    def initialize_attributes(self, snake_body_int, food_int, q):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}
        food_x, food_y = 0, 0 

    def get_direction_list(self):
        return(self.list_direction)

    def printf(self):
        print(self.list_direction[::-1],
              self.snake_body, self.food, self.queue)

    def bfs(self, valid_turn, i, j):
        if i == 0 or j == 0:
            return(False)

        # if valid_turn[i,j] == 0:
            # return(False)
        if valid_turn[i, j] == self.food:
            self.food_x, self.food_y = i,j
            return(True)
        # enquing all valid turns of w.r.t. current turns
        if valid_turn[i, j-1] != self.snake_body and valid_turn[i, j-1] != 0:
            key = str((i, j-1))
            if key not in self.added_first.keys():
                self.added_first[key] = str((i, j))
            self.queue.append([i, j-1, "l"])

        if valid_turn[i, j+1] != self.snake_body and valid_turn[i, j+1] != 0:
            #print(i, j+1, "R")
            key = str((i, j+1))
            if key not in self.added_first.keys():
                self.added_first[key] = str((i, j))
            self.queue.append([i, j+1, "r"])

        if valid_turn[i-1, j] != self.snake_body and valid_turn[i-1, j] != 0:
            key = str((i-1, j))
            if key not in self.added_first.keys():
                self.added_first[key] = str((i, j))
            self.queue.append([i-1, j, "u"])

        if valid_turn[i+1, j] != self.snake_body and valid_turn[i+1, j] != 0:
            key = str((i+1, j))
            if key not in self.added_first.keys():
                self.added_first[key] = str((i, j))
            self.queue.append([i+1, j, "d"])

        if len(self.queue) != 0:
            (curr_i, curr_j, t) = self.queue.pop(0)
        else:
            return(False)
        # print(curr_i, curr_j, t)
        new_valid_turn = np.copy(valid_turn)
        # if we are going to left then for that recusive call right will be invalid
        if t == "u" and valid_turn[curr_i+1, curr_j] != self.snake_body:
            new_valid_turn[curr_i+1, curr_j] = 0
        elif t == "d" and valid_turn[curr_i-1, curr_j] != self.snake_body:
            new_valid_turn[curr_i-1, curr_j] = 0
        elif t == "l" and valid_turn[curr_i, curr_j+1] != self.snake_body:
            new_valid_turn[curr_i, curr_j+1] = 0
        elif t == "r" and valid_turn[curr_i, curr_j-1] != self.snake_body:
            new_valid_turn[curr_i, curr_j-1] = 0

        # bfs search again on this popped turn
        if self.bfs(new_valid_turn, curr_i, curr_j) == True:
            return(True)

    def initiate_bfs(self, turns, position_x, position_y):
        sys.setrecursionlimit(x)
        cx_cy = str((position_x, position_y))
        tmp = []
        if self.bfs(turns, position_x, position_y) == True:
            # back track the path using dictionnary
            
            fx_fy = str((self.food_x, self.food_y))
            tmp.append(fx_fy)
            #print(self.added_first)
            for i in range(len(self.added_first)):
                new_key = self.added_first[fx_fy]
                tmp.append(new_key)
                fx_fy = new_key
                if new_key == cx_cy:
                    break
            # print(tmp)
            #convert to list_direction
            for i in range(len(tmp)-1):
            	delx = (int(tmp[i][1]) - int(tmp[i+1][1]))
            	dely = (int(tmp[i][4]) - int(tmp[i+1][4]))
            	if delx == -1:
            	    self.list_direction.append('u')
            	elif delx == 1:
            	    self.list_direction.append('d')            	
            	if dely == -1:
            	    self.list_direction.append('l')
            	elif dely == 1:
            	    self.list_direction.append('r')
        
        return(tmp)