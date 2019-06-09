import requests,base64

def verfiy(img_path):
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    access_token = "24.8c9d19026505908d8705c746ced9a540.2592000.1557164899.282335-15948645"
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
    with open(img_path,"rb") as f:
        img = base64.b64encode(f.read())

    data =  {
        "image":img
    }
    response = requests.post(url, headers=headers, data=data)
    content = response.text
    return content

if __name__ == '__main__':
    code = verfiy("./heh.jpg")
    print(code)






