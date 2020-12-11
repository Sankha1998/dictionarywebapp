from flask import Flask
from flask import render_template,request
import requests
from bs4 import BeautifulSoup as bs


app= Flask(__name__)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def meaning(url):
    response = requests.get(url, headers=headers).text
    soup = bs(response, 'lxml')
    data = soup.find_all('div', class_='definition flex-align-self-center')
    meaning = []
    try:
        c = 0
        for i in data:
            if (c < 10):
                meaning.append(i.text.strip())
                c += 1
            else:
                pass
    except:
        meaning.append('No Items Found')
    if len(meaning)==0:
        meaning.append('No Items Found')
    return meaning

def synonym(url1):
    response1 = requests.get(url1, headers=headers).text
    soup1 = bs(response1, 'lxml')
    synonyms = []

    try:
        c=0
        for i in soup1.find_all('div', class_='synonym-link-wrapper'):

            if (c < 10):
                synonyms.append(i.text.strip())
                c += 1
            else:
                pass
    except:
        synonyms.append('No Items Found')
    if len(synonyms)==0:
        synonyms.append('No Items Found')
    return synonyms




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dictionary', methods=['POST'])
def word():
    inp_word = request.form.get('word')
    url = 'https://www.yourdictionary.com/{}'.format(inp_word)
    url1 = 'https://thesaurus.yourdictionary.com/{}'.format(inp_word)
    meanings_list = meaning(url)
    synonyms_list = synonym(url1)
    return render_template('wordresult.html',meanings_list=meanings_list,synonyms_list=synonyms_list)


if __name__=="__main__":
    app.run(debug=True)