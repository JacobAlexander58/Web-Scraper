import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL to scrape
url = "https://example.com"  # Replace with the target URL

# Step 2: Send a GET request to the URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(url, headers=headers)

# Step 3: Check if request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 5: Find the elements you want (replace with actual tags/classes)
    items = soup.find_all("div", class_="target-class")  # Modify as needed

    # Step 6: Extract and print data
    for item in items:
        title = item.get_text(strip=True)
        print(title)

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
