# Binance Portfolio Manager

This project is intended for personal use. It was created to simplify the process of getting information 
from the Binance API. It makes use of python-binance library to carry out the calls.

My idea was to encapsulate all useful methods in classes distinguished by feature, eg: methods related to 
querying orders will be in class Orders. All such classes are accessible via the BinanceApi class.

### Project Setup
1. Set up an API key for Binance using the Binance app. Please follow the instructions available online for this
2. For providing API keys, one of two ways below can be used:
    * Create a file called 'secret' and store API_KEY and API_SECRET in it. Use attached example file.
    * Set API_KEY and API_SECRET environment variables.
    
# Filters to check in orders
https://stackoverflow.com/questions/61582902/python-binance-api-apierrorcode-1013-filter-failure-lot-size