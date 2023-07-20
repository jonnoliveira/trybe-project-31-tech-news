from tech_news import database


def search_and_count_categories(data_news):
    categories = []
    categories__count = {}

    for new in data_news:
        categories.append(new["category"])
        if new["category"] not in categories__count:
            categories__count[new["category"]] = 1
        else:
            categories__count[new["category"]] += 1

    return {"categories": categories, "count": categories__count}


# Requisito 10
def top_5_categories():
    data_news = database.find_news()
    searched = search_and_count_categories(data_news)

    categories = searched["categories"]
    categories_count = searched["count"]

    if len(categories) < 5:
        return categories

    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    # https://stackoverflow.com/questions/24728933/sort-dictionary-alphabetically-when-the-key-is-a-string-name
    top_sorted_categories = sorted(
        categories_count.items(),
        key=lambda item: (-item[1], item[0].lower()),
    )[:5]

    top_5_categories = []
    for item in top_sorted_categories:
        top_5_categories.append(item[0])

    return top_5_categories
