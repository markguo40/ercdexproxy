# erc_dex_proxy.WalletApi

All URIs are relative to *http://localhost:8700/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account**](WalletApi.md#get_account) | **GET** /wallet/account | 
[**get_balance**](WalletApi.md#get_balance) | **GET** /wallet/balance | 
[**get_ether_balance**](WalletApi.md#get_ether_balance) | **GET** /wallet/ether_balance | 
[**unwrap_ether**](WalletApi.md#unwrap_ether) | **POST** /wallet/unwrap_ether | 
[**wrap_ether**](WalletApi.md#wrap_ether) | **POST** /wallet/wrap_ether | 


# **get_account**
> str get_account()



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.WalletApi()

try:
    api_response = api_instance.get_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->get_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> str get_balance(token_address)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.WalletApi()
token_address = 'token_address_example' # str | 

try:
    api_response = api_instance.get_balance(token_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->get_balance: %s\n" % e)
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

# **get_ether_balance**
> str get_ether_balance()



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.WalletApi()

try:
    api_response = api_instance.get_ether_balance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->get_ether_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unwrap_ether**
> unwrap_ether(amount)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.WalletApi()
amount = 'amount_example' # str | 

try:
    api_instance.unwrap_ether(amount)
except ApiException as e:
    print("Exception when calling WalletApi->unwrap_ether: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wrap_ether**
> wrap_ether(amount)



### Example
```python
from __future__ import print_function
import time
import erc_dex_proxy
from erc_dex_proxy.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex_proxy.WalletApi()
amount = 'amount_example' # str | 

try:
    api_instance.wrap_ether(amount)
except ApiException as e:
    print("Exception when calling WalletApi->wrap_ether: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

