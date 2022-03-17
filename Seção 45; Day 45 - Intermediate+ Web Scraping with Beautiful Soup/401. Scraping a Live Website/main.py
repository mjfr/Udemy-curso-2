from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
articles_texts = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

articles_scores = [int(score.getText().split(' ')[0]) for score in soup.find_all(name="span", class_="score")]

print(articles_texts)
print(articles_links)
print(articles_scores)

highest_score_index = articles_scores.index(max(articles_scores))
print(f"{articles_texts[highest_score_index]}\n{articles_links[highest_score_index]}")
