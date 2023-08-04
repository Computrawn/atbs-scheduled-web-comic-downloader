import logging
import requests
import bs4

logging.basicConfig(
    level=logging.DEBUG,
    filename="selector_logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
# logging.disable(logging.CRITICAL)  # Note out to enable logging.


def get_pizza_cake():
    """Get list of urls from first page of site and create directory for storage."""
    pizza_list = []
    res = requests.get("https://pizzacakecomic.com/", timeout=10)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for link in soup.select(".post"):
        logging.info(link.a.img["src"])
        pizza_list.append(link.a.img["src"])

    # os.makedirs(f"./{self.name}", exist_ok=True)
    return pizza_list


def get_savage_chickens():
    """Get list of urls from first page of site and create directory for storage."""
    savage_list = []
    res = requests.get("https://www.savagechickens.com/", timeout=10)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    for link in soup.select(".entry_content"):
        logging.info(link.p.img["src"])
        savage_list.append(link.p.img["src"])

    # os.makedirs(f"./{self.name}", exist_ok=True)
    return savage_list


pizza_comics = get_pizza_cake()
logging.info(pizza_comics)

savage_comics = get_savage_chickens()
logging.info(savage_comics)
