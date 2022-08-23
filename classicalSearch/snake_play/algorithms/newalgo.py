import numpy as np
from .bfs import *
class Newalgo:
    count = 1
    grid_size = 0
    snake_body = 0
    food = 0
    queue = []
    list_direction = []
    # contains dictionary {str((i,j)):str((added first by which coordinate))}
    added_first = {}
    food_xy = []
    tail = []
    hamiltonian_cycle = []
    direc = []
    prev_index = 0

    def __init__(self, snake_body_int, food_int, q, t, food_pos, g):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}
        self.food_xy = food_pos
        self.tail = t
        self.grid_size = g
        self.direc = []

    def initialize_attributes(self, snake_body_int, food_int, q, t, food_pos):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}
        self.food_xy = food_pos
        self.tail = t

    def get_direction_list(self):
        return(self.list_direction)

    def printf(self):
        print(self.list_direction[::-1],
              self.snake_body, self.food, self.queue)

    def newalgo(self, valid_turn, i, j):
        
        path = []
        list_direction = []
        valid_turn_to_pass = valid_turn.copy()

        path = ['(2,1)', '(2,2)','(1,2)','(1,1)']
        # print(path,"during first iteration")
        self.count = self.count - 1
        valid_turn_to_pass[self.food_xy[0]][self.food_xy[1]] = 1#remove the food

        
    
        if path == []:
            return([])
        
        #path is comming in form ['(5,2)', '(4,3)', '(4,6)'] convert to list of list
        path_int = []
        for i in path:
            path_int.append(eval(i))
        
        len_of_list = len(path_int)
        i = len_of_list - 1
        while(True):
            
            if(path_int[i][1] == path_int[i-1][1]):#consecutive in same column
                col_l = path_int[i][1]+1
                col_r = path_int[i][1]-1

                row1,row2 = path_int[i-1][0], path_int[i][0]

                if(valid_turn_to_pass[row1][col_l] == 1 and valid_turn_to_pass[row2][col_l] == 1 and (row1, col_l) not in path_int and (row2, col_l) not in path_int):
                    path_int.insert(i, (row1, col_l))
                    path_int.insert(i+1, (row2, col_l))
                elif(valid_turn_to_pass[row1][col_r] == 1 and valid_turn_to_pass[row2][col_r] == 1 and (row1, col_r) not in path_int and (row2, col_r) not in path_int):
                    path_int.insert(i, (row1, col_r))
                    path_int.insert(i+1, (row2, col_r))                

            elif(path_int[i][0] == path_int[i-1][0]):#consecutive in same row
                row_d = path_int[i][0]+1
                row_u = path_int[i][0]-1

                col1,col2 = path_int[i-1][1], path_int[i][1]

                if(valid_turn_to_pass[row_d][col1] == 1 and valid_turn_to_pass[row_d][col2] == 1 and (row_d, col1) not in path_int and (row_d, col2) not in path_int):
                    path_int.insert(i, (row_d, col1))
                    path_int.insert(i+1, (row_d, col2))
                elif(valid_turn_to_pass[row_u][col1] == 1 and valid_turn_to_pass[row_u][col2] == 1 and (row_u, col1) not in path_int and (row_u, col2) not in path_int):
                    path_int.insert(i, (row_u, col1))
                    path_int.insert(i+1, (row_u, col2))
            
            #looping variables
            if len_of_list != len(path_int):
                #new element added then start expanding nodes from ending again
                len_of_list = len(path_int)
                i = len_of_list - 1
            else: 
                i = i - 1
            #print(path_int)
            #loop stop condtion 
            if i < 0 :
                #if i have reached to the goal i.e all element in list seen
                #while addition was done
                break
        
        #extract direction only till we get food in middle if not then 
        # direction list will be empty
        direc = []
        for k in range(1, len(path_int)):
            if path_int[k-1][0]+1 == path_int[k][0] and path_int[k-1][1] == path_int[k][1]:
                direc.append('u')
            elif path_int[k-1][0]-1 == path_int[k][0] and path_int[k-1][1] == path_int[k][1]:
                direc.append('d')
            elif path_int[k-1][0] == path_int[k][0] and path_int[k-1][1]-1 == path_int[k][1]:
                direc.append('r')
            elif path_int[k-1][0] == path_int[k][0] and path_int[k-1][1]+1 == path_int[k][1]:
                direc.append('l')
        return(path_int, direc)
    def new_algo(self, valid_turn, i, j):
        path_int = []
       
        #execute only once
        if self.count > 0:
            path_int, self.direc = self.newalgo( valid_turn, i, j)
            self.direc.insert(0,'u')
            self.count = self.count - 1
            self.hamiltonian_cycle = path_int
        # print("here new algo",valid_turn,path_int, self.direc, self.food_xy, self.tail)
        snake_head = self.tail[0]
        snake_head_index = self.hamiltonian_cycle.index(snake_head)
        #following is hamiltonian cycle
        # [(1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3), (6, 4), (6, 5), (6, 6), (5, 6), (4, 6), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1)] 
        #if food is at left side of snake head index in the above path(note above path is reversed i.e it is started from last to first)
        #then give slice of direction else cycle back and concatenate and return
        if tuple(self.food_xy) in self.hamiltonian_cycle[:snake_head_index]:
            self.list_direction = self.direc[self.hamiltonian_cycle.index(tuple(self.food_xy))+1: snake_head_index+1]
            
        else:
            self.list_direction =  self.direc[self.hamiltonian_cycle.index(tuple(self.food_xy))+1:] + self.direc[:snake_head_index+1] 
            # print("hey i am here", self.list_direction)
            # print("here new algo",valid_turn,self.hamiltonian_cycle, self.direc, self.food_xy, self.tail)

            

        # print("********************NEW ALGO********************************", self.list_direction)
        # print(self.list_direction)
        # print(direc)
        


        

# valid_turn = [
#                 [ 0,  0,  0,  0,  0,  0,  0],
#                 [ 0,  1,  1,  1,  1, 1,  0],
#                 [ 0,  1,  -1,  1,  1,  1,  0],
#                 [ 0,  2,  2,  1,  1,  1,  0],
#                 [ 0,  1,  2,  1,  1,  1,  0],
#                 [ 0,  1,  2,  2,  1,  1,  0],
#                 [ 0,  0,  0,  0,  0,  0,  0]
#             ]




# h = Hamilton(2,-1,[], [3,1], [2,2])
# h.hamilton(np.array(valid_turn), 5, 3)
