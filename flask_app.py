import requests,flask
from flask import Flask,request

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/gen")
def generateGmail():

    cookies = {
    'version': 'eyJpdiI6InhEbk82WFdXZk1pL0xnUjdYSk5CbEE9PSIsInZhbHVlIjoiL2Z4bHU1VjlzMDZzVG43VE0xQ2d5SWhiVUpiNmhaRjFWU2twOE9vOTdmMVY2Z2xza28wZFBHT3ltSlpsK1lGYyIsIm1hYyI6IjE1N2IxM2I3Y2RjYzNkODUyMWFhMjdhODZjM2Q0MDk0MjI4YmMxNTcyMDQyMjRkNzNhYWI5YWZkMzJkMDFlNGUifQ%3D%3D',
    '__gads': 'ID=6a5ff601c9997a4d-226a488c21d50011:T=1662179359:RT=1662179359:S=ALNI_Mb-zRKzuyy8phLIGTKSQN7BjDwxLg',
    '__gpi': 'UID=00000ab01e4cad97:T=1662179359:RT=1662204821:S=ALNI_MYRXqGKobZOut5A7p2kEZs2sWeiTw',
    'XSRF-TOKEN': 'eyJpdiI6IlBnVXUySkkvSDR5bG1TbHRZbDcvMUE9PSIsInZhbHVlIjoiQ2t5aGhpTmxyeEd0SlF5QWVtQnRVZUZHdW9RRUx6SjZBd2VlcHBEQ0lDTk1SWWw0dUduVjZJNFRKeUdOV3BhYjgxbE1rR0k2WXYwTmQ3blZvL0I2amxiZXUyendtT2ZhWGVVOEowSkd3ZVZUdTRKYzBGd0JOZS9STnlWQnBZNDgiLCJtYWMiOiIxODA5ZWVlZjZmNTQ3NmIxZWNjNDNlZWZmMjFkOTMxODNiYWViZWY5ZmQ3MGEwMjcxMjE5MzExNjQ5OWRhZDk4In0%3D',
    'sonjj_session': 'eyJpdiI6IkFEQjZhUEpYTjk2ZFNiRE9maW1nYUE9PSIsInZhbHVlIjoiVUZWZFZRVmZlZjlOdjRzbHRxRmRESFJtTUtIU2lRSnd4SUZYUnpadCtaTUx4L3BWWC9SSlJvQVcrK0dsVTNzNnh5N2FVTGo3S3RJVEFVMzRhWlN4aDBNVENUU2gwVmYrck9FaUs0N0x2UVVLMWt0ck11WlRKOUw4dGNIOExhT2EiLCJtYWMiOiJjOWJiMTFlMTAyZGJhMmM1ZjAxOTM2YmFiNzNjYTE4OTIxNTJiMDJjOTY0OWEyZjQ5OTJlYTJmNDYzYTdjNzRhIn0%3D',
}

    headers = {
    'authority': 'smailpro.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'version=eyJpdiI6InhEbk82WFdXZk1pL0xnUjdYSk5CbEE9PSIsInZhbHVlIjoiL2Z4bHU1VjlzMDZzVG43VE0xQ2d5SWhiVUpiNmhaRjFWU2twOE9vOTdmMVY2Z2xza28wZFBHT3ltSlpsK1lGYyIsIm1hYyI6IjE1N2IxM2I3Y2RjYzNkODUyMWFhMjdhODZjM2Q0MDk0MjI4YmMxNTcyMDQyMjRkNzNhYWI5YWZkMzJkMDFlNGUifQ%3D%3D; __gads=ID=6a5ff601c9997a4d-226a488c21d50011:T=1662179359:RT=1662179359:S=ALNI_Mb-zRKzuyy8phLIGTKSQN7BjDwxLg; __gpi=UID=00000ab01e4cad97:T=1662179359:RT=1662204821:S=ALNI_MYRXqGKobZOut5A7p2kEZs2sWeiTw; XSRF-TOKEN=eyJpdiI6IlBnVXUySkkvSDR5bG1TbHRZbDcvMUE9PSIsInZhbHVlIjoiQ2t5aGhpTmxyeEd0SlF5QWVtQnRVZUZHdW9RRUx6SjZBd2VlcHBEQ0lDTk1SWWw0dUduVjZJNFRKeUdOV3BhYjgxbE1rR0k2WXYwTmQ3blZvL0I2amxiZXUyendtT2ZhWGVVOEowSkd3ZVZUdTRKYzBGd0JOZS9STnlWQnBZNDgiLCJtYWMiOiIxODA5ZWVlZjZmNTQ3NmIxZWNjNDNlZWZmMjFkOTMxODNiYWViZWY5ZmQ3MGEwMjcxMjE5MzExNjQ5OWRhZDk4In0%3D; sonjj_session=eyJpdiI6IkFEQjZhUEpYTjk2ZFNiRE9maW1nYUE9PSIsInZhbHVlIjoiVUZWZFZRVmZlZjlOdjRzbHRxRmRESFJtTUtIU2lRSnd4SUZYUnpadCtaTUx4L3BWWC9SSlJvQVcrK0dsVTNzNnh5N2FVTGo3S3RJVEFVMzRhWlN4aDBNVENUU2gwVmYrck9FaUs0N0x2UVVLMWt0ck11WlRKOUw4dGNIOExhT2EiLCJtYWMiOiJjOWJiMTFlMTAyZGJhMmM1ZjAxOTM2YmFiNzNjYTE4OTIxNTJiMDJjOTY0OWEyZjQ5OTJlYTJmNDYzYTdjNzRhIn0%3D',
    'origin': 'https://smailpro.com',
    'referer': 'https://smailpro.com/advanced',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    #'x-xsrf-token': 'eyJpdiI6IlBnVXUySkkvSDR5bG1TbHRZbDcvMUE9PSIsInZhbHVlIjoiQ2t5aGhpTmxyeEd0SlF5QWVtQnRVZUZHdW9RRUx6SjZBd2VlcHBEQ0lDTk1SWWw0dUduVjZJNFRKeUdOV3BhYjgxbE1rR0k2WXYwTmQ3blZvL0I2amxiZXUyendtT2ZhWGVVOEowSkd3ZVZUdTRKYzBGd0JOZS9STnlWQnBZNDgiLCJtYWMiOiIxODA5ZWVlZjZmNTQ3NmIxZWNjNDNlZWZmMjFkOTMxODNiYWViZWY5ZmQ3MGEwMjcxMjE5MzExNjQ5OWRhZDk4In0=',
}

    json_data = {
    'domain': 'gmail.com',
    'username': 'random',
    'server': 'server-1',
    'type': 'alias',
}

    response = requests.post('https://smailpro.com/app/key', headers=headers, json=json_data).json()
    key = response['items']

    headers = {
    'authority': 'public-sonjj.p.rapidapi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://smailpro.com',
    'referer': 'https://smailpro.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-rapidapi-ua': 'RapidAPI-Playground',
}

    params = {
    'key': key,
    'rapidapi-key': 'f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081',
    'domain': 'gmail.com',
    'username': 'random',
    'server': 'server-1',
    'type': 'alias',
}

    response = requests.get('https://public-sonjj.p.rapidapi.com/email/gm/get', params=params, headers=headers)

    email = (response.json()['items']['email'])
    times = response.json()['items']['timestamp']
    data = {
      "status":"ok",
      "info":{"Email":f"{email}","Timestamp":f"{times}"},
      "by":"@trprogram On Telegram."

    }
    return data
@app.route("/")
def home():
  return "hello :)"
@app.route("/getMessages")
def get():
  email = request.args.get("email")
  timest = request.args.get("timestamp")    
    
  import requests

  cookies = {
    'version': 'eyJpdiI6InhEbk82WFdXZk1pL0xnUjdYSk5CbEE9PSIsInZhbHVlIjoiL2Z4bHU1VjlzMDZzVG43VE0xQ2d5SWhiVUpiNmhaRjFWU2twOE9vOTdmMVY2Z2xza28wZFBHT3ltSlpsK1lGYyIsIm1hYyI6IjE1N2IxM2I3Y2RjYzNkODUyMWFhMjdhODZjM2Q0MDk0MjI4YmMxNTcyMDQyMjRkNzNhYWI5YWZkMzJkMDFlNGUifQ%3D%3D',
    '__gads': 'ID=6a5ff601c9997a4d-226a488c21d50011:T=1662179359:RT=1662179359:S=ALNI_Mb-zRKzuyy8phLIGTKSQN7BjDwxLg',
    '__gpi': 'UID=00000ab01e4cad97:T=1662179359:RT=1662204821:S=ALNI_MYRXqGKobZOut5A7p2kEZs2sWeiTw',
    'XSRF-TOKEN': 'eyJpdiI6InlTNFRVQ3lKK2VVYWhzR1EvR0RHT1E9PSIsInZhbHVlIjoiZ0hOTG1LQVg1ZlVNcUVoYWRBWTcxSER0NDZNdTNzUUUybTdQK1BlL3QrZUpSNmlqWEhhYjlBK2tTWTBNcCtLcHpnM3FUVFgwSi9nOHZMVWp5Rms3T2F0b2llVnRSamkyTlpEc2gxQmhIWGR5K2tYdC8zTTBOQ2dRR0VsYUtwSVIiLCJtYWMiOiIzMTA0ODVkNGM5ODk0MzFjZTUxZDRkODQzN2VkM2JkZjBiNTg0YWMyNGJlMWM0YjZiZWU0Mjc2ZWRhYjVkNWQxIn0%3D',
    'sonjj_session': 'eyJpdiI6InlFblRwSUtmKzhRUjl0MkVQbWVCTXc9PSIsInZhbHVlIjoieC9ENlVXcWJBVmR0eGgrREE5TVBKb3VZVGdxcGlCYmpNcFE5aEl3ZkZPeGlQL2JwT0tJTlZldk13LzNsUnRaOEtrdnF5dUhvMjdPZzYxR29UUDhRVWJYb05YblhCZ3BGeWtGUmpLeDlxRDh2eDlRR2o1UG91NDBlQ2V2Q1hjZFciLCJtYWMiOiIyMDdmNWE2MTcxZjJjNmExYjA1NGZhMmUxODEzNTYzMjI2NzJiNmI3NjQ1MDQ1MTcwZGFmNjhlMGVhNmE3NmYxIn0%3D',
}

  headers = {
    'authority': 'smailpro.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'version=eyJpdiI6InhEbk82WFdXZk1pL0xnUjdYSk5CbEE9PSIsInZhbHVlIjoiL2Z4bHU1VjlzMDZzVG43VE0xQ2d5SWhiVUpiNmhaRjFWU2twOE9vOTdmMVY2Z2xza28wZFBHT3ltSlpsK1lGYyIsIm1hYyI6IjE1N2IxM2I3Y2RjYzNkODUyMWFhMjdhODZjM2Q0MDk0MjI4YmMxNTcyMDQyMjRkNzNhYWI5YWZkMzJkMDFlNGUifQ%3D%3D; __gads=ID=6a5ff601c9997a4d-226a488c21d50011:T=1662179359:RT=1662179359:S=ALNI_Mb-zRKzuyy8phLIGTKSQN7BjDwxLg; __gpi=UID=00000ab01e4cad97:T=1662179359:RT=1662204821:S=ALNI_MYRXqGKobZOut5A7p2kEZs2sWeiTw; XSRF-TOKEN=eyJpdiI6InlTNFRVQ3lKK2VVYWhzR1EvR0RHT1E9PSIsInZhbHVlIjoiZ0hOTG1LQVg1ZlVNcUVoYWRBWTcxSER0NDZNdTNzUUUybTdQK1BlL3QrZUpSNmlqWEhhYjlBK2tTWTBNcCtLcHpnM3FUVFgwSi9nOHZMVWp5Rms3T2F0b2llVnRSamkyTlpEc2gxQmhIWGR5K2tYdC8zTTBOQ2dRR0VsYUtwSVIiLCJtYWMiOiIzMTA0ODVkNGM5ODk0MzFjZTUxZDRkODQzN2VkM2JkZjBiNTg0YWMyNGJlMWM0YjZiZWU0Mjc2ZWRhYjVkNWQxIn0%3D; sonjj_session=eyJpdiI6InlFblRwSUtmKzhRUjl0MkVQbWVCTXc9PSIsInZhbHVlIjoieC9ENlVXcWJBVmR0eGgrREE5TVBKb3VZVGdxcGlCYmpNcFE5aEl3ZkZPeGlQL2JwT0tJTlZldk13LzNsUnRaOEtrdnF5dUhvMjdPZzYxR29UUDhRVWJYb05YblhCZ3BGeWtGUmpLeDlxRDh2eDlRR2o1UG91NDBlQ2V2Q1hjZFciLCJtYWMiOiIyMDdmNWE2MTcxZjJjNmExYjA1NGZhMmUxODEzNTYzMjI2NzJiNmI3NjQ1MDQ1MTcwZGFmNjhlMGVhNmE3NmYxIn0%3D',
    'origin': 'https://smailpro.com',
    'referer': 'https://smailpro.com/advanced',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    #'x-xsrf-token': 'eyJpdiI6InlTNFRVQ3lKK2VVYWhzR1EvR0RHT1E9PSIsInZhbHVlIjoiZ0hOTG1LQVg1ZlVNcUVoYWRBWTcxSER0NDZNdTNzUUUybTdQK1BlL3QrZUpSNmlqWEhhYjlBK2tTWTBNcCtLcHpnM3FUVFgwSi9nOHZMVWp5Rms3T2F0b2llVnRSamkyTlpEc2gxQmhIWGR5K2tYdC8zTTBOQ2dRR0VsYUtwSVIiLCJtYWMiOiIzMTA0ODVkNGM5ODk0MzFjZTUxZDRkODQzN2VkM2JkZjBiNTg0YWMyNGJlMWM0YjZiZWU0Mjc2ZWRhYjVkNWQxIn0=',
}

  json_data = {
    'email': email,
    'timestamp': timest,
}

  response = requests.post('https://smailpro.com/app/key', headers=headers, json=json_data).json()
  keyy = response['items']
  headers = {
    'authority': 'public-sonjj.p.rapidapi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://smailpro.com',
    'referer': 'https://smailpro.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-rapidapi-ua': 'RapidAPI-Playground',
}
  par = {
    "key": keyy,
    "rapidapi-key": "f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081",
    "email": f"{email}",
    "timestamp": timest
}
  response = requests.get(f'https://public-sonjj.p.rapidapi.com/email/gm/check',params=par, headers=headers).json()
  lists =(response['items'])
  data = {
    "status":"ok",
    "messages":{"list":f"{lists}"},
  }
  return data
app.run(host="0.0.0.0",port=8080)
