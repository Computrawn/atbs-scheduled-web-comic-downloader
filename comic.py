#! python3
# comic.py — An exercise in writing a Class.
# For more information, see project_details.txt.

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
    """Create Comic class."""

    def __init__(self, name, website, extension):
        self.name = name
        self.website = website
        self.extenstion = extension

    def get_comic_list(self):
        """Get list of urls from first page of site and create directory for storage."""
        comic_list = []
        res = requests.get(self.website, timeout=10)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")

        for link in soup.find_all("img"):
            image_link = link.get("src")
            if image_link.endswith(self.extenstion):
                comic_list.append(link.get("src"))

        os.makedirs(f"./{self.name}", exist_ok=True)
        return comic_list

    def download_new_comics(self, comic_list):
        """Download files not already in folder or ignore_files list."""
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
