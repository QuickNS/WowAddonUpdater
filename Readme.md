# WoW Addon Updater

## How to use it?

Clone this repository or download zip and extract files.

Need to have Python installed.

This installs all required packages
```
pip install -r requirements.txt
```

Update list.txt file with the information page of each Addon:

```
https://legacy-wow.com/classic-addons/questlogex/
https://www.curseforge.com/wow/addons/atlaslootclassic
https://www.wowinterface.com/downloads/info25078-BetterVendorPrice.html
```



The script currently supports Curse Forge, WowInterface and Legacy-Wow.

Simply add new addons (one per line) and then run the script as follows:

```
python updatemods.py
```

This will download all zip files to the **Packages** directory and then extract them to the **Addons** folder.

Just copy the contents of the **Addons** folder to your WoW installation

Enjoy!