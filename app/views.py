import unittest 
from models import source

Source = source.Source
class SourceTest(unittest.TestCase):
    '''
    Test behaviour of the source class
    '''
    def setUp(self):
        '''
        Run before every Test
        '''
        self.new_source = Source("up-news","News Catch","Trusted source for analysis, breaking news, headlines, videos","https://upnews.com","general")

    def test_instance(self):
        self.assertTrue(isinstance(self.news_review,news))

if __name__ == '__main__':
    unittest.main()
