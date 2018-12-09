import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import stringcase
import json
import os
# from teamcolors import teamcolors


def getAvatar(player, playerteam):
    browser = webdriver.Firefox()

    browser.get('http://qam.espn.go.com/nba/tools/lookup?method=headshots')

    teamelem = browser.find_element_by_xpath(
        f"//body/form/select[@name='teamId']/option[text()='{playerteam}']").click()
    playerelem = browser.find_element_by_link_text(player).click()
    avatarelem = browser.find_element_by_xpath("//div[@class='main-img']/img")
    avatarsrc = avatarelem.get_attribute('src')

    urllib.request.urlretrieve(
        avatarsrc, 'api/static/img/avatar_' + stringcase.snakecase(player) + '.png')
    browser.quit()


# jerseynumbers = {}


# def getJerseyNumbers(playerteam):
#     print('grabbing jersey number')
#     browser = webdriver.Firefox()

#     browser.get('http://qam.espn.go.com/nba/tools/lookup?method=headshots')

#     teamelem = browser.find_element_by_xpath(
#         f"//body/form/select[@name='teamId']/option[text()='{playerteam}']").click()
#     players = browser.find_elements_by_xpath("//body/table/tbody/tr")
#     for i, p in enumerate(players):
#         jerseynumbers[p.text.split(
#             '\n', 1)[0]] = p.text.split(' ', 2)[2]

#     browser.quit()


# for item in teamcolors:
#     try:
#         getJerseyNumbers(item)
#     except:
#         pass

# with open('listofnums.json', 'w') as f:
#     json.dump(jerseynumbers, f)
#     f.write(os.linesep)
