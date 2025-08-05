
from flask import Flask, request, jsonify
import app.arxiv_fetcher as arxiv_fetcher

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    topic = request.json.get('topic')
    papers = arxiv_fetcher.search_arxiv(topic)
    return jsonify(papers)

if __name__ == '__main__':
    app.run(debug=True)
