import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from .addon import Addon

class LegacyWowAddon(Addon):

    def __init__(self, url):
        super().__init__(url)
        self.type = "LegacyWoW"
        self.name = self.url.split("/")[-1].strip()

    def _download_file(self, url):
        print("Getting URL: ", url)
        r = requests.get(url, allow_redirects=True)
        with open(os.path.join("Packages", self.name + ".zip"), 'wb') as fp:
            fp.write(r.content)


    def download(self):
        print("\n[LEGACY-WOW] Downloading:", self.name.strip())

        # get page
        soup = BeautifulSoup(requests.get(self.url).text, features="html.parser")
        # get download link
        actionLink = soup.find("a", {"href": "Download"})['onclick']
        # get file location
        file_link = actionLink.replace("updateC('","").split(',')[0][:-1]
        # download
        self._download_file(file_link)