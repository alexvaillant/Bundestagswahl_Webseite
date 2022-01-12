from Web_Crawler.Crawler_Info_Collector import Crawler_Info_Getter

basic_url = "https://www.wahlrecht.de/umfragen/"

class Crawler_Info_Cleaner():
    def __init__(self, partylist, partyresults):
        self.partylist = partylist
        self.partyresults = partyresults

    def result_splitter(self): # Ordnet die Ergebnisse unterteilt, in die der Parteien in eigenständige Listen innerhalb einer großen Liste ein
        ordered_results = [[] for i in range(0, len(self.partylist))]
        new_raw_results = []
        old_results = []
        for element in self.partyresults: # übernimmt die Ergebnisse, und vereinfacht die Strings, sodass diese floats bzw. ints werden können
            cur = element.replace(" %", "")
            new_raw_results.append(cur.replace(",", "."))

        j = 0
        i = 0
        while j < len(new_raw_results): # sortiert die ungeordnete new_raw_results-liste in geordnete Listenelemente einer Liste ein
            if (j + 1) % 9 != 0:
                ordered_results[i].append(new_raw_results[j])
            else:
                old_results.append(new_raw_results[j])
                i = i + 1
            j = j + 1

        return ordered_results