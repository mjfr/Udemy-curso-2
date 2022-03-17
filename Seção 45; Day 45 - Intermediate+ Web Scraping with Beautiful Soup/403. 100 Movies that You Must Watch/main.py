import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(markup=web_page, parser="html.parser")
movies_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

with open(file="movie.txt", mode="w") as data:
    for movie in movies_list[::-1]:
        data.write(f"{movie}\n")
