import json
from bs4 import BeautifulSoup
import requests
import re
resp = requests.get('https://www.tripadvisor.in/Hotel_Review-g304554-d2048980-Reviews-Sofitel_Mumbai_BKC-Mumbai_Maharashtra.html') 
data = BeautifulSoup(resp.content).find('script', text = re.compile('window.__WEB_CONTEXT__')).text
pageManifest = json.loads(data.replace('window.__WEB_CONTEXT__=','').replace('{pageManifest:', '{"pageManifest":')[:-1])

x=pageManifest['pageManifest']['redux']['api']['responses']
list_x = list(x)
str_x = str(x)
list_of_dataAttrs = []
#keep executing this loop until dataAttrs exists in my dict_string, quit loop if you can't find dataAttrs
while(not str_x.find('\'data-vendorName\':') == -1):
	#extract required string, store it in my list of dataAttrs...finally replace dataAttrs with garbage value so that it doesn't get found again
	start_idx = str_x.find('\'data-vendorName\':') 
	cur_idx = start_idx
	result_str = ''
	#until i find '}', keep adding characters to my resultant string
	while(not str_x[cur_idx]==','):
		result_str+=str_x[cur_idx]
		cur_idx+=1
	
	list_of_dataAttrs.append(result_str)
	str_x = str_x[:start_idx] + 'someYungHo#@#$@@%^@#%' + str_x[cur_idx:]#replacing with garbage


print(list_of_dataAttrs)

# print('----------Printing all dataAttrs found----------')

# i=1
# for ele in list_of_dataAttrs:
# 	print(''.join(str(ele)))
# 	i+=1

