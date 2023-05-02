#! python3
# scheduled_comic_downloader.py — An exercise in keeping time and scheduling.
# For more information, see project_details.txt.

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.
