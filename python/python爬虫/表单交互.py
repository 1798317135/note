import requests
url = "https://www.douban.com/accounts/login"
params = {
    'source':'index_nav',
    'form_email':'760008395@qq.com',
    'form_password':'b123456789',
    'captcha-solution':'system',
    'captcha-id': 'ERWZkv68ofuZ9e96wbC9V2SH:en',
}
r = requests.post(url,params)
print(r.text)