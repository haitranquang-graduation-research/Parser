from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests
from pyquery import PyQuery
from correct_string import correct_string
import url_config
import element_path_resolver
def news(response, url):
    news = {

    }
    url_dto = {}
    url_dto['url'] = url
    site_detail = requests.post(url=url_config.get_news_specs_url() + 'api/site/view/by-url', json=url_dto)
    site_detail = site_detail.json()
    # print(site_detail)
    elements = element_path_resolver.parse_site(site_detail)
    news['source'] = site_detail['name']
    news['author'] = author(response, elements)
    news['title'] = title(response, elements)
    news['content'] = content(response, elements)
    news['topic'] = str(topic(response, elements))
    news['pictureCount'] = picture_count(response, elements)
    return news

def title(response, elements):
    pq = PyQuery(response)
    for element in elements['title']:
        title = pq(element)
        # print(title)
        # print(element)
        if (title.text() != None) and (len(title.text()) > 0):
            return correct_string(title.text())
    return correct_string(title.text())

def content(response, elements):
    pq = PyQuery(response)
    for element in elements['content']:
        content = pq(element)
        if (content.text() != None) and (len(content.text()) > 0):
            return correct_string(content.text())
    return correct_string(content.text())

def author(response, elements):
    pq = PyQuery(response)
    for element in elements['author']:
        author = [auth.text() for auth in pq(element).items()]
        if (len(author) > 0):
            author = author[len(author) - 1]
            return correct_string(author)
    return ''

def topic(response, elements):
    pq = PyQuery(response)
    for element in elements['topic']:
        topic = [top.text() for top in pq(element).items()]
        if (len(topic) > 0):
            topic = topic[0]
            return correct_string(topic)
        else:
            return ''

def picture_count(response, elements):
    pq = PyQuery(response)
    for element in elements['picture_count']:
        pictures = [picture for picture in pq(element).items()]
        if (len(pictures) > 0):
            return len(pictures)
    return len(pictures)