import requests
from bs4 import BeautifulSoup

def crawl(start_url, server):
    visited = set()
    index = {}

    def process_page(url, content):
        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Extract the text content from the page
        text = soup.get_text()

        # Build the index
        words = text.split()
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(url)

        # Find all the links on the page
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and href.startswith(server) and href not in visited:
                visited.add(href)
                response = requests.get(href)
                if response.status_code == 200 and response.headers['Content-Type'].startswith('text/html'):
                    process_page(href, response.content)

    # Start crawling from the start URL
    response = requests.get(start_url)
    if response.status_code == 200 and response.headers['Content-Type'].startswith('text/html'):
        process_page(start_url, response.content)

    return index

def search(index, words):
    result = []
    for word in words:
        if word in index:
            result.extend(index[word])
    return result

# Test the crawler
start_url = 'https://www.uni-osnabrueck.de/universitaet/personensuche/'
server = 'https://www.uni-osnabrueck.de'
index = crawl(start_url, server)

# Test the search functionality
search_words = ['malte.benjamins@uos.de', 'hori']
search_results = search(index, search_words)
print(f"Search results for words '{', '.join(search_words)}':")
for result in search_results:
    print(result)
