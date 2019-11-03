import requests
import json


class Vinmonopolet:

    def __init__(self):
        self.apikey = ''
        self.headers = {'Ocp-Apim-Subscription-Key': self.apikey}

    def search(self, search_string):
        search_string = search_string.split(" ")[0]
        url = 'https://apis.vinmonopolet.no/products/v0/details-normal' \
              '?productShortNameContains={}'.format(search_string)
        response = requests.get(url=url, headers=self.headers)
        return json.loads(response.text)
