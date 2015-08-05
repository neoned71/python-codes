import urllib
connection=urllib.urlopen('https://google.com')
headers=connection.headers



#to look what functions are available in headers
dir(headers)


#to have all the information on headers
#these are the available fields for headers
#['__contains__', '__delitem__', '__doc__', '__getitem__', '__init__', '__iter__', '__len__', '__module__', '__setitem__', '__str__', 'addcontinue', 'addheader', 'dict', 'encodingheader', 'fp', 'get', 'getaddr', 'getaddrlist', 'getallmatchingheaders', 'getdate', 'getdate_tz', 'getencoding', 'getfirstmatchingheader', 'getheader', 'getheaders', 'getmaintype', 'getparam', 'getparamnames', 'getplist', 'getrawheader', 'getsubtype', 'gettype', 'has_key', 'headers', 'iscomment', 'isheader', 'islast', 'items', 'keys', 'maintype', 'parseplist', 'parsetype', 'plist', 'plisttext', 'readheaders', 'rewindbody', 'seekable', 'setdefault', 'startofbody', 'startofheaders', 'status', 'subtype', 'type', 'typeheader', 'unixfrom', 'values']
headers.gettype()
headers.getheader('content-type')

#to read the data one per line
line=connection.readline()
print line

#read all the data in the page
connection.read()


#there is a better library for this 'requests' so,
import requests as req
s=req.get('http://google.com')
#optionally 'auth=(username,password)' can also be provided for login into the pages


#to view the source
if s.status_code == 200:
  print s.text
