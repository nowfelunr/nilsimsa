from bs4 import BeautifulSoup
import requests
import csv
 
with open('source.txt', 'r') as f:
    data = f.read()

header = ["Hash Name", "Digest"]
csv_file = open('hashes.xls', 'w')
writer = csv.writer(csv_file)
writer.writerow(header)
soup = BeautifulSoup(data,features="html.parser")

table = soup.find('table', {'class':'table table-bordered'})
trs = table.find_all('tr')
for tr in trs:
    td = tr.find_all('td')
    th = tr.find('th')
    digest = td[1].text
    hash_name = th.text

    
    writer.writerow([hash_name, digest])

