from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Startseite():
    return render_template("start.html")

@app.route("/Sonntagsfrage")
def Sonntagsfrage():

    poll_result = {}
    with open("data/data.txt", 'r') as file: # Entnimmt die Umfrage-ergebnis der Datenbank und wandelt es in ein Dictionary um
        for line in file:
            line_compresssed = line.strip().split(",")
            if float(line_compresssed[1]) % 1 == 0: # Verschönerung falls z.B. Schnitt 16.0 ist, dass 16 angezeigt wird
                poll_result[line_compresssed[0]] = int(float(line_compresssed[1]))
            else:
                poll_result[line_compresssed[0]] = line_compresssed[1]

    return render_template("sonntagsfrage.html", pollresult=poll_result)