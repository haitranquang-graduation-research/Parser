from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery
from general_parser import news

app = Flask(__name__)
api = Api(app)
print('Hello')

@app.route('/parser', methods = ['POST'])
def parse():
    data = request.json
    # print(data['url'])
    r = requests.get(data['url'])
    res = r.text
    ans = news(res, data['url'])
    ans['url'] = data['url']
    # print(ans['url'])
    # r1 = requests.post('http://172.21.0.5:1092/api/save', json=ans)
    # print(r1.json)
    return ans


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5090)