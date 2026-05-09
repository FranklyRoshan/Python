import requests
from bs4 import BeautifulSoup, element

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

movies = soup.find_all("div", class_="article-title-description__text")

movies_list = []
for movie in movies:
    element = str(movie.find("h3").get_text("title"))
    movies_list.append(element)

# 1. list.reverse() – In-place reversal
# Modifies the original list:
movies_list.reverse()
# 2. Slicing – Create a reversed copy
# Uses [::-1]:
# movies_list = movies_list[::-1]
# 3. reversed() – Iterator-based
# Returns an iterator:
# movies_list = list(reversed(movies_list))

with open("movies.txt", mode="w", encoding='utf-8', errors='replace') as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
