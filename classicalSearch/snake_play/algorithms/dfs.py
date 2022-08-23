import numpy as np

class Dfs:
    snake_body = 0
    food = 0
    visited = [[]]
    list_direction = []
    def __init__(self,snake_body_int, food_int, visit):
        self.snake_body = snake_body_int
        self.food = food_int
        self.visited = visit
        self.list_direction = []
    def initialize_attributes(self,snake_body_int, food_int, visit):
        self.snake_body = snake_body_int
        self.food = food_int
        self.visited = visit
        self.list_direction = []

    def get_direction_list(self):
        return(self.list_direction)
    def printf(self):
        print("########################")
        print(self.list_direction[::-1], self.snake_body, self.food, self.visited)
        print("########################")

    
    def dfs(self,valid_turn, i, j):
        if i == 0 or j == 0 :
            return(False)        
        if self.visited[i][j] == 0:#1 means not visited and 0 means visited
            return(False)
        else:
            self.visited[i][j] = 0        
        if valid_turn[i,j] == 0:
            return(False)        
        if valid_turn[i,j] == self.food:
            return(True)
        
        if valid_turn[i,j-1] != self.snake_body and self.dfs( valid_turn, i, j-1) == True:
            self.list_direction.append("l")
            return(True)

        if valid_turn[i,j+1] != self.snake_body and self.dfs(valid_turn, i, j+1) == True:
            self.list_direction.append("r")
            return(True)

        if valid_turn[i-1,j] != self.snake_body and self.dfs( valid_turn, i-1, j) == True:
            self.list_direction.append("u")
            return(True)

        if valid_turn[i+1,j] != self.snake_body and self.dfs( valid_turn, i+1, j) == True:
            self.list_direction.append("d")
            return(True)