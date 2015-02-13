''' 
Solution from Udacity to the nytimes.py code

'''

def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]

    for article in data:
        section = article["section"]
        title = article["title"]
        titles.append({section: title})
        if "media" in article:
            for m in article["media"]:
                for mm in m["media-metadata"]:
                    if mm["format"] == "Standard Thumbnail":
                        urls.append(mm["url"])
    return (titles, urls)