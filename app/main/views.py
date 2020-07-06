from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_source,news_source,get_category,get_headlines

@main.route('/')
def index():
    '''
    Route function returning indexpage with data
    '''
    soure= get_source()
    headlines = get_headlines()
    return render_template('index.html',sources=source, headlines = headlines)

@main.route('/news/<id>')
def news(id):

    '''
    View news pages function returning various article details page
    '''

    news= article_source(id)
    return render_template('news.html',articles= articles,id=id )

@main.route('/news_review/<review_name>')
def news_review(review_name):
    '''
    Return the news_review.html page and the content
    '''
    news_review = get_category(review_name)
    title = f'{review_name}'
    review = review_name

    return render_template('news_review.html',title = title,news_review = news_review, review = review_name)