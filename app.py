from autoscraper import AutoScraper
from flask import Flask, request,render_template
import json


amazon_scraper = AutoScraper()
amazon_scraper.load('amazon-search5.json')
app = Flask(__name__)

def get_amazon_result(search_query):
    url = 'https://www.amazon.in/s?k=%s' % search_query
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

def _aggregate_result(result):
    final_result = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:
            
            final_result.append({alias: result[alias][i] for alias in result})
        except:
            pass
    
    return final_result
    


@app.route('/')
def predict():
    return render_template("index.html")

@app.route('/search_api', methods=['POST'])
def search_api():
    k=request.form['key']
    #query = request.args.get('k')
    print(k)
    return dict(result=get_amazon_result(k))

if __name__ == '__main__':
    app.run(debug=True)
    



