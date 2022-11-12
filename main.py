import requests
from bs4 import BeautifulSoup

from duckduckgo_search import ddg


def google(keywords):

    # to search
    query = "Sukha Yoga Berlin"

    results = search(query, tld="co.in", num=10, stop=10, pause=2)

    print("Google Search Results", len(results))

    """
    searchUrl = "https://www.google.com/search?q=test"

    res = requests.get(searchUrl)
    if not res.ok:
        return

    raw_html = res.text

    html = BeautifulSoup(raw_html, 'html.parser')

    print(html)

    found = html.find('div', {'id': 'rso'})
    """


def duckduckgo(keywords):
    keywords = 'Bella Ciao'
    results = ddg(keywords,
                  safesearch='Moderate', time='y', max_results=25)
    print("DuckDuckGo Search Results", len(results))


def bing():
    searchUrl = "https://www.bing.com/search?q=sukha+yoga+berlin"

    res = requests.get(searchUrl)
    if not res.ok:
        return

    raw_html = res.text

    html = BeautifulSoup(raw_html, 'html.parser')

    print(html)


# bing()


google('dia mat')
duckduckgo('dia mat')
