
from autoscraper import AutoScraper
search = "iphone+11+silver"
amazon_url="https://www.amazon.in/s?k={}&s=price-desc-rank".format(search)

wanted_list=["₹1,25,900","New Apple iPhone 12 Pro Max (128GB) - Silver"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))
scraper.set_rule_aliases({'rule_mnqw':'price','rule_2arc':'title'})
scraper.keep_rules(['rule_mnqw','rule_2arc'])
scraper.save('amazon-search5.json')


