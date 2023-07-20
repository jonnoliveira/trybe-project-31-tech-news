from tech_news import database
import datetime


def iterating_over_the_data(news_list):
    result = []

    for new in news_list:
        item = f"{new['title']}", f"{new['url']}"
        result.append(item)
    return result


# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def validate_date(date):
    try:
        datetime.datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 7
def search_by_title(title):
    # https://www.mongodb.com/docs/v6.0/reference/operator/query/regex/
    news_list = database.search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )

    if news_list:
        return iterating_over_the_data(news_list)

    return news_list


# Requisito 8
def search_by_date(date):
    validate_date(date)

    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    date_correction = datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
        "%d/%m/%Y"
    )

    news_list = database.search_news(
        {"timestamp": {"$regex": date_correction}}
    )

    if news_list:
        return iterating_over_the_data(news_list)

    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
