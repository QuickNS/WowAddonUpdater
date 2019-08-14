from utils import Addon, CurseAddon, LegacyWowAddon, WowInterfaceAddon
import os
import zipfile

# open file and read addons
with open("list.txt", "r") as fp:
    addons = fp.readlines()

print()
print("### LISTING ADDONS ###")
print()

addonList = list()
for a in addons:
    if a.startswith("https://www.curseforge.com"):
        addonList.append(CurseAddon(a))
    elif a.startswith("https://legacy-wow.com/"):
        addonList.append(LegacyWowAddon(a))
    elif a.startswith("https://www.wowinterface.com"):
        addonList.append(WowInterfaceAddon(a))

for a in addonList:
    print(f"{a.name} - {a.type}")

print()
print(f"### TOTAL ADDONS: {len(addonList)} ###")

# prepare output dir
if not os.path.exists('Packages'):
    os.mkdir('Packages')

# download all addons
for addon in addonList:
    addon.download()

# prepare Addons dir
if not os.path.exists('Addons'):
    os.mkdir('Addons')

print(f"\n### DOWNLOADS COMPLETE ###\n")

# unzip all addons
for addon in addonList:
    filename = os.path.join("Packages",addon.name + ".zip")
    print("Extracting", filename)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall("Addons")