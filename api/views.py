from django.shortcuts import render
from basketball_reference_web_scraper import client
# Create your views here.

def index(request):

    season_totals = client.players_season_totals(season_end_year=2018)

    context = {
        'season_totals': season_totals,
    }
    print(season_totals)
    return render(request, 'index.html', context=context)