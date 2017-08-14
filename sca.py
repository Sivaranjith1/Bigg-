from scraper import Client
import bs4 as bs

url = "www.tubetamil.com/tamil-tv-show/bigg-boss/bigg-boss-14-08-2017-kamal-hassan.html"
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
print(source)
