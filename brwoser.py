import requests  

url = 'http://google.com'

print(f"try to connect {url}...")

try:
    response = requests.get(url)

    response.raise_for_status()

    print("\n---start HTML ---\n")
    print(response.text)
    print("\n--- end HTML ---\n")

except requests.exceptions.HTTPError as myError:
    print(f"HTTP ERROR: {myError}")
except requests.exceptions.ConnectionError as myError:
    print(f"Connection Error:  {myError}")
except requests.exceptions.Timeout as myError:
    print(f"  (Timeout): {myError}")
except requests.exceptions.RequestException as myError:
    print(f" Req exception   : {myError}")