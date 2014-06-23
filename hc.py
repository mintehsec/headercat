import urllib2; 
import re
url = raw_input("Enter URL: ")
 
print """
  _    _                _              _____      _   
 | |  | |              | |            / ____|    | |  
 | |__| | ___  __ _  __| | ___ _ __  | |     __ _| |_ 
 |  __  |/ _ \/ _` |/ _` |/ _ \ '__| | |    / _` | __|
 | |  | |  __/ (_| | (_| |  __/ |    | |___| (_| | |_ 
 |_|  |_|\___|\__,_|\__,_|\___|_|     \_____\__,_|\__|
------------------------------------------------------                                                     
                                                      
 
"""
 
response = urllib2.build_opener(urllib2.HTTPSHandler).open(urllib2.Request(url))
headers = str(response.info())
print url
 
find = re.search("(Powered.*)", headers)
if find:
    print"Found: ", find.group(1)
 
find = re.search("(Asp.*)", headers)
if find:
    print"Found: ", find.group(1)
                
find = re.search("(IIS.*)", headers)
if find:
    print"Found: ", find.group(1)
