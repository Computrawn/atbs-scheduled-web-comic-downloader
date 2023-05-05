#! python3
# scheduled_comic_downloader.py — An exercise in keeping time and scheduling.
# For more information, see project_details.txt.

import logging
import os
import time
import schedule
import requests
import bs4

logging.basicConfig(
    level=logging.DEBUG,
    filename="class_logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


class Comic:
    """Create Comic class."""

    def __init__(self, name, website, extension):
        self.name = name
        self.website = website
        self.extenstion = extension

    def get_comic(self):
        """Download comics from designated site."""
        comic_list = []
        res = requests.get(self.website)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")

        for link in soup.find_all("img"):
            image_link = link.get("src")
            if image_link.endswith(self.extenstion):
                comic_list.append(link.get("src"))

        os.makedirs(f"./{self.name}", exist_ok=True)

        existing_files = os.listdir(f"./{self.name}")
        ignore_files = [
            "callout-store3.jpg",
            "icon_chickens100.jpg",
            "icon_computer.jpg",
            "LMRB4hero250.jpg",
            "mug.jpg",
            "Savage_Chickens_Logo.jpg",
            "ebook_ad4102.jpg",
        ]
        missing_files = [
            file_name
            for file_name in comic_list
            if file_name.split("/")[-1] not in ignore_files
            if file_name.split("/")[-1] not in existing_files
        ]

        for comic in missing_files:
            comic_res = requests.get(comic)
            comic_res.raise_for_status()
            comic_name = comic.split("/")[-1]
            print(f"Downloading {comic_name} ...")
            with open(f"./{self.name}/{comic_name}", "wb") as f:
                for chunk in comic_res.iter_content(100_000):
                    f.write(chunk)


Pizza_Cake = Comic("pizza_cake", "https://pizzacakecomic.com", ".png")
Savage_Chickens = Comic("savage_chickens", "https://www.savagechickens.com", ".jpg")
Wonderella = Comic("wonderella", "https://nonadventures.com", ".png")

schedule.every().friday.at("14:40").do(Pizza_Cake.get_comic)
schedule.every().friday.at("14:45").do(Savage_Chickens.get_comic)
schedule.every().friday.at("14:50").do(Wonderella.get_comic)


while True:
    schedule.run_pending()
    time.sleep(1)
