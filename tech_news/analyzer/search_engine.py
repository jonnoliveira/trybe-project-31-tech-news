from tech_news import database


# Requisito 7
def search_by_title(title):
    # https://www.mongodb.com/docs/v6.0/reference/operator/query/regex/
    news_list = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    result = []

    if news_list:
        for new in news_list:
            item = f"{new['title']}", f"{new['url']}"
            result.append(item)
        return result

    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
