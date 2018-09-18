# erc_dex.AggregatedOrdersApi

All URIs are relative to *https://app.ercdex.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregated_orders**](AggregatedOrdersApi.md#get_aggregated_orders) | **GET** /aggregated_orders | 


# **get_aggregated_orders**
> IAggregatedOrderData get_aggregated_orders(base_symbol, quote_symbol)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.AggregatedOrdersApi()
base_symbol = 'base_symbol_example' # str | 
quote_symbol = 'quote_symbol_example' # str | 

try:
    api_response = api_instance.get_aggregated_orders(base_symbol, quote_symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregatedOrdersApi->get_aggregated_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_symbol** | **str**|  | 
 **quote_symbol** | **str**|  | 

### Return type

[**IAggregatedOrderData**](IAggregatedOrderData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

