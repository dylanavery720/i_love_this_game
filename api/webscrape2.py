import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import stringcase
import json
import os
from teamcolors import teamcolors


def getLogos():
    browser = webdriver.Firefox()

    browser.get(
        'https://en.wikipedia.org/wiki/National_Basketball_Association#Teams')
    for team in teamcolors:
        try:
            teamelem = browser.find_element_by_xpath(
                f"//*[@title='{team}']").click()
            logoelem = browser.find_element_by_xpath(
                f"//*[@alt='{team} logo']")
            logosrc = logoelem.get_attribute('src')
            urllib.request.urlretrieve(
                logosrc, 'api/static/img/' + stringcase.snakecase(team) + '.png')
        except:
            print('failed', team)
            pass
    browser.quit()


# def getActionPhotos():
    # need to find a source, 450 x 300 or bigger, refer to notes..
    # urllib.request.urlretrieve(
    #     actionsrc, 'api/static/img/' + stringcase.snakecase(player['name']) + '.jpg')


getLogos()
