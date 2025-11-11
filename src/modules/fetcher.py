thonimport requests
from utils.logger import log_info, log_error

def fetch_car_listings(urls):
    listings = []
    for url in urls:
        try:
            log_info(f"Fetching data from {url}")
            response = requests.get(url)
            response.raise_for_status()
            listings.append(response.text)
        except requests.exceptions.RequestException as e:
            log_error(f"Failed to fetch from {url}: {e}")
    return listings