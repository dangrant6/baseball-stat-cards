from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home,
    default_pitcher_detail,
    default_player_detail,
    pitcher_detail,
    player_detail,
    PositionPlayerViewSet, 
    PitcherViewSet,
    search,
    player_autocomplete,
    pitcher_autocomplete,
    formula_description,
)

router = DefaultRouter()
router.register(r'positionplayers', PositionPlayerViewSet)
router.register(r'pitchers', PitcherViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('pitchers/', default_pitcher_detail, name='default-pitcher-detail'),
    path('pitchers/<int:pitcher_id>/', pitcher_detail, name='pitcher-detail'),
    path('positionplayers/', default_player_detail, name='default-player-detail'),
    path('positionplayers/<int:player_id>/', player_detail, name='player-detail'),
    path('search/', search, name='player-search'),
    path('player-autocomplete/', player_autocomplete, name='player-autocomplete'),
    path('pitcher-autocomplete/', pitcher_autocomplete, name='pitcher-autocomplete'),
    path('formula/', formula_description, name='formula_description'),
]
