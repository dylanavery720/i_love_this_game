from django.shortcuts import render
from basketball_reference_web_scraper import client
# Create your views here.

from api.models import Card


def index(request):
    Card.objects.all().delete()
    season_totals = client.players_season_totals(season_end_year=2019)
    for index, player in enumerate(season_totals):
        try:
            Card.objects.create_card(index, player)
        except:
            print('making cards')
            pass
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'index.html', context=context)


def card(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'card.html', context=context)
