import urllib.request, urllib.parse, urllib.error
import http.cookiejar

##import urllib
import cookiejar

LOGIN_URL = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
get_url = 'http://www.jobbole.com/'  # 利用cookie请求访问另一个网址

values = {'action': 'user_login', 'user_login': 'whiteapple', 'user_pass': 'jaychou1324'}
postdata = urllib.parse.urlencode(values).encode()
print(postdata)
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
headers = {'User-Agent': user_agent}

cookie_filename = 'cookie_jar.txt'
cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
response=opener.open(request)
##try:
##    response = opener.open(request)
##    # print(response.read().decode())
##except urllib.error.URLError as e:
##    print(e.code, ':', e.reason)

cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
for item in cookie_jar:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

get_request = urllib.request.Request(get_url, headers=headers)
get_response = opener.open(get_request)
print('个人主页' in get_response.read().decode())
