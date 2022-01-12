from Web_Crawler.Crawler_Info_Cleaner import Crawler_Info_Cleaner
from Web_Crawler.Crawler_Info_Collector import Crawler_Info_Getter

basic_url = "https://www.wahlrecht.de/umfragen/"

def get_result(): # berrechnet aus den in Web_Crawler ersuchten Daten den Durschnitt für jede Partei und gibt diese als Dictionary mit Parteiname als Key zurück
    Wahl = Crawler_Info_Getter(basic_url)
    partylist = Wahl.get_partylist()
    partyresults = Wahl.get_partyresults()
    richtige_Wahl = Crawler_Info_Cleaner(partylist, partyresults)
    ergebnisse = richtige_Wahl.result_splitter()
    Schnittergebnis = {}

    for li in ergebnisse: # verwerfe Element, ersetze es durch Sonstige-Ergebnisse
        for element in li:
            if "FW 2Son. 6" == element:
                li.remove("FW 2Son. 6")
                li.append("6")

    k = 0
    i = 0
    res = 0
    print(ergebnisse)
    for li in ergebnisse: # Schleife berrechnet Schnitt und ordnet Wert die Partei zu
        for element in ergebnisse[i]:
            res = res + float(element)
            k = k + 1
        Schnittergebnis[partylist[i]] = round(res/k, 1)
        res = 0
        k = 0
        i = i + 1

    print(Schnittergebnis)

    return Schnittergebnis

# Beispielausführung um Ergebnisse zu drucken:
result = get_result()
print(result)

with open ("../Webseite/data/data.txt", 'w') as file: # Ergebnisse in die Datenkbank schreiben
    result = get_result()
    for element in result:
        file.write(element + "," + str(result[element]) + "\n")