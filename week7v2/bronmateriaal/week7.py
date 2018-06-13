from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route('/')
def index():

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/showScores')
def show_scores():
    list_scores = lees_scores("Scores.txt")
    return render_template("scores.html", scores=list_scores)

@app.route('/toonScore/<naam>')
def toonScore(naam):
    list_scores = lees_scores("Scores.txt")
    for score in list_scores:
        if score[0] == naam:
            student = score
    return render_template("toonScore.html", student = student)

def lees_scores(bestandsnaam):
    import os.path
    list_scores = []
    try:
        fo = open(os.path.dirname(os.path.abspath(__file__))+"/static/files/" + )