from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def start():
    #Instead of that:
    #return "<form action='reversed' method='get'><input name='rev'></input></form>" 
    return render_template("start.html")

@app.route("/search")
def search():
    if not 'rev' in request.args:
        return render_template("start.html")
    else:
    #getting the input
    #tokenizing it
    #pulling out the tokenized words from index
    #printing out the results
        rev = request.args['rev']
        a = [ rev, rev, rev]
        return render_template('search.html', result = a, rev = rev)
        