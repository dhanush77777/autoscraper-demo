
from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"

wanted_list=["₹58,400","New Apple iPhone 11 (128GB) - Black"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))
scraper.set_rule_aliases({'rule_i48i':'price','rule_1nla':'title'})
scraper.keep_rules(['rule_i48i','rule_1nla'])
scraper.save('amazon-search1')

