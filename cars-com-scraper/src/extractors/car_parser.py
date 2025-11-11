thonimport json

class CarParser:
    @staticmethod
    def parse_car_data(car_data):
        return {
            "list_url": car_data.get("list_url", ""),
            "record_url": car_data.get("record_url", ""),
            "name": car_data.get("name", ""),
            "description": car_data.get("description", ""),
            "mileage": car_data.get("mileage", ""),
            "price": car_data.get("price", ""),
            "make": car_data.get("make", ""),
            "model": car_data.get("model", ""),
            "trim": car_data.get("trim", ""),
            "year": car_data.get("year", ""),
            "vin": car_data.get("vin", ""),
            "body": car_data.get("body", ""),
            "cylinders": car_data.get("cylinders", ""),
            "doors": car_data.get("doors", ""),
            "drivetrain": car_data.get("drivetrain", ""),
            "exterior_color": car_data.get("exterior_color", ""),
            "interior_color": car_data.get("interior_color", ""),
            "fuel": car_data.get("fuel", ""),
            "transmission": car_data.get("transmission", ""),
            "engine": car_data.get("engine", ""),
            "stock_number": car_data.get("stock_number", ""),
            "features": car_data.get("features", []),
            "images": car_data.get("images", [])
        }