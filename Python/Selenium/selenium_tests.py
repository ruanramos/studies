from selenium import webdriver
import time

#usr = input('Enter your username or email id: ')
#pwd = getpass('Enter your password : ')

players = ['lelks', 'bagleri', 'pombo alienigena', 'puporr4uga', 'frozenfrost', 'lagega']
driver = webdriver.Chrome('C:/Users/ruanr/Desktop/chromedriver.exe')

for player in players:
    driver.get('https://br.op.gg/')
    player_box = driver.find_element_by_class_name('summoner-search-form__text')
    player_box.send_keys(player)
    submit_btn = driver.find_element_by_class_name('summoner-search-form__button')
    submit_btn.submit()

    rank = driver.find_element_by_class_name("TierRank")
    points = driver.find_element_by_class_name("LeaguePoints")
    print(player, rank.text, points.text)

driver.get('https://mail.google.com')

time.sleep(10)

driver.quit()