from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery
from specific.vnexpress import news as vnexpress_news
from specific.dantri import news as dantri_news
from specific.baomoi import news as baomoi_news
from specific.vov import news as vov_news
from specific.tuoitre import news as tuoitre_news
from specific.zingnews import news as zing_news
from specific.vietnamnet import news as vietnamnet_news
def news(response, url):
    if "vietnamnet" in url:
        return vietnamnet_news(response)
    if "tuoitre" in url:
        return tuoitre_news(response)
    if "vnexpress" in url:
        return vnexpress_news(response)
    if "dantri" in url:
        return dantri_news(response)
    if "baomoi" in url:
        return baomoi_news(response)
    if "vov" in url:
        return vov_news(response)
    if "zing" in url:
        return zing_news(response)
print(0)