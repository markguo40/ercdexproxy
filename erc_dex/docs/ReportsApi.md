# erc_dex.ReportsApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ticker_data**](ReportsApi.md#get_ticker_data) | **GET** /reports/ticker | 


# **get_ticker_data**
> list[ITokenTicker] get_ticker_data()



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.ReportsApi()

try:
    api_response = api_instance.get_ticker_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_ticker_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ITokenTicker]**](ITokenTicker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

