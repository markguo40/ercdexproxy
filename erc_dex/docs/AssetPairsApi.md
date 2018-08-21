# erc_dex.AssetPairsApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_pairs**](AssetPairsApi.md#get_asset_pairs) | **GET** /asset_pairs | 


# **get_asset_pairs**
> IGetAssetPairsResponse get_asset_pairs(page=page, per_page=per_page)



Get a list of supported asset pairs

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.AssetPairsApi()
page = 1 # float |  (optional) (default to 1)
per_page = 100 # float |  (optional) (default to 100)

try:
    api_response = api_instance.get_asset_pairs(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetPairsApi->get_asset_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **per_page** | **float**|  | [optional] [default to 100]

### Return type

[**IGetAssetPairsResponse**](IGetAssetPairsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

