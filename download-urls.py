import os
import requests
import time

# Read the URLs from the text file
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

# Read the cookies from the text file
with open('cookies.txt', 'r') as file:
    cookies = file.read().splitlines()

# Download each file
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie.split('=')[0], cookie.split('=')[1])

for url in urls:
        
        # Set the headers
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9,he;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'DNT': '1',
            'Origin': 'https://www.remini.me',
            'Pragma': 'no-cache',
            'Referer': 'https://www.remini.me/all/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        
        # Set the cookie and headers
        session.headers.update(headers)
        
        # Sleep for 100 miliseconds
        time.sleep(0.1)

        # Download the file
        response = session.get(url)
        if response.status_code == 200:
            filename = url.split('/')[-1]
            with open(os.path.join('output', filename), 'wb') as file:
                file.write(response.content)
                print(f"Downloaded {filename} to output folder")
        else:
            print(f"Failed to download {url}")
