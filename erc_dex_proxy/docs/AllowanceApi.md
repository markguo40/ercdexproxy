# erc_dex_proxy.AllowanceApi

All URIs are relative to *http://localhost:8700/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allowance**](AllowanceApi.md#get_allowance) | **GET** /wallet/allowances | 
[**remove_allowance**](AllowanceApi.md#remove_allowance) | **POST** /wallet/allowances/remove | 
[**set_allowance**](AllowanceApi.md#set_allowance) | **POST** /wallet/allowances/set | 
[**set_unlimited_allowance**](AllowanceApi.md#set_unlimited_allowance) | **POST** /wallet/allowances/unlimited | 


# **get_allowance**
> str get_allowance(token_address)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.AllowanceApi()
token_address = 'token_address_example' # str | 

try:
    api_response = api_instance.get_allowance(token_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllowanceApi->get_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_address** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_allowance**
> remove_allowance(token_address)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.AllowanceApi()
token_address = 'token_address_example' # str | 

try:
    api_instance.remove_allowance(token_address)
except ApiException as e:
    print("Exception when calling AllowanceApi->remove_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_address** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_allowance**
> set_allowance(token_address, value)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.AllowanceApi()
token_address = 'token_address_example' # str | 
value = 'value_example' # str | 

try:
    api_instance.set_allowance(token_address, value)
except ApiException as e:
    print("Exception when calling AllowanceApi->set_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_address** | **str**|  | 
 **value** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_unlimited_allowance**
> set_unlimited_allowance(token_address)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.AllowanceApi()
token_address = 'token_address_example' # str | 

try:
    api_instance.set_unlimited_allowance(token_address)
except ApiException as e:
    print("Exception when calling AllowanceApi->set_unlimited_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_address** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

