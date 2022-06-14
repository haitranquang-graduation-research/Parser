from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery
import url_config
import element_path_resolver
def news(response, url):
    news = {

    }
    url_dto = {}
    url_dto['url'] = url
    site_detail = requests.post(url=url_config.get_news_specs_url() + 'api/site/view/by-url', json=url_dto)
    site_detail = site_detail.json()
    elements = element_path_resolver.parse_site(site_detail)
    news['author'] = author(response, elements)
    news['title'] = title(response, elements)
    news['content'] = content(response, elements)
    news['topic'] = str(topic(response, elements))
    news['pictureCount'] = picture_count(response, elements)
    return news

def title(response, elements):
    pq = PyQuery(response)
    title = pq(elements['title'])
    return title.text()

def content(response, elements):
    pq = PyQuery(response)
    content = pq(elements['content'])
    return content.text()

def author(response, elements):
    pq = PyQuery(response)
    author = [auth.text() for auth in pq(elements['author']).items()]
    if (len(author) > 0):
        author = author[len(author) - 1]
        return author
    return ''

def topic(response, elements):
    pq = PyQuery(response)
    topic = [top.text() for top in pq(elements['topic']).items()]
    if (len(topic) > 0):
        topic = topic[0]
        return topic
    else:
        topic = ''

def picture_count(response, elements):
    pq = PyQuery(response)
    pictures = [picture for picture in pq(elements['picture_count']).items()]
    return len(pictures)