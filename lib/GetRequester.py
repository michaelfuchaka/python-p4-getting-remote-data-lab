import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
         """
        Sends a GET request to the URL passed in on initialization.
        Returns the raw response body (string).
        """
         response = requests.get(self.url)
         return response.content


    def load_json(self):
           """
        Uses get_response_body to send a request,
        then converts the response to Python data (list or dict).
        """
           response_body = self.get_response_body()
           return json.loads(response_body)