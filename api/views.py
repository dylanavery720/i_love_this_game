from django.shortcuts import render
from basketball_reference_web_scraper import client
# Create your views here.

from api.models import Card


def index(request):
    season_totals = client.players_season_totals(season_end_year=2018)
    for index, player in enumerate(season_totals):
        try:
            Card.objects.create_card(index, player['name'], player['age'], player['team'].value)
        except:
            pass
    
    cards = Card.objects.all() 
    context = {
        'cards': cards,
    }
    return render(request, 'index.html', context=context)