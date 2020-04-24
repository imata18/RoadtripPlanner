# Reference This code is from yelp api website
from __future__ import print_function
from urllib.parse import quote
import requests

API_KEY= "BwMypdqwoIEj990faouAsALG8cdugo5GMigEs4qE-SYVMgObVA3Ur2bPsD61_ymZIHD8U9k0BjCl1miUHTqrcsWtDwoX6rPP89y4MB8cprEghdsq-bQzc00yQEF2XnYx"

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
SEARCH_LIMIT = 1


def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()


def search(term, location, api_key=API_KEY):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_hotel_name(location):
    hotel = search("hotel", location)
    return hotel["businesses"][0]["name"]
