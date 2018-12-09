import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import stringcase
import csv


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


listofnums = []


def getJerseyNumber(player, playerteam):
    print('grabbing jersey number')
    browser = webdriver.Firefox()

    browser.get('http://qam.espn.go.com/nba/tools/lookup?method=headshots')

    teamelem = browser.find_element_by_xpath(
        f"//body/form/select[@name='teamId']/option[text()='{playerteam}']").click()
    playerelem = browser.find_element_by_link_text(player).click()
    jersey = browser.find_element_by_xpath(
        "//div[@class='ih-left-container']/h2")

    # write jersey to file so that they dont get lost
    with open('listofnums.cv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=[player])
            writer.writerow(player, jersey.text.split(' ', 1)[0] )

    browser.quit()
    return entry
    # return jersey.text.split(' ', 1)[0]


# Should have this just scrape every time and fill a file with their name and number, doesnt need to be iterative
getJerseyNumber('Jimmy Butler', "Philadelphia 76ers")
getJerseyNumber('John Wall', "Washington Wizards")

