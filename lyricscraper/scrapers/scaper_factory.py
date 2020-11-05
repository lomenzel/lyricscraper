# Import all the scrapers here to ensure globals() has the key in it for dynamic instantiation
from .azlyrics_scraper import AZLyricsScraper
from .musixmatch_scraper import MusixMatchScraper
from .genius_scraper import GeniusScraper
from .songlyrics_scraper import SongLyricsScraper

class ScraperFactory:
    """ Singleton Factory of metadata providers. Pass in the name defined in the provider .name() and an instance will be returned. """
    __instance = None
    providers = {}

    def __new__(cls):
        if ScraperFactory.__instance is None:
            ScraperFactory.__instance = object.__new__(cls)
        
        return ScraperFactory.__instance

    def __init__(self):
        pass
    
    def get_scraper(self, setting_name):
        if not setting_name in self.providers:
            cls = globals()[setting_name + 'Scraper']
            self.providers[setting_name] = cls()
        return self.providers[setting_name]
