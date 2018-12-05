from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    team = models.CharField(max_length=200)

    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        return reverse('card-detail', args=[str(self.id)])

    def iter(self, cards):
        my_iter = iter(cards)
        return my_iter

    def getCards(self, cards):
        my_cards = list()
        for card in cards:
            cardObject = self.objects.get(name=card)
            my_cards.append(cardObject.name)
        return my_cards
