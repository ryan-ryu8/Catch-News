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
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,descrption,url)
            source_results.append(source_object)
    return source_results

def news_source(id):
    news_source_url = 'https://newsapi/headlines?sources={}&apiKey={}'.format(id,api_key)
    print(news_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        news_source_data = url.read()
        news_source_response = json.loads(news_source_data)

        news_source_results = None

        if news_source_response['news']:
            news_source_list = news_source_response['news']
            news_source_results = process_news_results(news_source_list)

    return news_source_results

def get_category(review_name):
    '''
    Gets response to review json
    '''
    get_category_url = review_url.format(review_name,apikey)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)
        get_category_results = None

        if get_category_response['news']:
            get_category_list = get_category_response['news']
            get_category_results = process_news_results(get_category_list)

    return get_category_results

def get_headlines():
    '''
    Gets response to category json
    '''
    get_headlines_url = 'https://newsapi/headlines?country=ke&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        get_headlines_results = None

        if get_headlines_response['news']:
            get_headlines_list = get_headlines_response['news']
            get_headlines_results = process_news_results(get_headlines_list)

    return get_headlines_results

