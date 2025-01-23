import requests
from bs4 import BeautifulSoup



def write_to_text():
	page = requests.get("http://www.stat.berkeley.edu/~binyu/Site/Publications.html")

	soup = BeautifulSoup(page.text)

	l = soup.find_all('li')

	f = open("parseddata.txt", "wb")
	# to modify href "../" to correct link
	for element in l:
		if element and element.find('a') and element.find('a')['href'][:2]=='..':
			element.find('a')['href'] = 'http://www.stat.berkeley.edu/~binyu'+element.find('a')['href'][3:]
		f.write(element.prettify().encode('utf-8')+"\n")

	f.flush()
	f.close()



def write_to_html():
	pub = open("template.html", 'rb')
	soup_pub = BeautifulSoup(pub.read())
	main = soup_pub.find(id="main")
	new_tag = soup_pub.new_tag("ul")
	main.append(new_tag)

	#page = requests.get("http://www.stat.berkeley.edu/~binyu/Site/Publications.html")
	page = requests.get("https://binyu.stat.berkeley.edu/papers")
	soup = BeautifulSoup(page.text)

	l = soup.find_all('li')

	for element in l:
		if element and element.find('a') and element.find('a').find('href') and element.find('a')['href'][:2]=='..':
			element.find('a')['href'] = 'http://www.stat.berkeley.edu/~binyu/'+element.find('a')['href'][3:]
		main.ul.append(element)
	
	f = open('publications.html', 'wb')
	f.write(soup_pub.prettify().encode('utf-8'))
	f.flush()
	f.close()

write_to_html()



