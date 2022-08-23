from .snake_play.final_data import *
import time
import numpy as np
import matplotlib.pyplot as plt
import sys
def analyse(search_name):
    sys.setrecursionlimit(100000)
    scores_data = []#iteration, average score, avg time complexity
    itr = 0
    avg_score = 0
    avg_time_complexity = 0

    start_time = time.time()
    for i in range(10):        
        for k in range(1):
            direction, position = get_data(search_name)
            avg_score = avg_score + len(position) - 1            
            itr = itr + 1
        avg_time_complexity = avg_time_complexity + time.time() - start_time
        print("iteration reached", itr*5)
        scores_data.append([itr*5, avg_score/itr, avg_time_complexity/itr])
    
    scores_data_np = np.array(scores_data)
    print(scores_data_np)
    itr_axis = np.array(scores_data_np[:,0])
    score_axis = np.array(scores_data_np[:,1])
    time_axis = np.array(scores_data_np[:,2])
    
    plt.figure(1)
    plt.ylabel('Average Score')
    plt.xlabel('Number of iterations')
    plt.plot(itr_axis, score_axis, label = search_name)
    plt.legend(loc='best')
    #plt.show()
    score_path = "classicalSearch/static/classicalSearch/"+search_name+"_s.png"
    plt.savefig(score_path)
    
    plt.figure(2)    
    plt.ylabel('Average Time')
    plt.xlabel('Number of iterations')
    plt.plot(itr_axis, time_axis, label = search_name)
    plt.legend(loc='best')
    #plt.show()
    time_path = "classicalSearch/static/classicalSearch/"+search_name+"_t.png"
    plt.savefig(time_path)

    return("classicalSearch/"+search_name+"_s.png", "classicalSearch/"+search_name+"_t.png")    
    # return(itr_axis, score_axis, time_axis)

# sys.setrecursionlimit(1000000)
# print(sys.getrecursionlimit())
# itr_axis, score_axis, time_axis = analyse("bfs")
# plt.figure(1)
# plt.ylabel('Average Score')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, score_axis)
# #plt.show()
# score_path = "s"+"_s.png"
# plt.savefig(score_path)


# plt.figure(2)    
# plt.ylabel('Average Time')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, time_axis)
# #plt.show()
# time_path = "t"+"_t.png"
# plt.savefig(time_path)


# sys.setrecursionlimit(1000000)
# itr_axis, score_axis, time_axis = analyse("dfs")
# plt.figure(1)
# plt.ylabel('Average Score')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, score_axis)
# #plt.show()
# score_path = "s"+"_s.png"
# plt.savefig(score_path)


# plt.figure(2)    
# plt.ylabel('Average Time')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, time_axis)
# #plt.show()
# time_path = "t"+"_t.png"
# plt.savefig(time_path)


# sys.setrecursionlimit(1000000)
# itr_axis, score_axis, time_axis = analyse("astar")
# plt.figure(1)
# plt.ylabel('Average Score')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, score_axis)
# #plt.show()
# score_path = "s"+"_s.png"
# plt.savefig(score_path)


# plt.figure(2)    
# plt.ylabel('Average Time')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, time_axis)
# #plt.show()
# time_path = "t"+"_t.png"
# plt.savefig(time_path)


# sys.setrecursionlimit(1000000)
# itr_axis, score_axis, time_axis = analyse("bfs")
# plt.figure(1)
# plt.ylabel('Average Score')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, score_axis)
# #plt.show()
# score_path = "s"+"_s.png"
# plt.savefig(score_path)


# plt.figure(2)    
# plt.ylabel('Average Time')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, time_axis)
# #plt.show()
# time_path = "t"+"_t.png"
# plt.savefig(time_path)

# sys.setrecursionlimit(1000000)
# itr_axis, score_axis, time_axis = analyse("hamilton")
# plt.figure(1)
# plt.ylabel('Average Score')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, score_axis)
# #plt.show()
# score_path = "s"+"_s.png"
# plt.savefig(score_path)


# plt.figure(2)    
# plt.ylabel('Average Time')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, time_axis)
# #plt.show()
# time_path = "t"+"_t.png"
# plt.savefig(time_path)

# sys.setrecursionlimit(1000000)
# itr_axis, score_axis, time_axis = analyse("newalgo")
# plt.figure(1)
# plt.ylabel('Average Score')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, score_axis)
# #plt.show()
# score_path = "s"+"_s.png"
# plt.savefig(score_path)


# plt.figure(2)    
# plt.ylabel('Average Time')
# plt.xlabel('Number of iterations')
# plt.plot(itr_axis, time_axis)
# #plt.show()
# time_path = "t"+"_t.png"
# plt.savefig(time_path)