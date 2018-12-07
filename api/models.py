from django.db import models
import stringcase

# Once deployed Database should be updated every day so that cards stay up to date...


class CardManager(models.Manager):
    def create_card(self, id, player):
        print('creating card')
        teamlogo = 'img/' + \
            stringcase.snakecase(player['team'].value.title()) + '.jpg'
        avatar = 'img/avatar_' + stringcase.snakecase(player['name']) + '.jpg'
        photo = 'img/' + stringcase.snakecase(player['name']) + '.jpg'
        print('calculating points')
        points = self.calculatePoints(
            player['made_free_throws'], player['made_field_goals'], player['made_three_point_field_goals'])
        print('done')
        apg = "{:.1f}".format(player['assists'] / player['games_played'])
        spg = "{:.1f}".format(player['steals'] / player['games_played'])
        bpg = "{:.1f}".format(player['blocks'] / player['games_played'])
        rpg = "{:.1f}".format(
            (player['offensive_rebounds'] + player['defensive_rebounds']) / player['games_played'])
        ppg = "{:.1f}".format(points / player['games_played'])
        fgpercentage = "{:.1f}".format(
            player['made_field_goals'] / player['attempted_field_goals'])
        ftpercentage = "{:.1f}".format(
            player['made_free_throws'] / player['attempted_free_throws'])
        gp = player['games_played']
        print(id)
        print(id, player['name'], player['age'])
        print(player['team'].value.title(
        ), teamlogo, avatar)
        print(apg, spg, bpg, rpg, ppg, gp, fgpercentage,
              ftpercentage, player['positions'][0].value)
        print('saving card to db')
        card = self.create(id=id, name=player['name'], age=player['age'], team=player['team'].value.title(), teamlogo=teamlogo, avatar=avatar, position=player['positions'][0].value,
                           apg=apg, spg=spg, bpg=bpg, rpg=rpg, ppg=ppg, gp=gp, fgpercentage=fgpercentage, ftpercentage=ftpercentage)
        return card

    def calculatePoints(self, ft, fg, three):
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
    apg = models.CharField(max_length=200)
    spg = models.CharField(max_length=200)
    bpg = models.CharField(max_length=200)
    rpg = models.CharField(max_length=200)
    ppg = models.CharField(max_length=200)
    fgpercentage = models.CharField(max_length=200)
    ftpercentage = models.CharField(max_length=200)
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
