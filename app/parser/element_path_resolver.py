from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery

app = Flask(__name__)
api = Api(app)
print('Hello')


def parse_path(elements):
    detail = {
        "title":[],
        "author":[],
        "picture_count":[],
        "content":[],
        "href":[],
        "topic":[]
    }
    for element in elements:
        detail[element['type'].lower()].append(element['path'])
    # print(detail)
    return detail


def parse_site(siteDetail):
    return parse_path(siteDetail['elements'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5054)
