import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from .addon import Addon

class WowInterfaceAddon(Addon):

    def __init__(self, url):
        super().__init__(url)
        self.type = "WowInterface"
        self.name = self.url.split("/")[-1].strip().split('-')[1].split('.')[0]
        print("Name", self.name)

    def _download_file(self, url):
        print("Getting URL: ", url)
        r = requests.get(url, allow_redirects=True)
        with open(os.path.join("Packages", self.name + ".zip"), 'wb') as fp:
            fp.write(r.content)


    def download(self):
        print("\n[WOWINTERFACE] Downloading:", self.name.strip())
        url = self.url.replace("info","download").replace(".html","")
        # get page
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        # get download link
        actionLink = soup.find("div", {"class": "manuallink"})
        # get file location
        file_link = actionLink.find("a")['href']
        # download
        self._download_file(file_link)