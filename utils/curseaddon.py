import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen 
from .addon import Addon

class CurseAddon(Addon):

    def __init__(self, url):
        super().__init__(url)
        self.type = "Curse"
        self.name = self.url.split("/")[-1].strip()

    def _download_file(self, download_link):
            url = "https://www.curseforge.com" + download_link + "/file"
            url = url.replace("/files", "/download")
            print("Getting URL: ", url)
            r = requests.get(url, allow_redirects=True)
            with open(os.path.join("Packages", self.name + ".zip"), 'wb') as fp:
                fp.write(r.content)

    def download(self):
        print("\n[CURSE] Downloading:", self.name.strip())

        url = self.url + "/files"
        # get files page
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")
        # get files table in page
        results = soup.find_all("table", {"class": "listing-project-file"})
        # find all files
        files = results[0].find_all("tr")
        # search for correct version
        foundIt = False
        for f in files[1:]:
            download_link = f.find("a", {"data-action": "file-link"})["href"]
            version = f.find("div", {"class": "mr-2"}).text.strip()
            if version == self.targetWowVersion:
                # found it
                foundIt= True
                self._download_file(download_link)
                break

        if not foundIt:
            # didn't find correct version so just download latest
            f = files[1]
            download_link = f.find("a", {"data-action": "file-link"})["href"]
            print(f"Couldn't find match for version {self.targetWowVersion}. Downloading latest instead.")
            self._download_file(download_link)

