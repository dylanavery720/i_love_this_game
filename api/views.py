from django.shortcuts import render
from django.views import generic
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


def frontcard(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'frontcard.html', context=context)


class CardDetailView(generic.DetailView):
    model = Card
    # fields = ('jersey', 'teamlogo')
    # success_url = reverse_lazy('project_change')


class FrontCardDetailView(generic.ListView):
    model = Card
    # fields = ('jersey', 'teamlogo')
    # success_url = reverse_lazy('project_change')
