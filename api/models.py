from django.db import models
import stringcase

# Once deployed Database should be updated every day so that cards stay up to date... 

class CardManager(models.Manager):
    def  create_card(self, id, name, age, team, position, assists, steals, blocks, offensive_rebounds, defensive_rebounds, made_field_goals, attempted_field_goals, attempted_free_throws, made_three_point_field_goals, made_free_throws, games):
        teamlogo = 'img/' + stringcase.snakecase(team) + '.jpg'
        avatar = 'img/' + stringcase.snakecase(name) + '.jpg'
        photo = 'img/' + stringcase.snakecase(name) + '.jpg'
        points = self.calculatePoints(made_free_throws, made_field_goals, made_three_point_field_goals)
        apg = "{:.1f}".format(assists / games)
        spg = "{:.1f}".format(steals / games)
        bpg = "{:.1f}".format(blocks / games)
        rpg = "{:.1f}".format((offensive_rebounds + defensive_rebounds) / games)
        ppg = "{:.1f}".format(points / games)
        fgpercentage = "{:.1f}".format(made_field_goals / attempted_field_goals)
        ftpercentage = "{:.1f}".format(made_free_throws / attempted_free_throws)
        gp = games
        card = self.create(id=id,name=name, age=age, team=team, teamlogo=teamlogo, avatar=avatar, position=position, apg=apg, spg=spg, bpg=bpg, rpg=rpg, ppg=ppg, gp=gp, fgpercentage=fgpercentage, ftpercentage=ftpercentage)
        return card

    def calculatePoints(ft, fg, three):
        return (ft + (fg * 2) + (three * 3))
     

class Card(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    teamlogo = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    games = models.CharField(max_length=200)
    apg = models.CharField(max_length=200)
    spg = models.CharField(max_length=200)
    bpg = models.CharField(max_length=200)
    rpg = models.CharField(max_length=200)
    ppg = models.CharField(max_length=200)
    gp = models.CharField(max_length=200)
    
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
