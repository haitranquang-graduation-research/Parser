from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery

app = Flask(__name__)
api = Api(app)
print('Hello')

@app.route('/parser', methods = ['POST'])
def parse():
    data = request.json
    print(data['url'])
    r = requests.get(data['url'])
    res = r.text
    ans = news(res)
    ans['url'] = data['url']
    r1 = requests.post('http://167.71.205.25:1092/api/save', json=ans)
    print(r1.json)
    return ans

def news(response):
    news = {

    }
    news['author'] = author(response)
    news['title'] = title(response)
    news['content'] = content(response)
    return news

def title(response):
    html = response
    pq = PyQuery(html)
    title = pq('h1.title-detail')
    return title.text()

def content(response):
    html = response
    pq = PyQuery(html)
    content = pq('p.Normal')
    return content.text()

def author(response):
    pq = PyQuery(response)
    author = pq('article > .Normal > strong')
    return author.text()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)