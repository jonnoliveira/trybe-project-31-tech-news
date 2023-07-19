from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        for _ in range(5):
            response = requests.get(
                url, headers={"user-agent": "Fake user-agent"}
            )
            if response.status_code == 200:
                return response.text
            time.sleep(1)

    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    items = selector.css(".entry-title")

    news_list = []

    for news in items:
        links = news.css("a::attr(href)").get()
        news_list.append(links)

    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".nav-links a.next::attr(href)").get()

    if next_page_link is None:
        return None

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
