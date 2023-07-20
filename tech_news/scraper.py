from parsel import Selector
import requests
import time
from tech_news.database import create_news


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
    selector = Selector(text=html_content)

    # https://stackoverflow.com/questions/52849274/getting-the-current-url-page-ref-scrapy
    url = selector.css("link[rel=canonical]::attr(href)").get()

    title = (
        selector.css(".entry-header-inner h1.entry-title::text").get().rstrip()
    )

    timesstamp = selector.css("ul.post-meta li.meta-date::text").get()

    writer = selector.css(
        "ul.post-meta li.meta-author span.author a::text"
    ).get()

    """ 
    r'\d+'": O operador "+" faz diferença. Sem ele indicamos a representação
    de um unico caracter numérico;
    já com ele indicamos a representação de um ou mais caracteres numéricos
    em sequência.
    """
    reading_time = int(
        selector.css("ul.post-meta li.meta-reading-time::text").re_first(
            r"\d+"
        )
    )

    # https://developer.mozilla.org/en-US/docs/Web/CSS/:first-of-type
    # https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator
    summary = "".join(
        selector.css("div.entry-content > p:first-of-type *::text").getall()
    ).strip()

    category = selector.css(
        ".meta-category a.category-style span.label::text"
    ).get()

    return {
        "url": url,
        "title": title,
        "timestamp": timesstamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://blog.betrybe.com/")
    news_list = scrape_updates(html_content)
    news_db = []

    while amount > len(news_list):
        new_link = scrape_next_page_link(html_content)
        html_content = fetch(new_link)
        news_list.extend(scrape_updates(html_content))

    for news in news_list:
        html_content = fetch(news)
        news_db.append(scrape_news(html_content))

    create_news(news_db[:amount])

    return news_db[:amount]
