#! python3
# comicdldr_class.py — First try at OOP.

import logging
import os
import requests
import bs4

logging.basicConfig(
    level=logging.DEBUG,
    filename="class_logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


class Comic:
    def __init__(self, name, website):
        self.name = name
        self.website = website

    def get_comic(self):
        comic_list = []
        res = requests.get(self.website)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")

        for link in soup.find_all("img"):
            image_link = link.get("src")

            if image_link.endswith((".png", ".jpg", ".gif")):
                comic_list.append(link.get("src"))

        os.makedirs(f"./{self.name}", exist_ok=True)

        existing_files = os.listdir(f"./{self.name}")
        ignore_files = [
            "callout-store3.jpg",
            "ebookad410_fear.gif",
            "footerlogo.gif",
            "icon_chickens100.jpg",
            "icon_computer.jpg",
            "icon_random.gif",
            "LMRB4hero250.jpg",
            "mug.jpg",
            "Savage_Chickens_Logo.jpg",
            "wfacebook.gif",
            "wtvtropes.gif",
            "wtwitter.gif",
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


comic_1 = Comic("pizza_cake", "https://pizzacakecomic.com")
comic_2 = Comic("savage_chickens", "https://www.savagechickens.com")
comic_3 = Comic("wonderella", "https://nonadventures.com")

comic_1.get_comic()
comic_2.get_comic()
comic_3.get_comic()
