from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'search-home'),
    path('dfs/', views.dfs, name = 'dfs-home'),
    path('bfs/', views.bfs, name = 'bfs-home'),
    path('astar/', views.astar, name = 'astar-home'),
    path('hamilton/', views.hamiltonian, name = 'hamilton-home'),
    path('hamilton_cycle/', views.hamiltonian_cycle, name = 'hamilton-cycle'),
    path('P5/', views.p5game, name = 'P5_snake'),
    path('analyse/', views.analysis, name = 'search-analyse'),
    path('analyse_all/', views.analysis_all, name = 'search-analyse-all'),



]
