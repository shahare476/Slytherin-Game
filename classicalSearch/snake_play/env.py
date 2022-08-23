import numpy as np
from .algorithms.dfs import *
from .algorithms.bfs import *
from .algorithms.astar import *
from .algorithms.hamilton import *
from .algorithms.newalgo import *

import random

def game_play(search):
    all_food_positions = []
    all_direction_list = []
    # inititalize
    list_direction = []
    grid_size = 8
    position_x, position_y = 1, 1
    old_tail = [(position_x, position_y)]
    food_x = food_y = -1
    snake_body = 2
    food = -1
    snake_body_lenght = 1
    new_algo_counter = 1
    # initialize valid_turn matrix contain all zero for the postion where movement is invalid
    valid_turn = np.ones((grid_size+2, grid_size+2), dtype=np.int16)
    valid_turn[:, 0] = valid_turn[0, :] = valid_turn[grid_size+1,
                                                    :] = valid_turn[:, grid_size+1] = np.zeros(grid_size+2, dtype=np.int16)
    visit = np.copy(valid_turn)


    ########################################################################
    loop = grid_size**2
    if search == "bfs":
        b = Bfs(snake_body, food, [])
    elif search == "dfs":
        d = Dfs(snake_body, food, np.copy(visit))
    elif search == "astar":
        a = Astar(snake_body, food, np.copy(visit), grid_size)
    elif search == "hamilton":
        h = Hamilton(snake_body, food, [], [], [], grid_size)
    elif search == "newalgo":
        n = Newalgo(snake_body, food, [], [], [], grid_size )
    
   
    

    while(loop > 0):
        
        # find new tail
        new_tail = []
        # calculate length of list_direction
        len_list_direction = len(list_direction)
        #make previous food location valid
        if food_x != -1:#not the first iteration
            valid_turn[food_x, food_y] = snake_body# increased by 1
            new_tail.append((food_x, food_y))# increased by 1
            
        
        # find valid_turn matrix
        if list_direction == []:  # implies game has started
            valid_turn[position_x, position_y] = snake_body
            # print(position_x, position_y,"first time")            
            new_tail = old_tail
        else:
            x = food_x
            y = food_y
            
            l = min(snake_body_lenght-1, len_list_direction-1)
            i = 0
            while l > 0:
                t = list_direction[i]
                if t == 'r':
                    y = y - 1
                    valid_turn[x, y] = snake_body
                    # print(x,y,"t==r")
                    new_tail.append((x, y))
                elif t == 'l':
                    y = y + 1
                    valid_turn[x, y] = snake_body
                    # print(x,y,"t==l")
                    new_tail.append((x, y))
                elif t == 'u':
                    x = x + 1
                    valid_turn[x, y] = snake_body
                    # print(x,y,"t==u")
                    new_tail.append((x, y))
                elif t == 'd':
                    x = x - 1
                    valid_turn[x, y] = snake_body
                    # print(x,y,"t==d")
                    new_tail.append((x, y))
                # print("new tail is",new_tail)
                
                i = i + 1
                l = l - 1
            # print("old tail",old_tail)
            
            # if turns taken was less than snake length than remove tail block from back
            if len_list_direction > snake_body_lenght:
                l = snake_body_lenght - 1
                while(l > 0):
                    (x, y) = old_tail.pop()  # empty all old tail
                    # removing oldtail means position has become valid
                    valid_turn[x, y] = 1
                    l = l - 1
            else:
                l = len_list_direction - 1
                while(l > 0):
                    # empty old tail only by only position it has moved forward
                    (x, y) = old_tail.pop()
                    # removing oltail means position has become valid
                    valid_turn[x, y] = 1
                    l = l - 1
                new_tail = new_tail + old_tail
            old_tail = new_tail
            # print("new tail",new_tail)
        # produce food location not on snake body    
        food_x = random.randint(1, grid_size)
        food_y = random.randint(1, grid_size)
        
        while((food_x, food_y) in old_tail):
            food_x = random.randint(1, grid_size)
            food_y = random.randint(1, grid_size)
            if len(old_tail) == grid_size**2:
                break
        #append in all_food_positions
        all_food_positions.append([food_x, food_y])
        # print("new food location generated ",food_x, food_y)
        valid_turn[food_x, food_y] = food
        

        # print("**************TAIL*************", new_tail)
        #initalize direction list before calling
        if search == "bfs":
            b.initialize_attributes(snake_body, food, [])
        elif search == "dfs":
            d.initialize_attributes(snake_body, food, np.copy(visit))
        elif search == "astar":
            a.initialize_attributes(snake_body, food, np.copy(visit), [food_x, food_y])
        elif search == "hamilton":
            h.initialize_attributes(snake_body, food, [], list(new_tail[-1]), [food_x, food_y] )
        elif search == "newalgo":
            n.initialize_attributes(snake_body, food, [], new_tail, [food_x, food_y])

        if search == "bfs":
            b.initiate_bfs(valid_turn, position_x, position_y)
        elif search == "dfs":
            d.dfs(valid_turn, position_x, position_y)
        elif search == "astar":
            a.astar(valid_turn, position_x, position_y)
        elif search == "hamilton":
            # print("inside enve before function call",[food_x, food_y], valid_turn)
            h.hamilton(valid_turn, position_x, position_y)
        elif search == "newalgo":
            n.new_algo(valid_turn[:], position_x, position_y)
       

        #for next dfs call new position of snake head will be at this iteration food position
        position_x = food_x
        position_y = food_y


        if search == "bfs":
            list_direction = b.get_direction_list()
            # print("bfs******\nTurns matrix\n", valid_turn,"\nlist direction", list_direction[::-1])#list_direction[::-1]
            
        elif search == "dfs":
            list_direction = d.get_direction_list()
            # print("dfs******\nTurns matrix\n", valid_turn,"\nlist direction", list_direction[::-1])#list_direction[::-1]
            
        elif  search == "astar":
            list_direction = a.get_direction_list()
            # print("astar******\nTurns matrix\n", valid_turn,"\nlist direction", list_direction[::-1])#list_direction[::-1]
            
        elif search == "hamilton":
            list_direction = h.get_direction_list()
            # print("hamilton******\nTurns matrix\n", valid_turn,"\nlist direction", list_direction[::-1],"\n", [food_x, food_y])#list_direction[::-1]
        elif search == "newalgo":
            # if new_algo_counter == 1:
            list_direction = n.get_direction_list()
            new_algo_counter = new_algo_counter + 1
            # else:
                # list_direction = n.get_direction_list()#[:-1]
            # print("newalgo******\nTurns matrix\n", valid_turn,"\nlist direction", list_direction[::-1])#list_direction[::-1]
            

            # print("hamilton cucle******\nTurns matrix\n", valid_turn,"\nlist direction", list_direction[::-1],"\n", [food_x, food_y],"old tail\n", old_tail)#list_direction[::-1]

            


        
        #append direction list in all_direction_list
        all_direction_list.append(list_direction[::-1])
        # print("after dfs\n")
        # d.printf()
        # if list_direction has remained empty then snake game ended else length++
        if list_direction != []:
            snake_body_lenght = snake_body_lenght + 1
        else:
            break
        

        # remove current food from the place so that new food is place randomly
        valid_turn[food_x, food_y] = 1
        loop = loop - 1
        # print(all_direction_list, all_food_positions)
    ###########################################################################
    
    return(all_direction_list, all_food_positions)