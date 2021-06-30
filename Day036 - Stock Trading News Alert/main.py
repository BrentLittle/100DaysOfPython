
import requests


AV_APIKEY = "7O5YDWKRFQLZV8Z1"
NEWS_APIKEY = "a8424667c2764174bd2162cac1941554"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


#TODO 1. - Get yesterday's closing stock price. 
stockParams = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":AV_APIKEY,
}
response = requests.get(STOCK_ENDPOINT, params=stockParams)
data = response.json()["Time Series (Daily)"]
dataList = [value for (key,value) in data.items()]
yesterdayData = dataList[0]
yesterdayClosingPrice = yesterdayData["4. close"]


#TODO 2. - Get the day before yesterday's closing stock price
dayBeforeLastData = dataList[1]
dayBeforeLastClosingPrice = dayBeforeLastData["4. close"]


#TODO 3. - Find the positive difference between yesterday and the day before
posDifferenceInPrice = abs(float(yesterdayClosingPrice) - float(dayBeforeLastClosingPrice))


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diffPercent = posDifferenceInPrice/float(yesterdayClosingPrice)*100


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diffPercent > 1:
    
    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.    
    newsParams = {
        "q":COMPANY_NAME,
        "apiKey":NEWS_APIKEY,
    }
    
    response = requests.get(NEWS_ENDPOINT, params=newsParams)
    articles = response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    topThreeArticles = articles[:3]
  

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    articleBriefings = [f"Headline:{article['title']}. \nBrief: {article['description']}" for article in topThreeArticles]


#TODO 9. - Print out each of the articles 
for article in articleBriefings:
    print(f"{article}\n")