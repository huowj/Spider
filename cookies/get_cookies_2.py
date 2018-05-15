import urllib.request, urllib.parse, urllib.error
import http.cookiejar

##import urllib
import cookiejar

LOGIN_URL = 'http://www.jobbole.com/login/?redirect=http%3A%2F%2Fwww.jobbole.com%2F'
##get_url = 'http://www.jobbole.com/'  # 利用cookie请求访问另一个网址

values = {'action': 'user_login', 'jb_user_login': 'whiteapple', 'jb_user_pass': 'jaychou1324'}
postdata = urllib.parse.urlencode(values).encode()
print(postdata)
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent}

cookie_filename = 'cookie_jar.txt'
cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
print(request)
try:
    response = opener.open(request)
    # print(response.read().decode())
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
