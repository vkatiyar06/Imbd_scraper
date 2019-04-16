from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import requests
import time
import datetime
from dateutil import parser
from mailing import mailer
from savetodb import savetomysqldb

message = []


def find_status(link):
    res = requests.get(link)
    html = res.content
    soup = BeautifulSoup(html, "html5lib")

    for i in soup.find_all("div", {"class": "list_item"}):
        dt = re.sub(r"\s+", " ", str(i.find("div", {"class": "airdate"}).text))
        d_current = datetime.datetime.now()
        if(dt != " "):
            if(len(re.findall(r"\d+", dt)) == 2):
                if(d_current < parser.parse(str(dt))):
                    message.append(
                        "The next episode airs on " + parser.parse(dt).date())
                    return
            else:
                if(d_current.strftime("%Y") <= parser.parse(dt).strftime("%Y")):
                    message.append("The next season begins in " + dt)
                    return
        else:
            message.append("No info available")


def getLatestlink(link):
    res = requests.get(link)
    html = res.content
    soup = BeautifulSoup(html, "html5lib")
    chk1 = soup.find('div', {"class": "subtext"})
    sub_text = chk1.find_all("a")[-1].text
    rex = re.findall(r"\d{4}", sub_text)
    if(len(rex) == 2):
        message.append("TV series has finished streaming all its episodes.")
    else:
        first = (soup.find("div", {"class": "seasons-and-year-nav"}))
        sub = (first.find_all("div")[2])
        link_last = ("https://www.imdb.com" +
                     sub.find("a").get("href").split('&')[0])
        find_status(link_last)


def imdb_scrapper(query):
    path = "https://www.google.com/search?q="+str(query)+" tv series imdb"
    r = requests.get(path)
   
    html = r.content
    soup = BeautifulSoup(html, "html5lib")
    first = ((soup.find("div", attrs={"class": "g"})))
    first_sub = (first.find("h3", attrs={"class": "r"}))
    link = (first_sub.find("a").get("href").replace("/url?q=",
                                                    "").split('&sa')[0])

    getLatestlink(link)


# example => q = "game of thrones,friends,sherlock holmes"

def run():
    receiver = input("Enter email (receiver) :- ")
    raw_q = input("Enter comma seperated query(TV series):- ")
    query = raw_q.split(",")
    for i in range(len(query)):
        imdb_scrapper(query[i])
    # print(message)
    mailer(receiver, query, message)
    savetomysqldb(raw_q, receiver)


run()
