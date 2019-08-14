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
            
        

    