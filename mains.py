from flask import Flask, jsonify
import requests
API_KEY = "16fe1ec6122c49088cb49d432192f97a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-03-29&sortBy=publishedAt&apiKey=16fe1ec6122c49088cb49d432192f97a"

app = Flask(__name__)

@app.route("/")
def get_news():
    response = requests.get(url)
    data = response.json()
    total_articles = len(data["articles"])
    first_article = data["articles"][0]
    author = first_article["author"]
    published_at = first_article["publishedAt"]
    output_data = {"total_articles": total_articles,
                       "first_article_author": author,
                        "first_article_published_at": published_at}
    return jsonify(output_data)
            
if __name__ == "__main__":
    app.run(debug=True)
