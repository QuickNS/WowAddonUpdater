class Addon:



    def __fixUrl(self, url):
        result = url.strip()
        if result[-1] == '/':
            return result[:-1]
        return result

    def __init__(self, url):
        self.url = self.__fixUrl(url)
        self.name = url.split("/")[-1].strip()
        if self.url.startswith("https://www.curseforge.com"):
            self.type = "Curse"
        elif self.url.startswith("https://legacy-wow.com/"):
            self.type = "LegacyWow"

    def download(self):
        import requests
        import os
        from bs4 import BeautifulSoup
        from urllib.request import urlopen 

        __VERSION__ = "1.13.2"

        # curse handling
        if self.type == "Curse":
            print("\nDownloading:", self.name.strip())

            url = self.url + "/files"
            # get files page
            soup = BeautifulSoup(requests.get(url).text, features="lxml")
            # get files table in page
            results = soup.find_all("table", {"class": "listing-project-file"})
            # find all files
            files = results[0].find_all("tr")
            # search for correct version
            foundIt = False
            for f in files[1:]:
                download_link = f.find("a", {"data-action": "file-link"})["href"]
                version = f.find("div", {"class": "mr-2"}).text.strip()
                if version == __VERSION__:
                    # found it
                    foundIt= True
                    url = "https://www.curseforge.com" + download_link + "/file"
                    url = url.replace("/files", "/download")
                    print("Getting URL: ", url)
                    r = requests.get(url, allow_redirects=True)
                    with open(os.path.join("Addons", self.name + ".zip"), 'wb') as fp:
                        fp.write(r.content)
                    break

            if not foundIt:
                # didn't find correct version so just download latest
                f = files[1]
                download_link = f.find("a", {"data-action": "file-link"})["href"]
                print(f"Couldn't find match for version {__VERSION__}. Downloading latest instead.")
                url = "https://www.curseforge.com" + download_link + "/file"
                url = url.replace("/files", "/download")
                print("Getting URL: ", url)
                r = requests.get(url, allow_redirects=True)
                with open(os.path.join("Addons", self.name + ".zip"), 'wb') as fp:
                    fp.write(r.content)
                
        

    