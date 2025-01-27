from flask import render_template,request,redirect
from . import main
from ..request import get_sources,get_news,search_sources
from ..models import News, Articals

# Views
@main.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    #getting sources
    sources = get_sources()
    print(sources)

    title = 'BestNews'
    return render_template('index.html', title = title ,sources = sources )

@main.route('/news/<id>')
def news(id):
    news = get_news(id)
    print(news)

    title= 'Articales'
    return render_template('news.html',title = title, news=news)

@main.route('/search/<artical_name>')
def search(artical_name):
    artical_name_list = artical_name.split(" ")
    artical_name_format = "+".join(artical_name_list)
    searched_articals = searches_artical(artical_name_format)
    title = f'search results for {searches_artical} '
    return render_template('search.html',search = searched_articals)
    





