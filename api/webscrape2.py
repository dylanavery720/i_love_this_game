import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import stringcase
import json
import os
# from teamcolors import teamcolors


def getLogos():
    # for each team in teamcolors go to wikipedia page for that team and download its svg
    # urllib.request.urlretrieve(
    #     logossrc, 'api/static/img/' + stringcase.snakecase(player['team'].value.title()) + '.png')


def getActionPhotos():
    # need to find a source, 450 x 300 or bigger, refer to notes..
    # urllib.request.urlretrieve(
    #     actionsrc, 'api/static/img/' + stringcase.snakecase(player['name']) + '.jpg')
