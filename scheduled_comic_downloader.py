#! python3
# scheduled_comic_downloader.py — An exercise in keeping time and scheduling.
# For more information, see project_details.txt.

import logging
import os
import requests
import bs4

# import lxml
import concurrent.futures

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def get_pizza_cake():
    pizza_cake = []
    res = requests.get("https://pizzacakecomic.com")
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for link in soup.find_all("img"):
        image_link = link.get("src")
        if image_link.endswith(".png"):
            pizza_cake.append(link.get("src"))
    os.makedirs("./pizza_cake", exist_ok=True)
    return pizza_cake


def download_comic(comic):
    res = requests.get(comic)
    res.raise_for_status()
    comic_name = comic.split("/")[-1]
    print(f"Downloading {comic_name} ...")
    with open(f"./pizza_cake/{comic.split('/')[-1]}", "wb") as f:
        for chunk in res.iter_content(100_000):
            f.write(chunk)


def check_pizza_cake():
    pizza_list = get_pizza_cake()

    existing_files = os.listdir("./pizza_cake")

    missing_pizza_cake = [
        file_name
        for file_name in pizza_list
        if file_name.split("/")[-1] not in existing_files
    ]

    if len(missing_pizza_cake) > 10:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(download_comic, missing_pizza_cake)
    else:
        for comic in missing_pizza_cake:
            download_comic(comic)


check_pizza_cake()
