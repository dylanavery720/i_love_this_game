from django.db import models
import stringcase
from basketball_reference_web_scraper import client
from api.webscrape import getAvatar
from api.teamcolors import teamcolors
from api.jerseynumbers import jerseynumbers
from django.urls import reverse


# Once deployed Database should be updated every day so that cards stay up to date...
# season_totals_2017 = client.players_season_totals(season_end_year=2018)
# season_totals_2016 = client.players_season_totals(season_end_year=2017)


class CardManager(models.Manager):
    def create_card(self, id, player):
        # print out Jimmy Butlers whole team object and try to access 76ers, [-1?]
        try:
            jersey = jerseynumbers[player['name']]
        except:
            jersey = "00"
        teamlogo = 'img/' + \
            stringcase.snakecase(player['team'].value.title()) + '.png'
        avatar = 'img/avatar_' + stringcase.snakecase(player['name']) + '.png'
        photo = 'img/' + stringcase.snakecase(player['name']) + '.jpg'
        points = self.calculatePoints(
            player['made_free_throws'], player['made_field_goals'], player['made_three_point_field_goals'])
        apg = "{:.1f}".format(player['assists'] / player['games_played'])
        spg = "{:.1f}".format(player['steals'] / player['games_played'])
        bpg = "{:.1f}".format(player['blocks'] / player['games_played'])
        rpg = "{:.1f}".format(
            (player['offensive_rebounds'] + player['defensive_rebounds']) / player['games_played'])
        ppg = "{:.1f}".format(points / player['games_played'])
        fgpercentage = "{0:.1%}".format(
            player['made_field_goals'] / player['attempted_field_goals'])[:-1]
        ftpercentage = "{0:.1%}".format(
            player['made_free_throws'] / player['attempted_free_throws'])[:-1]
        gp = '%02d' % player['games_played']
        lastname = player['name'].split(' ', 1)[0]
        firstname = player['name'].split(' ', 1)[1]
        position = "".join([word[0]
                            for word in player['positions'][0].value.split()])
        team = self.getTeam(player['team'].value.title())
        if player['name'] == 'Jimmy Butler':
            print(teamcolors[player['team'].value.title()])
        teamcolor = teamcolors[player['team'].value.title()]
        card = self.create(id=id, name=player['name'], age=player['age'], team=team, teamlogo=teamlogo, avatar=avatar, photo=photo, position=position,
                           apg=apg, spg=spg, bpg=bpg, rpg=rpg, ppg=ppg, gp=gp, fgpercentage=fgpercentage, ftpercentage=ftpercentage, firstname=firstname.upper(), lastname=lastname.upper(), teamcolor=teamcolor, jersey=jersey)
        return card

    def calculatePoints(self, ft, fg, three):
        return (ft + ((fg-three) * 2) + (three * 3))

    def getTeam(self, team):
        teamprefix = team.split(' ', 1)[0]
        if teamprefix == 'Los':
            return team.split(' ', 2)[2]
        if 3 < len(team.split(' ', 1)[0]) <= 6:
            return team.split(' ', 1)[0]
        return team[:6]


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
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fgpercentage = models.CharField(max_length=200)
    ftpercentage = models.CharField(max_length=200)
    gp = models.CharField(max_length=200)
    teamcolor = models.CharField(max_length=200)
    jersey = models.CharField(max_length=200)

    objects = CardManager()

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])

    def get_front_url(self):
        return reverse('front_detail', args=[str(self.id)])

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
                print('fail')
                # self.objects.all().delete()
        return my_cards
