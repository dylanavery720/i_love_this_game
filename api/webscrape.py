import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import stringcase


def getAvatar():
    player = 'Vince Carter'
    playerteam = "Atlanta Hawks"

    browser = webdriver.Firefox()

    browser.get('http://qam.espn.go.com/nba/tools/lookup?method=headshots')

    teamelem = browser.find_element_by_xpath(
        f"//body/form/select[@name='teamId']/option[text()='{playerteam}']").click()
    playerelem = browser.find_element_by_link_text(player).click()
    avatarelem = browser.find_element_by_xpath("//div[@class='main-img']/img")
    avatarsrc = avatarelem.get_attribute('src')
    print(avatarsrc)
    print('api/static/img/avatar_' + stringcase.snakecase(player) + '.png')

    # urllib.request.urlretrieve(
    #     avatarsrc, 'api/static/img/avatar_' + stringcase.snakecase(player) + '.png')
    browser.quit()


getAvatar()
