#! python3
# comic_scheduler.py — An exercise in scheduling.

import time
import schedule
from comic import Comic

pizza_cake = Comic("pizza_cake", "https://pizzacakecomic.com", ".png")
savage_chickens = Comic("savage_chickens", "https://www.savagechickens.com", ".jpg")
wonderella = Comic("wonderella", "https://nonadventures.com", ".png")


def get_pizza_cake():
    the_list = pizza_cake.get_comic_list()
    pizza_cake.download_new_comics(the_list)


def get_savage_chickens():
    the_list = savage_chickens.get_comic_list()
    savage_chickens.download_new_comics(the_list)


def get_wonderella():
    the_list = wonderella.get_comic_list()
    wonderella.download_new_comics(the_list)


schedule.every().monday.at("13:57").do(get_pizza_cake)
schedule.every().monday.at("14:00").do(get_savage_chickens)
schedule.every().monday.at("13:45").do(get_wonderella)


while True:
    schedule.run_pending()
    time.sleep(1)
