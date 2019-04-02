#! python3
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import sys

usg_msg = """\
Usage:
python3 craigslist_scrape.py <product name string, spaces ok>\
"""

if len(sys.argv) > 1:
    # Get address from command line.
    product_name = '+'.join(sys.argv[1:])
    print(product_name)
else:
	print(usg_msg)
	exit(1)

my_url = "https://inlandempire.craigslist.org/search/sya?query=" + product_name
uClient = urlopen(my_url) 
page_html = uClient.read() # puts contents into var, raw html
uClient.close()

page_soup = soup(page_html, "html.parser") # soupify page
# html class for desired results, have to pick apart these containers
# for desired info
results = page_soup.findAll("li", {"class":"result-row"}) 

filename = "craigslist_" + product_name.replace('+','_') + ".csv"
f = open(filename, "w")

headers = "result_name, price, time_posted, link \n"


f.write(headers)

for result in results:

	price = result.a.text.strip()
	
	result_name = result.p.a.text.replace(",", "-")
	
	time_posted = result.p.time["title"]

	result_link = result.a['href']
	print("result_name", result_name)
	print("price", price)
	print("time_posted", time_posted)
	print("result_link", result_link, "\n")


	f.write(result_name +","+ price +","+ time_posted +","+ result_link + "\n")



