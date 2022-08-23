import numpy as np
import math
class Astar:
    grid_size = 0
    snake_body = 0
    food = 0
    food_pos = []
    visited = [[]]
    list_direction = []
    def __init__(self,snake_body_int, food_int, visit,g):
        self.snake_body = snake_body_int
        self.food = food_int
        self.visited = visit
        self.list_direction = []
        self.food_pos = []
        self.grid_size = g+2
    def initialize_attributes(self,snake_body_int, food_int, visit, food_location):
        self.snake_body = snake_body_int
        self.food = food_int
        self.visited = visit
        self.list_direction = []
        self.food_pos = food_location

    def get_direction_list(self):
        return(self.list_direction)
    def printf(self):
        print("########################")
        print(self.list_direction[::-1], self.snake_body, self.food, self.visited)
        print("########################")
    def get_node_name(self, i,j):
        return(self.grid_size*i+j)
    def dict_sort(self, dictionary_list):
        sorted_dict = {}
        keys = list(dictionary_list.keys())
        
        while(dictionary_list != {}):   
            min_v = 100000
            min_key = ""         
            for key in keys:
                if dictionary_list[key][1] <= min_v:
                    min_v = dictionary_list[key][1]
                    min_key = key
    
            sorted_dict[min_key] = dictionary_list[min_key]
            dictionary_list.pop(min_key)
            keys.remove(min_key)
        return(sorted_dict)


            
    def heuristic(self,i,j):
        return(((j-self.food_pos[1])**2 + (i-self.food_pos[0])**2)**.5)

    def astar(self,valid_turn, i, j):
        inital_snake_head_node = self.get_node_name(i,j)
        reached = 0#when we reach goal then stop
        start_node = self.get_node_name(i,j)
        #track previous poped node so that next turn will not be in direction of previous node
        prev_node_poped = -1
        finished_dictionary = {}
        # contains list of keys currently in dictionary_priority queue
        dict_key = [start_node]
        priority_q = {start_node : [0 , 0 + self.heuristic(i,j), start_node]}
        t = 50
        while(reached != 1 ):#in one iteration we look at all possible direction from head of snake 
            #pick first element of minimum priority queue (you can get the first key from dict_key)
            #move 1step in all possible valid direction
            #add in queues
            #the picked element is added to finished_dictionary and removed from priority_dictionary
            #sort queue 


            #two stoping condition either i reach food or i have nowhere to go
            if dict_key == []:#if empty queue
                reached = 1
                break
            current_node = dict_key[0]
            i,j = math.floor(current_node/self.grid_size), current_node%self.grid_size
            
            
            
            if [i,j] == self.food_pos:
                finished_dictionary[current_node] = priority_q[current_node]
                reached = 1
                break
            
            dist_till_here = priority_q[dict_key[0]][0]
            if (valid_turn[i-1][j] == 1 or valid_turn[i-1][j] == -1) and self.get_node_name(i-1,j) not in finished_dictionary.keys():
                node = self.get_node_name(i-1,j)
                if node in dict_key:#if already present then try to adjust the new path
                    d = dist_till_here + 1
                    if priority_q[node][0] > d:
                        priority_q[node][0] = d#update new distance
                        priority_q[node][1] = d+self.heuristic(i-1,j)#update new heuristic
                        priority_q[node][1] = current_node#update node from where we reached here
                else:
                    d = dist_till_here + 1
                    priority_q[node] = [d, d+self.heuristic(i-1,j), current_node]
                    dict_key.append(node)
                
            if (valid_turn[i+1][j] == 1 or valid_turn[i+1][j] == -1) and self.get_node_name(i+1,j) not in finished_dictionary.keys():
                node = self.get_node_name(i+1,j)
                if node in dict_key:#if already present then try to adjust the new path
                    d = dist_till_here + 1
                    if priority_q[node][0] > d:
                        priority_q[node][0] = d#update new distance
                        priority_q[node][1] = d+self.heuristic(i+1,j)#update new heuristic
                        priority_q[node][1] = current_node#update node from where we reached here
                else:
                    d = dist_till_here + 1
                    priority_q[node] = [d, d+self.heuristic(i+1,j), current_node]
                    dict_key.append(node)

            if (valid_turn[i][j-1] == 1 or valid_turn[i][j-1] == -1) and self.get_node_name(i,j-1) not in finished_dictionary.keys():
                
                node = self.get_node_name(i,j-1)
                if node in dict_key:#if already present then try to adjust the new path
                    d = dist_till_here + 1
                    if priority_q[node][0] > d:
                        priority_q[node][0] = d#update new distance
                        priority_q[node][1] = d+self.heuristic(i,j-1)#update new heuristic
                        priority_q[node][1] = current_node#update node from where we reached here
                else:
                    d = dist_till_here + 1
                    priority_q[node] = [d, d+self.heuristic(i,j-1), current_node]
                    dict_key.append(node)

            if (valid_turn[i][j+1] == 1 or valid_turn[i][j+1] == -1) and self.get_node_name(i,j+1) not in finished_dictionary.keys():
                node = self.get_node_name(i,j+1)
                if node in dict_key:#if already present then try to adjust the new path
                    d = dist_till_here + 1
                    if priority_q[node][0] > d:
                        priority_q[node][0] = d#update new distance
                        priority_q[node][1] = d+self.heuristic(i,j+1)#update new heuristic
                        priority_q[node][1] = current_node#update node from where we reached here
                else:
                    d = dist_till_here + 1
                    priority_q[node] = [d, d+self.heuristic(i,j+1), current_node]#distance assign heuristic assign node from where we reached here
                    dict_key.append(node)
                    
            
            finished_dictionary[current_node] = priority_q[current_node]
            finished_dictionary.keys()
            priority_q.pop(current_node)
            priority_q = self.dict_sort(priority_q)
            dict_key = list(priority_q.keys())
            # if t> 0 :
            #     print(current_node, priority_q, i, j,"\n")
            # t = t-1

        ##find path:##if finished dictionary do not contain food means cannot be reached
        #the direction list is given empty
        # print("\n\n",finished_dictionary)
        path = []
        node_nm = self.get_node_name(self.food_pos[0],self.food_pos[1])
        path.append(node_nm)
        if node_nm not in finished_dictionary.keys():
            self.list_direction = []
        else:

            prev_node = finished_dictionary[node_nm][2]
            
            finished_dictionary.pop(node_nm)
            
            while(True):            
                path.append(prev_node)            
                tmp = prev_node
                # print(prev_node)
                prev_node = finished_dictionary[prev_node][2]
                finished_dictionary.pop(tmp)
                if prev_node == inital_snake_head_node:
                    # print(prev_node,"^^^^^^^^^^^^^^")
                    path.append(prev_node)
                    break
                
            
            ##convert node in path list as index representation in path list
            
            path_i =[]
            for i in path:
                path_i.append([math.floor(i/self.grid_size), i%self.grid_size])
            ##find direction using path_i
            # print(path, path_i)
            direc = []
            for k in range(1, len(path_i)):
                if path_i[k-1][0]+1 == path_i[k][0] and path_i[k-1][1] == path_i[k][1]:
                    direc.append('u')
                elif path_i[k-1][0]-1 == path_i[k][0] and path_i[k-1][1] == path_i[k][1]:
                    direc.append('d')
                elif path_i[k-1][0] == path_i[k][0] and path_i[k-1][1]-1 == path_i[k][1]:
                    direc.append('r')
                elif path_i[k-1][0] == path_i[k][0] and path_i[k-1][1]+1 == path_i[k][1]:
                    direc.append('l')
            # print(direc)
            self.list_direction = direc
        return
# a = Astar(2,2,[], 8)
# a.initialize_attributes(2, -1, [], [7, 3])
# valid_turn = [
#                 [ 0,  0,  0 , 0 , 0  ,0  ,0  ,0 , 0,  0],
#                 [ 0,  1  ,1,  1,  1,  1,  1,  2,  1 , 0],
#                 [ 0 , 1,  1  ,1,  1 , 1,  2 , 2 , 1 , 0],
#                 [ 0  ,1 , 1 , 1,  1  ,1 , 2 , 1 , 1,  0],
#                 [ 0 , 1,  1 , 1 , 1 , 1 , 2,  1,  1,  0],
#                 [ 0 , 1 , 1,  1 , 1 , 1  ,2 , 1 , 1 , 0],
#                 [ 0 , 1  ,1,  1 , 1 , 1  ,2,  1,  1 , 0],
#                 [ 0 , 1 , 1 ,-1  ,1 , 1,  1 , 1,  1 , 0],
#                 [ 0 , 1  ,1 , 1 , 1,  1 , 1 , 1,  1 , 0],
#                 [ 0 , 0 , 0 , 0 , 0,  0 , 0,  0,  0,  0]
#             ] 

# a.astar(valid_turn, 1,7)

