# erc_dex.NotificationsApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /notifications | 


# **get_notifications**
> list[Notification] get_notifications(account)



Get active notifications for an account

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.NotificationsApi()
account = 'account_example' # str | 

try:
    api_response = api_instance.get_notifications(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | 

### Return type

[**list[Notification]**](Notification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

