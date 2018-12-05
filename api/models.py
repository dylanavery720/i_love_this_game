from django.db import models

# Create your models here.

# {'name': 'Ivica Zubac', 'positions': [<Position.CENTER: 'CENTER'>], 
# 'age': 20, 'team': <Team.LOS_ANGELES_LAKERS: 'LOS ANGELES LAKERS'>, 'games_played': 43, 
# 'games_started': 0, 'minutes_played': 410, 'made_field_goals': 61, 'attempted_field_goals': 122, 
# 'made_three_point_field_goals': 0, 'attempted_three_point_field_goals': 1, 'made_free_throws': 39, 
# 'attempted_free_throws': 51, 'offensive_rebounds': 45, 'defensive_rebounds': 78, 'assists': 25, 
# 'steals': 8, 'blocks': 15, 'turnovers': 26, 'personal_fouls': 47}

# CardManager will need some methods to calculate stats

# minutes / games played
# points / games games_played ??? where are points ? 
# etc

class CardManager(models.Manager):
    def  create_card(self, id, name, age, team, position, assists, games):
        teamlogo = 'img/' + team + '.jpg'
        avatar = 'img/' + name
        apg = "{:.1f}".format(assists / games)
        card = self.create(id=id,name=name, age=age, team=team, teamlogo=teamlogo, avatar=avatar, position=position, apg=apg)
        return card 

class Card(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    teamlogo = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    games = models.CharField(max_length=200)
    apg = models.CharField(max_length=200)
    
    objects = CardManager()
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
            try:
                cardObject = self.objects.get(name=card)
                my_cards.append(cardObject.name)
            except: 
                cardObjects = self.objects.all()
                # self.objects.all().delete()
        return my_cards
