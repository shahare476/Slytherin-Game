from django.shortcuts import render
from django.http import HttpResponse
from random import random
from json import dumps 
import math
from django.views.decorators.clickjacking import xframe_options_exempt
from .snake_play.final_data import *
from .analyse import *
context = {
    'all_direction' : [],
    'all_position' : [],
    'search' : ""
}
def home(request):    
    return render(request, 'index.html')
@xframe_options_exempt
def p5game(request):
    contextJson = dumps(context)
    print("inside p5game\n",contextJson)
    return render(request, 'P5/frame.html', context)
def dfs(request):
    context['search'] = "Depth First Search"
    context['all_direction'], context['all_position'] = get_data("dfs")
    return render(request, 'dfs.html',context)
def bfs(request):
    context['search'] = "Breadth First Search"
    context['all_direction'], context['all_position'] = get_data("bfs")
    return render(request, 'bfs.html',context)
def astar(request):
    context['search'] = "A-Star"
    context['all_direction'], context['all_position'] = get_data("astar")
    return render(request, 'astar.html')
def hamiltonian(request):
    context['search'] = "Hamiltonian Path"
    context['all_direction'], context['all_position'] = get_data("hamilton")
    return render(request, 'hamilton.html')
def hamiltonian_cycle(request):
    context['search'] = "Hamiltonian Cycle"
    context['all_direction'], context['all_position'] = get_data("newalgo")
    print(context)
    return render(request, 'newalgo.html')

context_analyse = {
    'search' : "",
    'image_path_score' : "",
    'image_path_time' : ""
}
def analysis(request):

    image_path_score = ""
    image_path_time = ""
    if context['search'] == "Depth First Search":
        image_path_score, image_path_time = analyse("dfs")
        
    elif context['search'] == "Breadth First Search":
        image_path_score, image_path_time = analyse("bfs")

    elif context['search'] == "A-Star":
        image_path_score, image_path_time = analyse("astar")

    elif context['search'] == "Hamiltonian Path":
        image_path_score, image_path_time = analyse("hamilton")

    elif context['search'] == "Hamiltonian Cycle":        
        image_path_score, image_path_time = analyse("newalgo")
         
    
    context_analyse['search'] = context['search']
    context_analyse['image_path_score'] = image_path_score
    context_analyse['image_path_time'] = image_path_time
    print(context_analyse)

    return render(request, 'analyse.html', context_analyse)



def analysis_all(request):

    return render(request, 'overallanalysis.html')









# def simulateKeyPress(key):
#     keyboard = Controller()
#     keyboard.press(key)
#     keyboard.release(key)

# while(1):
#     simulateKeyPress(Key.up)
#     simulateKeyPress(Key.left)
#     simulateKeyPress(Key.right)
#     simulateKeyPress(Key.down)