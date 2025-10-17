import requests

# 1
params = {
    'action': 'query',
    'format': 'json',
    'list': 'search',
    'srsearch': 'apple'
}

url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=apple"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
response = requests.get(url, params=params, headers=headers)

data = response.json()
titles = []
for page in data['query']['search']:
    titles.append(page['title'])
print(titles)