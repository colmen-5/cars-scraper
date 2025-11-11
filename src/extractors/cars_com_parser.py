thonimport requests
from bs4 import BeautifulSoup

def parse_car_data(url):
    # Send GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    car_listings = []

    # Find all car listings on the page
    listings = soup.find_all('div', class_='vehicle-card')

    for listing in listings:
        car_data = {
            'list_url': url,
            'record_url': listing.find('a')['href'],
            'name': listing.find('h2').text.strip(),
            'price': listing.find('span', class_='primary-price').text.strip(),
            'mileage': listing.find('div', class_='mileage').text.strip() if listing.find('div', class_='mileage') else '',
            'make': listing.find('span', class_='make').text.strip(),
            'model': listing.find('span', class_='model').text.strip(),
            'year': listing.find('span', class_='year').text.strip(),
            'vin': '',  # This might need further scraping from individual listing pages
            'features': []  # Extract features if available
        }
        car_listings.append(car_data)

    return car_listings