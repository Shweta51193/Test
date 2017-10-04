from bs4 import BeautifulSoup
import requests
import re

url = "https://www.flipkart.com/search?as=on&as-pos=1_1_ic_watches+boys&as-show=on&otracker=start&page=4&q=watches+boys&sid=r18%2Ff13&viewType=grid"
data = requests.get(url)
soup = BeautifulSoup(data.text)
# print(soup)
start_tag=soup.find("div",{"class":"GQtpzo"})
cout_tag = start_tag.find("div", {"class": "KG9X1F"})
# print(cout_tag.text)
# for i in cout_tag:
#     print(i)
count_text = cout_tag.text
print(count_text)
d = re.match('^Showing.*?of\s*(\d+,\d+).*?$', count_text)
comma_count=d.group(1)
p_count=int(comma_count.replace(',',''))
no_of_pages=int(p_count/40)+1
print(no_of_pages)

next_tag=start_tag.find("div",{"class":"_2kUstJ"})
next_a=next_tag.find("a")
b = url.split('/')
next_url=b[2]+next_a['href']
print(next_url)
a=next_url.split('page')

e=a[0]+"page"
print(a)
# second_url=next_url.replace(old, new, count)

	