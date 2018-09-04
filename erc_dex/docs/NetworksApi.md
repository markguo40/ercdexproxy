# erc_dex.NetworksApi

All URIs are relative to *https://app.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_network**](NetworksApi.md#get_supported_network) | **GET** /networks | 
[**is_maintenance**](NetworksApi.md#is_maintenance) | **GET** /networks/maintenance | 


# **get_supported_network**
> INetwork get_supported_network()



Get supported network info

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.NetworksApi()

try:
    api_response = api_instance.get_supported_network()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->get_supported_network: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**INetwork**](INetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_maintenance**
> IMaintenanceStatus is_maintenance()



Determine if app is in maintenance mode

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.NetworksApi()

try:
    api_response = api_instance.is_maintenance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworksApi->is_maintenance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IMaintenanceStatus**](IMaintenanceStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

