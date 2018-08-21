# erc_dex.TradingViewApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trading_view_logs**](TradingViewApi.md#get_trading_view_logs) | **GET** /trading_view | 


# **get_trading_view_logs**
> list[ITradingViewLog] get_trading_view_logs(pair, resolution, start_date, end_date)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradingViewApi()
pair = 'pair_example' # str | 
resolution = 'resolution_example' # str | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | 
end_date = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.get_trading_view_logs(pair, resolution, start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradingViewApi->get_trading_view_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pair** | **str**|  | 
 **resolution** | **str**|  | 
 **start_date** | **datetime**|  | 
 **end_date** | **datetime**|  | 

### Return type

[**list[ITradingViewLog]**](ITradingViewLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

