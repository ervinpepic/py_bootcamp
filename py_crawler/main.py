import requests
from bs4 import BeautifulSoup

respo = requests.get("https://stackoverflow.com/questions")
beautiful_soup4 = BeautifulSoup(respo.text, "html.parser")

question_list = beautiful_soup4.select(".question-summary")
for q in question_list:
    print(q.select_one(".question-hyperlink").getText())
    print(q.select_one(".vote-count-post").getText())