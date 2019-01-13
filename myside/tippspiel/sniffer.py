from bs4 import BeautifulSoup
import requests
from re import compile
from subprocess import call


def getSoup(url):
    call(["curl", url, "-o", "soup.html"])
    with open("soup.html") as file:
        soup = BeautifulSoup(file.read(), "html5lib")
        return soup


def newEvent(url):
    pattern = compile(r"https://www\.hltv\.org/events/\d{4}/.+")
    if pattern.match(url):
        try:
            soup = getSoup(url)
            name = soup.find("div", class_="eventname").text
            id = soup.find(
                "a", class_="event-nav active")["href"].split("/")[2]
            return name, id
        except:
            return ("", -1)

    else:
        return ("", -1)


def getMatches(id):
    url = r"https://www.hltv.org/matches?event="+str(id)
    soup = getSoup(url)
    matches = list()
    for match in soup.find_all("a", class_="a-reset block upcoming-match standard-box"):
        matches.append("https://www.hltv.org"+match["href"])
    return matches


def getResult(url):
    soup = getSoup(url)
    if soup.find("div", class_="countdown").get_text() == "Match over":
        if soup.find("div", class_="team1-gradient").div["class"] == "won":
            result = [True, 0]
        else:
            result = [True, 1]
    else:
        result = [False, -1]
    return result


def getMatch(url):
    soup = getSoup(url)
    id = url.split("/")[4]
    team1 = soup.find("div", class_="team1-gradient").div.get_text()
    team2 = soup.find("div", class_="team2-gradient").div.get_text()
    return {"team1": team1, "team2": team2, "id": id}
