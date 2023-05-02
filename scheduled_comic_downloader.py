#! python3
# scheduled_comic_downloader.py — An exercise in keeping time and scheduling.
# For more information, see project_details.txt.

import logging
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
        image = link.get("src")
        if image.endswith(".png"):
            pizza_cake.append(link.get("src"))
    return pizza_cake


def download_comic_thread(comic):
    res = requests.get(comic)
    res.raise_for_status()
    comic_name = comic.split("/")
    print(f"Downloading {comic_name[-1]} ...")
    with open(f"{comic_name[-1]}.png", "wb") as f:
        for chunk in res.iter_content(100_000):
            f.write(chunk)


pizza_list = get_pizza_cake()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_comic_thread, pizza_list)
