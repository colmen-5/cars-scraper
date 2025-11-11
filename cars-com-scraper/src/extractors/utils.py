thonimport re

class Utils:
    @staticmethod
    def clean_text(text):
        return re.sub(r'\s+', ' ', text).strip()

    @staticmethod
    def format_price(price):
        return float(price.replace('$', '').replace(',', '')) if price else 0

    @staticmethod
    def is_valid_url(url):
        return re.match(r'https?://[^\s]+', url) is not None