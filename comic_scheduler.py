#! python3
# comic_scheduler.py — An exercise in scheduling.

import time
import schedule
from comic import Comic

pizza_cake = Comic("pizza_cake", "https://pizzacakecomic.com", ".png")
savage_chickens = Comic("savage_chickens", "https://www.savagechickens.com", ".jpg")
wonderella = Comic("wonderella", "https://nonadventures.com", ".png")

THE_LIST = [pizza_cake, savage_chickens, wonderella]
THE_TIME = "11:30"


def get_comic(comics):
    """Download any missing comics from website's front page."""
    for comic in comics:
        comic_list = comic.get_comic_list()
        comic.download_new_comics(comic_list)


schedule.every().tuesday.at(THE_TIME).do(get_comic, comic_list=THE_LIST)

while True:
    schedule.run_pending()
    time.sleep(1)
