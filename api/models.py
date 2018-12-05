from django.db import models
import stringcase

class CardManager(models.Manager):
    def  create_card(self, id, name, age, team, position, assists, games):
        teamlogo = 'img/' + stringcase.snakecase(team) + '.jpg'
        avatar = 'img/' + stringcase.snakecase(name) + '.jpg'
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
