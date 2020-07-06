import is 

class Config:
    '''
    Parent class configuration
    '''
    News_Api_Source_url = 'https://newsapi/headlines?sources={}&apiKey={}'
    Review_Api_url = 'https://newsapi/headlines?country=ke&apiKey={}'

class ProdConfig(Config):
    '''
    Child class config
    Args:
    Config: Parent config with general config settings
    '''
    pass

class DevConfig(Config):
    '''
    Child class development
    Args:
    Config:  Parent config with general config settings
    '''
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}