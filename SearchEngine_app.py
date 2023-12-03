from flask import Flask, request, render_template
from crawler import index, search 


app = Flask(__name__)

@app.route("/")
def start():
    return render_template("start.html")

@app.route("/search")
def search_results():
    if not 'rev' in request.args:
        return render_template("start.html")
    else:
    #getting the input
        rev = request.args['rev']
    
    #pulling out the tokenized words from index
        result = search (index, rev)
        filtered_results = []
        for i in result: 
            if i not in filtered_results:
                filtered_results.append(i)
            
    #printing out the results
        return render_template('search.html', result = filtered_results, rev = rev)
        