#https://pypi.org/project/requests/
#https://requests.readthedocs.io/en/latest/

import requests

# x = requests.get('http://httpbin.org/get')

# print(x.headers)
# print(x.headers['Server'])
# print(x.status_code)

# if x.status_code == 200:
#     print("Success!")
# elif x.status_code == 404:
#     print("Not found!")

# print(x.elapsed)
# print(x.cookies)
# print(x.content)
# print(x.text)

# x = requests.get("http://httpbin.org/get", params={'id':'1'})
# print(x.url)

# x = requests.get("http://httpbin.org/get?id=2")
# print(x.url)

# x = requests.get("http://httpbin.org/get", params={'id':'3'}, headers={'accept':'application/json', 'test':'test_header',"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"})
# print(x.headers)
# print(x.text)

# x = requests.delete('http://httpbin.org/delete')
# print(x.text)

# x = requests.post('http://httpbin.org/post', data={'a':'b'})
# print(x.text)

# files = {'file': open('google.png', 'rb')}
# x = requests.post('http://httpbin.org/post', files=files)
# print(x.text)

# x = requests.get("http://httpbin.org/get", auth=('username', 'password'))
# print(x.text)

# x = requests.get("https://bohansec.com")
# print(x.text)

# x = requests.get("https://expired.badssl.com",verify=False)
# print(x.text)

# x = requests.get("http://github.com", allow_redirects=False)
# print(x.headers)

# x = requests.get("http://httpbin.org/get", timeout=0.01)
# print(x.content)

# x = requests.get("http://httpbin.org/cookies", cookies={'a':'b'})
# print(x.text)

# x = requests.Session()
# x.cookies.update({'a':'b'})

# print(x.get("http://httpbin.org/cookies").text)

# x = requests.get('https://api.github.com/events')
# print(x.json())

x = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png')
with open('google2.png', 'wb') as f:
    f.write(x.content)