from utils.addon import Addon
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen 

__VERSION__ = "1.13.2"

# open file and read addons
with open("list.txt", "r") as fp:
    addons = fp.readlines()

print()
print("### LISTING ADDONS ###")
print()

addonList = [Addon(a) for a in addons]

for a in addonList:
    print(a.url, a.type)

print()
print(f"### TOTAL ADDONS: {len(addonList)} ###")
print()

# prepare output dir
if not os.path.exists('AddOns'):
    os.mkdir('Addons')

current = addonList[0]

# curse handling
print("Downloading:", current.name.strip())

url = current.url + "/files"
# get files page
soup = BeautifulSoup(requests.get(url).text, features="lxml")
# get files table in page
results = soup.find_all("table", {"class": "listing-project-file"})
# find all files
files = results[0].find_all("tr")
# search for correct version
for f in files[1:]:
    download_link = f.find("a", {"data-action": "file-link"})["href"]
    version = f.find("div", {"class": "mr-2"}).text.strip()
    if version == __VERSION__:
        # found it
        url = "https://www.curseforge.com" + download_link + "/file"
        url = url.replace("/files", "/download")
        print("Getting URL: ", url)
        r = requests.get(url, allow_redirects=True)
        with open(os.path.join("Addons", current.name + ".zip"), 'wb') as fp:
            fp.write(r.content)
        break
