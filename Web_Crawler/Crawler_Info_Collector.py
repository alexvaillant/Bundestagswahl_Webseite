import requests
from bs4 import BeautifulSoup
import time

regulars = ["CDU/CSU", "SPD", "GRÜNE", "FDP", "DIE LINKE", "AfD", "Sonstige"]
basic_url = "https://www.wahlrecht.de/umfragen/"

def get_htmldoc(url): # Die Funktion erhält eine url und gibt den html-code der Webseite als BeautifulSoup-Datei wieder zurück
    time.sleep(0.5)
    r = requests.get(url)
    doc = BeautifulSoup(r.text, 'html.parser')
    return doc


class Crawler_Info_Getter():
    def __init__(self, url):
        self.url = url

    def get_partylist(self): # Die Funktion erhält die BeautifulSoup-Datei und sucht, die Namen und die Reihenfolge, der wichtigsten Parteien
        doc = get_htmldoc(self.url)
        partylist = []

        for li in doc.select(".li"):
            partyname = li.text
            if partyname in regulars:
                partylist.append(partyname)

        return partylist


    def get_partyresults(self): # Die Funktion erhält die BeautifulSoup-Datei und sucht, nach den Werte, der Umfrage-Ergebnisse, der Institute
        doc = get_htmldoc(self.url)
        raw_results = []

        compressed = doc.find_all('td')
        for element in compressed:
            single_result = element.text
            if "%" in single_result:
                raw_results.append(single_result)

        return raw_results