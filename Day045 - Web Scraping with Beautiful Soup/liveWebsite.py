from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")


articles = soup.find_all(name="a", class_="storylink")

articleTexts, articleLinks = [], []
for articleTag in articles:
    articleTexts.append(articleTag.getText())
    articleLinks.append(articleTag.get("href"))

articleUpvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# print(articleTexts)
# print(articleLinks)
# print(articleUpvotes)

indexOfLargestUpvotes = articleUpvotes.index(max(articleUpvotes))

print(articleTexts[indexOfLargestUpvotes])
print(articleLinks[indexOfLargestUpvotes])
print(articleUpvotes[indexOfLargestUpvotes])