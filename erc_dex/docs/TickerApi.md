# erc_dex.TickerApi

All URIs are relative to *https://app.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ticker**](TickerApi.md#get_ticker) | **GET** /ticker | 


# **get_ticker**
> list[IGlobalTickerRecord] get_ticker(granularity=granularity)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TickerApi()
granularity = '24h' # str | Granularity of results: 24h (1 day), 1w (1 week), 1mo (1 month) (optional) (default to 24h)

try:
    api_response = api_instance.get_ticker(granularity=granularity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TickerApi->get_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granularity** | **str**| Granularity of results: 24h (1 day), 1w (1 week), 1mo (1 month) | [optional] [default to 24h]

### Return type

[**list[IGlobalTickerRecord]**](IGlobalTickerRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

