from bs4 import BeautifulSoup

with open('teachers.xml', 'r') as f:
	file = f.read() 


soup = BeautifulSoup(file, 'xml')

names = soup.find_all('name')
for name in names:
    print(name.text)