from django.shortcuts import render, redirect, get_object_or_404
from .models import PositionPlayer, Pitcher
from .serializer import PositionPlayerSerializer, PitcherSerializer
from rest_framework import viewsets
from django.views.generic import DetailView
from django.http import JsonResponse
from django.urls import reverse
import joblib

hitter_model = joblib.load('cards/data/war_prediction_model_hitters_rf.pkl')
pitcher_model = joblib.load('cards/data/war_prediction_model_pitchers_rf.pkl')

class PositionPlayerViewSet(viewsets.ModelViewSet):
    queryset = PositionPlayer.objects.all()
    serializer_class = PositionPlayerSerializer

class PitcherViewSet(viewsets.ModelViewSet):
    queryset = Pitcher.objects.all()
    serializer_class = PitcherSerializer
    
def home(request):
    return render(request, 'cards/home.html')

def default_player_detail(request):
    default_id = 951
    return redirect('player-detail', player_id=default_id)

def default_pitcher_detail(request):
    default_id = 4070
    return redirect('pitcher-detail', pitcher_id=default_id)

def player_detail(request, player_id):
    player = PositionPlayer.objects.get(id=player_id)
    features = [[player.war_last_year, player.war_year_before_last]]
    
    # Make the WAR prediction
    predicted_war = hitter_model.predict(features)[0]
    context = {
        'player': player,
        'predicted_war': predicted_war,
    }
    return render(request, 'cards/position_player_card.html', {'player': player})

def pitcher_detail(request, pitcher_id):
    pitcher = Pitcher.objects.get(id=pitcher_id)
    features = [[pitcher.war_last_year, pitcher.war_year_before_last]]
    
    # Make the WAR prediction
    predicted_war = pitcher_model.predict(features)[0]
    context = {
        'pitcher': pitcher,
        'predicted_war': predicted_war,
    }
    return render(request, 'cards/pitcher_card.html', {'pitcher': pitcher})

def search(request):
    query = request.GET.get('q')
    if query:
        # Try to get a position player first
        player = PositionPlayer.objects.filter(name__icontains=query).first()
        if player:
            return redirect('player-detail', player_id=player.id)
        
        # If not found, try to get a pitcher
        pitcher = Pitcher.objects.filter(name__icontains=query).first()
        if pitcher:
            return redirect('pitcher-detail', pitcher_id=pitcher.id)
        return render(request, 'search_form.html', {'error_message': 'Player not found.'})
    
    return render(request, 'search_form.html')

def player_autocomplete(request):
    if 'term' in request.GET:
        qs = PositionPlayer.objects.filter(name__icontains=request.GET.get('term'))
        players = [{
            'label': player.name, 
            'url': reverse('player-detail', kwargs={'player_id': player.id})
        } for player in qs]
        return JsonResponse(players, safe=False)
    return JsonResponse([], safe=False)

def pitcher_autocomplete(request):
    if 'term' in request.GET:
        qs = Pitcher.objects.filter(name__icontains=request.GET.get('term'))
        pitchers = [{
            'label': pitcher.name, 
            'url': reverse('pitcher-detail', kwargs={'pitcher_id': pitcher.id})
        } for pitcher in qs]
        return JsonResponse(pitchers, safe=False)
    return JsonResponse([], safe=False)

def formula_description(request):
    return render(request, 'cards/formula.html')