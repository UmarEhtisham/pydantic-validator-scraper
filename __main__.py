"""
Episode Scraper for TalkPython API Client

This script fetches and parses episode data from the TalkPython API, converts it into `Episode` model instances, and allows searching by title.

Usage:
------
1. Ensure `config` is properly set up with `base_url` and `episodes_path`.
2. Run the script:
   ```bash
   python scraper.py
   ```
3. Enter a search term when prompted to filter episodes by title.

Dependencies:
-------------
- requests
- BeautifulSoup (bs4)
- pydantic

Example:
--------
Input: "Python"
Output: List of episodes with "Python" in the title.
"""

import requests 
from bs4 import BeautifulSoup, Tag
from config import config
from model import Episode
from pprint import pprint

def extract_episode_data(row: Tag) -> dict:
    """
    Extracts episode data from an HTML row element.

    Args:
        row (Tag): A BeautifulSoup Tag representing a table row.

    Returns:
        dict: A dictionary containing episode attributes.
    """
    model_data = {}
    row_data = row.select('td')

    for i, td in enumerate(row_data):
        if i == 0:
            model_data['show_number'] = td.text.replace('#', '').strip()
        elif i == 1:
            model_data['date'] = td.text.strip()
        elif i == 2:
            link = td.find('a')
            model_data['url'] = config.base_url + link.attrs['href']
            model_data['title'] = link.text.strip()
        elif i == 3:
            model_data['guest'] = td.text.strip()

    return model_data

# Fetch page content
response = requests.get(config.page_url)
soup = BeautifulSoup(response.text, "html.parser")

# Parse rows from the episodes table
rows = soup.select('tbody > tr')

episodes = [Episode(**extract_episode_data(row)) for row in rows]

# Search functionality
search_term = input("Enter search term: ")
search_results = [episode for episode in episodes if search_term.lower() in episode.title.lower()]

# Display search results
pprint(search_results)
