from utils.addon import Addon
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen 

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

for addon in addonList:
    addon.download()
