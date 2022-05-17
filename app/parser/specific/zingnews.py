from flask import jsonify, request, Flask
from flask_restful import Resource, Api
from numpy import size
import requests
from pyquery import PyQuery

def news(response):
    news = {

    }
    news['author'] = author(response)
    news['title'] = title(response)
    news['content'] = content(response)
    news['topic'] = str(topic(response))
    news['pictureCount'] = picture_count(response)
    return news

def title(response):
    html = response
    pq = PyQuery(html)
    title = pq('.the-article-title')
    return title.text()

def content(response):
    html = response
    pq = PyQuery(html)
    content = pq('.the-article-body > p')
    return content.text()

def author(response):
    pq = PyQuery(response)
    author = [auth.text() for auth in pq('.author').items()]
    if (len(author) > 0):
        author = author[len(author) - 1]
    return author

def topic(response):
    pq = PyQuery(response)
    topic = [top.text() for top in pq('.the-article-category > a').items()]
    
    return topic

def picture_count(response):
    pq = PyQuery(response)
    pictures = [picture for picture in pq('.pCaption').items()]

    return len(pictures)