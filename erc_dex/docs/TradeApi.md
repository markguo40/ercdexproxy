# erc_dex.TradeApi

All URIs are relative to *https://app.ercdex.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fill**](TradeApi.md#fill) | **POST** /trade/fill | 
[**get_market_quote**](TradeApi.md#get_market_quote) | **POST** /trade/market_quote | 
[**get_market_quote_by_percent**](TradeApi.md#get_market_quote_by_percent) | **POST** /trade/market_quote_by_percent | 
[**get_receipt**](TradeApi.md#get_receipt) | **GET** /trade/receipt/{id} | 
[**get_receipts**](TradeApi.md#get_receipts) | **GET** /trade/receipts | 
[**request_fill**](TradeApi.md#request_fill) | **POST** /trade/request_fill | 


# **fill**
> FillReceipt fill(request)



Redeem a signed quote (see RequestFill to receive a quote)

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeApi()
request = erc_dex.IFillRequest() # IFillRequest | 

try:
    api_response = api_instance.fill(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IFillRequest**](IFillRequest.md)|  | 

### Return type

[**FillReceipt**](FillReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_quote**
> IMarketOrderQuote get_market_quote(request)



Get a quote for a requested quantity

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeApi()
request = erc_dex.IGetMarketOrderQuoteRequest() # IGetMarketOrderQuoteRequest | 

try:
    api_response = api_instance.get_market_quote(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->get_market_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IGetMarketOrderQuoteRequest**](IGetMarketOrderQuoteRequest.md)|  | 

### Return type

[**IMarketOrderQuote**](IMarketOrderQuote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_quote_by_percent**
> IMarketOrderQuote get_market_quote_by_percent(request)



Get a quote by percentage

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeApi()
request = erc_dex.IGetMarketOrderQuoteByPercentageRequest() # IGetMarketOrderQuoteByPercentageRequest | 

try:
    api_response = api_instance.get_market_quote_by_percent(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->get_market_quote_by_percent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IGetMarketOrderQuoteByPercentageRequest**](IGetMarketOrderQuoteByPercentageRequest.md)|  | 

### Return type

[**IMarketOrderQuote**](IMarketOrderQuote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt**
> FillReceipt get_receipt(id)



Get a receipt of an attempted fill

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeApi()
id = 1.2 # float | 

try:
    api_response = api_instance.get_receipt(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->get_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**FillReceipt**](FillReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts**
> IGetReceiptsResponse get_receipts(page=page, per_page=per_page, taker_address=taker_address, pair=pair, maker_address=maker_address, order_id=order_id)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeApi()
page = 1 # float | Page (optional) (default to 1)
per_page = 100 # float | Page size (optional) (default to 100)
taker_address = 'taker_address_example' # str | Optionally provide wallet address of receipt recipient (optional)
pair = 'pair_example' # str | The token pair in the format BASE/QUOTE, e.g. ZRX/WETH (optional)
maker_address = 'maker_address_example' # str | Optionally provide wallet address of order maker (optional)
order_id = 1.2 # float |  (optional)

try:
    api_response = api_instance.get_receipts(page=page, per_page=per_page, taker_address=taker_address, pair=pair, maker_address=maker_address, order_id=order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->get_receipts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Page | [optional] [default to 1]
 **per_page** | **float**| Page size | [optional] [default to 100]
 **taker_address** | **str**| Optionally provide wallet address of receipt recipient | [optional] 
 **pair** | **str**| The token pair in the format BASE/QUOTE, e.g. ZRX/WETH | [optional] 
 **maker_address** | **str**| Optionally provide wallet address of order maker | [optional] 
 **order_id** | **float**|  | [optional] 

### Return type

[**IGetReceiptsResponse**](IGetReceiptsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_fill**
> MarketQuote request_fill(request)



Request to fill an order; returns a quote payload that can be signed and redeemed to begin execution

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeApi()
request = erc_dex.IRequestFillRequest() # IRequestFillRequest | 

try:
    api_response = api_instance.request_fill(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeApi->request_fill: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IRequestFillRequest**](IRequestFillRequest.md)|  | 

### Return type

[**MarketQuote**](MarketQuote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

