import mechanize
br = mechanize.Browser()

br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox')]

br.open("https://cccbdb.nist.gov/gaufiles1.asp")

# response = br.response()
# print response.geturl() # URL of the page we just opened
# print response.info()   # headers
# print response.read()   # body

# for form in br.forms():
#     print form.name
#     print form

br.select_form(name='form1') 

for control in br.form.controls:
    control.readonly = False
    # print control
    # print control.name
    # print control.type

br['formula'] = 'C6H14'
response_cbox = br.submit()
#print response_cbox.read()

br.select_form(nr=0)

br['which'] = ['2']
resp = br.submit()
#print resp.read() 

#######################################################################################

from bs4 import BeautifulSoup
#import requests 

temp = resp
soup = BeautifulSoup(temp, "html.parser")

global index ;global path_url ;
index =0 ;path_url =[] ;file_url=[];

for links in soup.find_all( "td",class_="num"):
	# print(links.find_all('a'))
	for link in links.find_all('a'):
		index = index +1
		# print(link.get('href'))
		path_url.append(link.get('href'))


base_url = "https://cccbdb.nist.gov/"
for i in xrange(0,index):
	file_url.append(base_url + path_url[i])
	#print file_url[i] 
print file_url[4] 
 
#########################################################################################

import urllib
urllib.urlretrieve(file_url[4], "testFile4.txt")