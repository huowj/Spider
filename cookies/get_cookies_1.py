import urllib.request

data = {'name' : 'www', 'password' : '123456'}
f = urllib.request.urlopen(
        url     = 'http://www.ideawu.net/',
        #data    = urllib.urlencode(data)
		)
print (f.read())
