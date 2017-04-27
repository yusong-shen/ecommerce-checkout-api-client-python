from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.CartApi()

try:
    # Get available billing and shipping countries
    api_response = api_instance.checkout_available_countries_get_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_available_countries_get_using_get: %s\n" % e)