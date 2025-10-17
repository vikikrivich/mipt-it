import requests
import bottle

cache = {}

@bottle.route('/')
def index():
    return bottle.template('index.html', search_term='', pages=[])

@bottle.post('/search')
def search():
    search_term = bottle.request.forms.get('search')
    if search_term in cache:
        pages = cache[search_term]
    else:
        params = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srsearch': search_term
        }
        url = "https://en.wikipedia.org/w/api.php"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        pages = []
        for page in data['query']['search']:
            pages.append({'title': page['title'], 'pageid': page['pageid']})
        cache[search_term] = pages
    return bottle.template('index.html', pages=pages, search_term=search_term)

@bottle.route('/page/<pageid>')
def page(pageid):
    if pageid in cache:
        title, text = cache[pageid]
    else:
        params = {
            'action': 'parse',
            'prop': 'text',
            'pageid': pageid,
            'format': 'json'
        }
        url = "https://en.wikipedia.org/w/api.php"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        title = data['parse']['title']
        text = data['parse']['text']['*']
        cache[pageid] = (title, text)
    return bottle.template('page.html', title=title, text=text)

bottle.run(host='0.0.0.0', port=8080)