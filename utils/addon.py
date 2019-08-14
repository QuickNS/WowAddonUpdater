class Addon:

    def __fixUrl(self, url):
        result = url.strip()
        if result[-1] == '/':
            return result[:-1]
        return result

    def __init__(self, url):
        self.url = self.__fixUrl(url).strip()
        self.targetWowVersion = "1.13.2"
        
    def download(self):
        raise NotImplementedError('subclasses must override download()!')


    