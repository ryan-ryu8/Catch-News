import urllib.request,json
from .models import News, News_review, Source, Headlines

api_key = None
source_url = None
review_url = None

def configure_request(app):
    global api_key, source_url, review_url
    api_key = app.config['News_Api_Key']
    source_url = app.config['News_Api_Source_url']
    review_url = app.config['Review_Api_url']

def get_source():
    '''
    Gets json response to url request
    '''
    get_source_url = source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_source_response = json.loads(get_sources_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results 

def process_results(source_list):
    '''
    Process results to list of objects transformation
    Args:
    source_list:source details
    Returns:
    source_results:source objects
    '''