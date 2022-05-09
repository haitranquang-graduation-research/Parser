from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery
from specific.vnexpress import news as vnexpress_news
from specific.dantri import news as dantri_news
from specific.baomoi import news as baomoi_news
def news(response, url):
    if "vnexpress" in url:
        print('vnexpress')
        return vnexpress_news(response)
    if "dantri" in url:
        return dantri_news(response)
    if "baomoi" in url:
        return baomoi_news(response)
print(0)