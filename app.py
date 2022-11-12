from flask import Flask, render_template, jsonify, request
from googlesearch import search
from urllib.parse import urlparse
from duckduckgo_search import ddg
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/google', methods=['POST'])
def google():
    query = request.args.get('query')
    targetUrl = request.args.get('targetUrl')

    targetUrl = urlparse(targetUrl).netloc

    results = []
    for res in search(query, num=25, stop=25, pause=2):
        results.append(res)

    ranking = -1
    for index, res in enumerate(results):
        url = urlparse(res).netloc
        if url == targetUrl and (index+1 < ranking or ranking == -1):
            ranking = index+1

    apiResults = results

    return jsonify({'ranking': ranking,
                    'results': apiResults})


@app.route('/duckduckgo', methods=['POST'])
def duckduckgo():
    query = request.args.get('query')
    targetUrl = request.args.get('targetUrl')

    targetUrl = urlparse(targetUrl).netloc

    results = ddg(query,
                  safesearch='Moderate', time='y', max_results=25)

    apiResults = []

    ranking = -1
    for index, res in enumerate(results):
        apiResults.append(res['href'])
        url = urlparse(res['href']).netloc
        if url == targetUrl and (index+1 < ranking or ranking == -1):
            ranking = index+1

    return jsonify({'ranking': ranking,
                    'results': apiResults})
