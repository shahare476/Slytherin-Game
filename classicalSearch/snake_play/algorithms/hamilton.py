import numpy as np
from .bfs1 import *
import sys
class Hamilton:
    snake_body = 0
    food = 0
    queue = []
    list_direction = []
    # contains dictionary {str((i,j)):str((added first by which coordinate))}
    added_first = {}
    food_xy = []
    tail_end = []
    count = 1
    grid_size = 0

    def __init__(self, snake_body_int, food_int, q, t, food_pos,g):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}
        self.food_xy = food_pos
        self.tail_end = t
        self.grid_size = g

    def initialize_attributes(self, snake_body_int, food_int, q, t, food_pos):
        self.snake_body = snake_body_int
        self.food = food_int
        self.queue = q  # empty queue
        self.list_direction = []
        self.added_first = {}
        self.food_xy = food_pos
        self.tail_end = t

    def get_direction_list(self):
        return(self.list_direction)

    def printf(self):
        print(self.list_direction[::-1],
              self.snake_body, self.food, self.queue)

    def hamilton(self, valid_turn, i, j):
        sys.setrecursionlimit(1000000)
        path = []
        list_direction = []
        valid_turn_to_pass = valid_turn.copy()
        if self.count == 1:
            path = ['(1,1)','(2,1)', '(2,2)','(1,2)', '(1,1)']
            # print(path,"during first iteration")
            self.count = self.count - 1
            valid_turn_to_pass[self.food_xy[0]][self.food_xy[1]] = 1#remove the food

            # print(path,"inside hamiltonian no bfs ************",valid_turn,"\n" ,valid_turn_to_pass, "\n",self.food_xy )

        else:
            valid_turn_to_pass[self.tail_end[0]][self.tail_end[1]] = self.food#make tail food
            valid_turn_to_pass[self.food_xy[0]][self.food_xy[1]] = 1#remove the food
            # print(valid_turn_to_pass)
            b = Bfs(2, -1, [])
            b.initialize_attributes(2, -1, [])        
            path = b.initiate_bfs(valid_turn_to_pass, i, j)
            # print(path,"inside hamiltonian bfs ************",valid_turn,path,"\n" ,valid_turn_to_pass, "\n",self.food_xy )
            list_direction = b.get_direction_list()
        
        if path == []:
            self.list_direction = []
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

        #find index of (food_x, food_y) in path path_int
        #if food cannot be reached then not in path and then save empty list
        if tuple(self.food_xy) not in path_int:
            self.list_direction = []
            # print("path jere wtf", path_int, self.food_xy)
        else:
            index = path_int.index(tuple(self.food_xy))
            #direction list is from index to end
            self.list_direction = direc[index:]
        # print("path jere wtf", path_int, self.food_xy)
        # print(self.list_direction)
        # print(direc)
        return
        

# valid_turn =  [[ 0 , 0 , 0  ,0  ,0 , 0  ,0  ,0 , 0 , 0],
#                 [ 0 , 2 , 1  ,1 , 1 , 1,  1,  1,  1,  0],
#                 [ 0 , 1  ,1 , 1 , 1,  1  ,1  ,1 , 1 , 0],
#                 [ 0  ,1 , 1 ,1 , 1,  1  ,1,  1 , 1 , 0],
#                 [ 0 , 1 , 1 , 1 , 1, 1 , 1,  1 , 1 ,0],
#                 [ 0 , 1 , 1  ,1 , 1 , 1 , 1 , 1,  1,  0],
#                 [ 0,  1,  1 , 1  ,1  ,1,  1 , 1 , 1 , 0],
#                 [ 0  ,1 , 1  ,1 , 1 , 1, -1  ,1 , 1 , 0],
#                 [ 0  ,1  ,1 , 1  ,1  ,1 , 1,  1 , 1  ,0],
#                 [ 0  ,0 , 0 , 0  ,0 , 0 , 0  ,0 , 0,  0]] 



# h = Hamilton(2,-1,[], [1,1], [7,6], 8)
# h.hamilton(np.array(valid_turn), 1, 1)
