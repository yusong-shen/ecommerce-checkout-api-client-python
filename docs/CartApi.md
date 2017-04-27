# swagger_client.CartApi

All URIs are relative to *https://ecommerce-checkout-flow-v1.herokuapp.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_available_countries_get_using_get**](CartApi.md#checkout_available_countries_get_using_get) | **GET** /checkout/availableCountries | Get available billing and shipping countries
[**checkout_checkout_id_available_payment_methods_get_using_get**](CartApi.md#checkout_checkout_id_available_payment_methods_get_using_get) | **GET** /checkout/{checkoutId}/availablePaymentMethods | Get available payment methods
[**checkout_checkout_id_available_shipping_methods_get_using_get**](CartApi.md#checkout_checkout_id_available_shipping_methods_get_using_get) | **GET** /checkout/{checkoutId}/availableShippingMethods | Get shipping info
[**checkout_checkout_id_billing_address_put_using_put**](CartApi.md#checkout_checkout_id_billing_address_put_using_put) | **PUT** /checkout/{checkoutId}/billingAddress | Update the billing address
[**checkout_checkout_id_customer_attributes_put_using_put**](CartApi.md#checkout_checkout_id_customer_attributes_put_using_put) | **PUT** /checkout/{checkoutId}/customerAttributes | Set or update customer attributes
[**checkout_checkout_id_get_using_get**](CartApi.md#checkout_checkout_id_get_using_get) | **GET** /checkout/{checkoutId} | Get an existing cart
[**checkout_checkout_id_items_item_id_delete_using_delete**](CartApi.md#checkout_checkout_id_items_item_id_delete_using_delete) | **DELETE** /checkout/{checkoutId}/items/{itemId} | Delete an item from the shopping cart
[**checkout_checkout_id_items_item_id_put_using_put**](CartApi.md#checkout_checkout_id_items_item_id_put_using_put) | **PUT** /checkout/{checkoutId}/items/{itemId} | Update an existing item from the shopping cart
[**checkout_checkout_id_pay_post_using_post**](CartApi.md#checkout_checkout_id_pay_post_using_post) | **POST** /checkout/{checkoutId}/pay | Pay the cart total
[**checkout_checkout_id_shipping_address_put_using_put**](CartApi.md#checkout_checkout_id_shipping_address_put_using_put) | **PUT** /checkout/{checkoutId}/shippingAddress | Update the shipping address
[**checkout_checkout_id_shipping_method_put_using_put**](CartApi.md#checkout_checkout_id_shipping_method_put_using_put) | **PUT** /checkout/{checkoutId}/shippingMethod | Set or update the shipping method
[**create_cart_using_post**](CartApi.md#create_cart_using_post) | **POST** /checkout | Create a possibly empty shopping cart
[**create_item_using_post**](CartApi.md#create_item_using_post) | **POST** /checkout/{checkoutId}/items | Add a new item to the shopping cart


# **checkout_available_countries_get_using_get**
> AvailableCountries checkout_available_countries_get_using_get()

Get available billing and shipping countries

### Example 
```python
from __future__ import print_statement
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
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableCountries**](AvailableCountries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_available_payment_methods_get_using_get**
> AvailablePaymentMethodList checkout_checkout_id_available_payment_methods_get_using_get(checkout_id)

Get available payment methods

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id

try: 
    # Get available payment methods
    api_response = api_instance.checkout_checkout_id_available_payment_methods_get_using_get(checkout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_available_payment_methods_get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 

### Return type

[**AvailablePaymentMethodList**](AvailablePaymentMethodList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_available_shipping_methods_get_using_get**
> AvailableShippingMethodList checkout_checkout_id_available_shipping_methods_get_using_get(checkout_id)

Get shipping info

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id

try: 
    # Get shipping info
    api_response = api_instance.checkout_checkout_id_available_shipping_methods_get_using_get(checkout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_available_shipping_methods_get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 

### Return type

[**AvailableShippingMethodList**](AvailableShippingMethodList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_billing_address_put_using_put**
> Checkout checkout_checkout_id_billing_address_put_using_put(checkout_id, body)

Update the billing address

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
body = swagger_client.Address() # Address | Cart object that needs to be updated

try: 
    # Update the billing address
    api_response = api_instance.checkout_checkout_id_billing_address_put_using_put(checkout_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_billing_address_put_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **body** | [**Address**](Address.md)| Cart object that needs to be updated | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_customer_attributes_put_using_put**
> Checkout checkout_checkout_id_customer_attributes_put_using_put(checkout_id, customer_attributes)

Set or update customer attributes

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
customer_attributes = swagger_client.CustomerAttributes() # CustomerAttributes | Customer attributes

try: 
    # Set or update customer attributes
    api_response = api_instance.checkout_checkout_id_customer_attributes_put_using_put(checkout_id, customer_attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_customer_attributes_put_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **customer_attributes** | [**CustomerAttributes**](CustomerAttributes.md)| Customer attributes | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_get_using_get**
> Checkout checkout_checkout_id_get_using_get(checkout_id)

Get an existing cart

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id

try: 
    # Get an existing cart
    api_response = api_instance.checkout_checkout_id_get_using_get(checkout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_items_item_id_delete_using_delete**
> Checkout checkout_checkout_id_items_item_id_delete_using_delete(checkout_id, item_id)

Delete an item from the shopping cart

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
item_id = 'item_id_example' # str | Item Id

try: 
    # Delete an item from the shopping cart
    api_response = api_instance.checkout_checkout_id_items_item_id_delete_using_delete(checkout_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_items_item_id_delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **item_id** | **str**| Item Id | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_items_item_id_put_using_put**
> Checkout checkout_checkout_id_items_item_id_put_using_put(checkout_id, item_id, item)

Update an existing item from the shopping cart

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
item_id = 'item_id_example' # str | Item Id
item = swagger_client.Product() # Product | Item

try: 
    # Update an existing item from the shopping cart
    api_response = api_instance.checkout_checkout_id_items_item_id_put_using_put(checkout_id, item_id, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_items_item_id_put_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **item_id** | **str**| Item Id | 
 **item** | [**Product**](Product.md)| Item | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_pay_post_using_post**
> checkout_checkout_id_pay_post_using_post(checkout_id, body)

Pay the cart total

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
body = swagger_client.PaymentMethod() # PaymentMethod | Payment method

try: 
    # Pay the cart total
    api_instance.checkout_checkout_id_pay_post_using_post(checkout_id, body)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_pay_post_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **body** | [**PaymentMethod**](PaymentMethod.md)| Payment method | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_shipping_address_put_using_put**
> Checkout checkout_checkout_id_shipping_address_put_using_put(checkout_id, body)

Update the shipping address

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
body = swagger_client.Address() # Address | Shipping address

try: 
    # Update the shipping address
    api_response = api_instance.checkout_checkout_id_shipping_address_put_using_put(checkout_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_shipping_address_put_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **body** | [**Address**](Address.md)| Shipping address | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_checkout_id_shipping_method_put_using_put**
> Checkout checkout_checkout_id_shipping_method_put_using_put(checkout_id, shipping_method)

Set or update the shipping method

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
shipping_method = 'shipping_method_example' # str | Shipping method (0: Express, 1: Standard, 2: Economy)

try: 
    # Set or update the shipping method
    api_response = api_instance.checkout_checkout_id_shipping_method_put_using_put(checkout_id, shipping_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->checkout_checkout_id_shipping_method_put_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **shipping_method** | **str**| Shipping method (0: Express, 1: Standard, 2: Economy) | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cart_using_post**
> Checkout create_cart_using_post(cart)

Create a possibly empty shopping cart

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
cart = swagger_client.Cart() # Cart | Includes billing and products info

try: 
    # Create a possibly empty shopping cart
    api_response = api_instance.create_cart_using_post(cart)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->create_cart_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart** | [**Cart**](Cart.md)| Includes billing and products info | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_using_post**
> Checkout create_item_using_post(checkout_id, item)

Add a new item to the shopping cart

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CartApi()
checkout_id = 'checkout_id_example' # str | Checkout Id
item = swagger_client.Product() # Product | Item to be added to the cart

try: 
    # Add a new item to the shopping cart
    api_response = api_instance.create_item_using_post(checkout_id, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartApi->create_item_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| Checkout Id | 
 **item** | [**Product**](Product.md)| Item to be added to the cart | 

### Return type

[**Checkout**](Checkout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

