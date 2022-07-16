from bs4 import BeautifulSoup
import lxml

import requests

r = requests.get("https://news.ycombinator.com/news")
yc_webpage = r.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)
print(article_texts[max_index])
print(article_links[max_index])
print(max_upvotes)



















#
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# all_anchor = soup.find_all(name="a")
# # for tag in all_anchor:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# company_url_sel = soup.select_one(selector="#name")
# select_classes = soup.select(".heading")
# # print(select_classes)

