from django.shortcuts import render
from .models import Game

def home(request):
    return render(request, 'games/home.html')

def list_games(request):
    games = Game.objects.all()
    return render(request, 'games/list_games.html', {'games': games})
