import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


# url = "https://www.ezinearticles.com"
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")
# articleid = soup.find(id='recent-article-container')
# articles = articleid.find_all("div", class_="article")


# links = [article.find("h3").find("a")['href'] for article in articles]


# full_urls = [url + link for link in links]


# url = "https://www.selfgrowth.com/articles"
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")
# articleid = soup.find(id='articles-list')
# unorderedlist = articleid.find("ul")
# articles = unorderedlist.find_all("li")


# links = [article.find("a")["href"] for article in articles]


# url = url.replace("/articles", "")


# full_urls = [url+link for link in links]


# response = requests.get(full_urls[1])
# soup = BeautifulSoup(response.content, "html.parser")
# a = soup.find("a", class_="print")
# print_url = url + a["href"]


# url = "https://www.sourcewatch.org"
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")
# div = soup.find("div", class_="mp-2col-right")
# tables = div.find_all("table")
# links = tables[1].find_all("a")


# full_url = [url + link["href"] for link in links]


# url = "https://www.articledirectoryusa.com"
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")
# articles = soup.find(id="blockStyle319Main89")
# links = articles.find_all("a")


# full_url = [url + link["href"] for link in links]


# url = "https://www.sooperarticles.com/"
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")
# articles = soup.find("section", class_="articles-list micro-share").find_all("h2", class_="entry-title")


# links = [article.find("a")["href"] for article in articles]


#============================================================================#


# url = "https://cyberleninka.org/article/c/computer-and-information-sciences"
# response = requests.get(url)
# url = url.replace("/article/c/computer-and-information-sciences", "")


# soup = BeautifulSoup(response.content, "html.parser")
# links = soup.find("div", class_="full").find_all("a")
# print_urls = [url + link["href"] + ".pdf" for link in links]


# url = "https://hanushek.stanford.edu/publications/academic"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# links = soup.find_all("div", class_="views-field views-field-field-publications-download")
# print_urls = []


# for link in links:
#     a = link.find("a")
#     try:
#         print_urls.append(a["href"])
#     except:
#         pass


# url = "https://www.journals.uchicago.edu/social-justice"
# response = requests.get(url)
# url = url.replace("/social-justice", "")

# soup = BeautifulSoup(response.content, "html.parser")
# articles = soup.find(id = "rich-text-cbe11fbf-e0e0-4920-86bc-0a5134fc275e")
# links = articles.find_all("a")
# print_urls = []


# for link in links:
#     if "/doi" in link["href"]:
#         print_url = url + link["href"]
#         print_url = print_url.replace("full", "pdf")
#         print_urls.append(print_url)


# url = "https://eric.ed.gov/?q=source%3A%22Academic+Leadership+Journal+in+Student+Research%22"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# links = soup.find_all("div", class_="r_i")


# print_urls = [link.find("div", class_="r_f").find("a")["href"] for link in links]


# url = "https://ecommons.aku.edu/pjns/"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# links = soup.find_all("p", class_="pdf")


# print_urls = [link.find("a")["href"] for link in links]


# url = "https://cyberleninka.org/article/n/68.pdf"
# response = urlopen(url)
# file = open("aloo" + ".pdf", "wb")
# file.write(response.read())
# file.close()