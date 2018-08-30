# erc_dex.NewsApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crypto_panic_news**](NewsApi.md#get_crypto_panic_news) | **GET** /news/cryptopanic/{symbol} | 


# **get_crypto_panic_news**
> ICryptoPanicPostsResponse get_crypto_panic_news(symbol)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.NewsApi()
symbol = 'symbol_example' # str | 

try:
    api_response = api_instance.get_crypto_panic_news(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsApi->get_crypto_panic_news: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 

### Return type

[**ICryptoPanicPostsResponse**](ICryptoPanicPostsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

