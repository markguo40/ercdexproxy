# erc_dex_proxy.OrderApi

All URIs are relative to *http://localhost:8700/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrderApi.md#cancel_order) | **POST** /order/cancel/{orderHash} | 
[**create_order**](OrderApi.md#create_order) | **POST** /order/create | 
[**fill_order**](OrderApi.md#fill_order) | **POST** /order/fill | 


# **cancel_order**
> str cancel_order(order_hash)



Cancel an existing order

### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.OrderApi()
order_hash = 'order_hash_example' # str | 

try:
    api_response = api_instance.cancel_order(order_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_hash** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> IOrder create_order(params)



Create a new order

### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.OrderApi()
params = erc_dex_proxy.ICreateOrderArgs() # ICreateOrderArgs | 

try:
    api_response = api_instance.create_order(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**ICreateOrderArgs**](ICreateOrderArgs.md)|  | 

### Return type

[**IOrder**](IOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fill_order**
> IFillReceipt fill_order(request)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.OrderApi()
request = erc_dex_proxy.IFillOrdersParams() # IFillOrdersParams | 

try:
    api_response = api_instance.fill_order(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderApi->fill_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IFillOrdersParams**](IFillOrdersParams.md)|  | 

### Return type

[**IFillReceipt**](IFillReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

