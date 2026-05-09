# ===============================================================
# Web Scraping
# ===============================================================
from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# Find all elements with class 'titleline'
titlelines = soup.find_all("span", class_="titleline")

# Extract and print the text from each title link
article_text = []
article_link = []
for titleline in titlelines:
    title = titleline.find("a").get_text()
    article_text.append(title)
    title = titleline.find("a").get("href")
    article_link.append(title)
# print(article_text)
# print(article_link)

scores = soup.find_all("span", class_="subline")
article_upvote = []
for score in scores:
    point = int(score.find("span").get_text("score").split()[0])
    article_upvote.append(point)
# print(article_upvote)

max = 0
for num in article_upvote:
    if num > max:
        max = num
max_index = article_upvote.index(max)
print(f"The Highest Rated Title: {article_text[max_index]}\n"
      f"Title link: {article_link[max_index]}")




# ===============================================================
# Parsing HTML & Making soup
# Finding and selecting Particular Element with Beautiful Soup
# ===============================================================
#
# with open("/Web Development Project/Beautiful Soup Project/website.html") as file:
# # with open("website.html") as file:
#     content = file.read()
#     # print(content)
#
# soup = BeautifulSoup(content, "html.parser")
# # soup = BeautifulSoup(content, "lxml")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.a)
#
# all_anchor_tag = soup.find_all(name="a")
# # print(all_anchor_tag)
#
# # for tag in all_anchor_tag:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# specific_id = soup.find(name="h1", id="name")
# # print(specific_id)
#
# # class attribute
# specific_class = soup.find(name="h3", class_="heading")
# # print(specific_class)
#
# name = soup.select_one("#name")
# # print(name)
#
# headings = soup.select(".heading")
# # print(headings)

# tag_in_a_tag = soup.select("ul li")
# print(tag_in_a_tag)