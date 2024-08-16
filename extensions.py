<<<<<<< HEAD
# extensions.py
import requests
import json

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            url = f'https://api.exchangerate-api.com/v4/latest/{base}'
            response = requests.get(url)
            data = json.loads(response.text)

            if quote not in data['rates']:
                raise APIException(f'Invalid currency: {quote}')

            rate = data['rates'][quote]
            result = amount * rate
            return result

        except Exception as e:
            raise APIException(f'Error fetching data from API: {str(e)}')


class APIException(Exception):
    pass

=======
# extensions.py
import requests
import json

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            url = f'https://api.exchangerate-api.com/v4/latest/{base}'
            response = requests.get(url)
            data = json.loads(response.text)

            if quote not in data['rates']:
                raise APIException(f'Invalid currency: {quote}')

            rate = data['rates'][quote]
            result = amount * rate
            return result

        except Exception as e:
            raise APIException(f'Error fetching data from API: {str(e)}')


class APIException(Exception):
    pass

>>>>>>> ff38df81652acdabb4ed80bc0cc18d2dd99c347f
