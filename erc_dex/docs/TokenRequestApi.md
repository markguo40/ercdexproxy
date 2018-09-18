# erc_dex.TokenRequestApi

All URIs are relative to *https://app.ercdex.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_request**](TokenRequestApi.md#create_token_request) | **POST** /token_requests | 


# **create_token_request**
> create_token_request(request)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TokenRequestApi()
request = erc_dex.ITokenRequestRequest() # ITokenRequestRequest | 

try:
    api_instance.create_token_request(request)
except ApiException as e:
    print("Exception when calling TokenRequestApi->create_token_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ITokenRequestRequest**](ITokenRequestRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

