# erc_dex.OrdersApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_orders**](OrdersApi.md#cancel_orders) | **POST** /orders/cancel | 
[**create_order**](OrdersApi.md#create_order) | **POST** /orders | 
[**get_fee_recipients**](OrdersApi.md#get_fee_recipients) | **GET** /fee_recipients | 
[**get_order_by_hash**](OrdersApi.md#get_order_by_hash) | **GET** /order/{orderHash} | 
[**get_order_config**](OrdersApi.md#get_order_config) | **GET** /order_config | 
[**get_orderbook**](OrdersApi.md#get_orderbook) | **GET** /orderbook | 
[**get_orders**](OrdersApi.md#get_orders) | **GET** /orders | 


# **cancel_orders**
> list[ICancelOrderResult] cancel_orders(request)



Cancel one or more orders

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()
request = erc_dex.ICancelOrdersRequest() # ICancelOrdersRequest | 

try:
    api_response = api_instance.cancel_orders(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ICancelOrdersRequest**](ICancelOrdersRequest.md)|  | 

### Return type

[**list[ICancelOrderResult]**](ICancelOrderResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> Order create_order(request)



Submit a signed order

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()
request = erc_dex.IOrderCreationRequest() # IOrderCreationRequest | 

try:
    api_response = api_instance.create_order(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**IOrderCreationRequest**](IOrderCreationRequest.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_recipients**
> IFeeRecipientsResponse get_fee_recipients()



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()

try:
    api_response = api_instance.get_fee_recipients()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_fee_recipients: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IFeeRecipientsResponse**](IFeeRecipientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_hash**
> IOrderData get_order_by_hash(order_hash)



Get a single order by hash

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()
order_hash = 'order_hash_example' # str | Hex format hash of order parameters

try:
    api_response = api_instance.get_order_by_hash(order_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_by_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_hash** | **str**| Hex format hash of order parameters | 

### Return type

[**IOrderData**](IOrderData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_config**
> IOrderConfig get_order_config(maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()
maker_address = 'maker_address_example' # str | 
taker_address = 'taker_address_example' # str | 
maker_asset_amount = 'maker_asset_amount_example' # str | 
taker_asset_amount = 'taker_asset_amount_example' # str | 
maker_asset_data = 'maker_asset_data_example' # str | 
taker_asset_data = 'taker_asset_data_example' # str | 
exchange_address = 'exchange_address_example' # str | 

try:
    api_response = api_instance.get_order_config(maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maker_address** | **str**|  | 
 **taker_address** | **str**|  | 
 **maker_asset_amount** | **str**|  | 
 **taker_asset_amount** | **str**|  | 
 **maker_asset_data** | **str**|  | 
 **taker_asset_data** | **str**|  | 
 **exchange_address** | **str**|  | 

### Return type

[**IOrderConfig**](IOrderConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderbook**
> IOrderbookResponse get_orderbook(base_asset_data, quote_asset_data, per_page=per_page, page=page)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()
base_asset_data = 'base_asset_data_example' # str | 
quote_asset_data = 'quote_asset_data_example' # str | 
per_page = 100 # float |  (optional) (default to 100)
page = 1 # float |  (optional) (default to 1)

try:
    api_response = api_instance.get_orderbook(base_asset_data, quote_asset_data, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_orderbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_data** | **str**|  | 
 **quote_asset_data** | **str**|  | 
 **per_page** | **float**|  | [optional] [default to 100]
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**IOrderbookResponse**](IOrderbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> IGetOrdersResponse get_orders(open=open, page=page, per_page=per_page, exchange_address=exchange_address, fee_recipient_address=fee_recipient_address, taker_asset_data=taker_asset_data, maker_asset_data=maker_asset_data, sender_address=sender_address, trader_asset_data=trader_asset_data, trader_address=trader_address, taker_asset_address=taker_asset_address, taker_address=taker_address, maker_asset_address=maker_asset_address, maker_address=maker_address, maker_asset_proxy_id=maker_asset_proxy_id, taker_asset_proxy_id=taker_asset_proxy_id, pair=pair)



Get a list of orders

### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.OrdersApi()
open = true # bool | Include orders that are open; if false, only closed orders are returned (optional) (default to true)
page = 1 # float | Page number (optional) (default to 1)
per_page = 100 # float | Page size (optional) (default to 100)
exchange_address = 'exchange_address_example' # str | 0x contract exchange address (optional)
fee_recipient_address = 'fee_recipient_address_example' # str | Fee recipient address (optional)
taker_asset_data = 'taker_asset_data_example' # str | Encoded taker asset data (optional)
maker_asset_data = 'maker_asset_data_example' # str | Encoded maker asset data (optional)
sender_address = 'sender_address_example' # str | Designated address to execute orders (optional)
trader_asset_data = 'trader_asset_data_example' # str | Encoded asset data (could be maker or taker) (optional)
trader_address = 'trader_address_example' # str | Trader address (could be makerAddress or takerAddress) (optional)
taker_asset_address = 'taker_asset_address_example' # str | Token address of taker asset (optional)
taker_address = 'taker_address_example' # str | Address of order taker (optional)
maker_asset_address = 'maker_asset_address_example' # str | Token address of maker asset (optional)
maker_address = 'maker_address_example' # str | Address of order maker (optional)
maker_asset_proxy_id = 'maker_asset_proxy_id_example' # str |  (optional)
taker_asset_proxy_id = 'taker_asset_proxy_id_example' # str |  (optional)
pair = 'pair_example' # str |  (optional)

try:
    api_response = api_instance.get_orders(open=open, page=page, per_page=per_page, exchange_address=exchange_address, fee_recipient_address=fee_recipient_address, taker_asset_data=taker_asset_data, maker_asset_data=maker_asset_data, sender_address=sender_address, trader_asset_data=trader_asset_data, trader_address=trader_address, taker_asset_address=taker_asset_address, taker_address=taker_address, maker_asset_address=maker_asset_address, maker_address=maker_address, maker_asset_proxy_id=maker_asset_proxy_id, taker_asset_proxy_id=taker_asset_proxy_id, pair=pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open** | **bool**| Include orders that are open; if false, only closed orders are returned | [optional] [default to true]
 **page** | **float**| Page number | [optional] [default to 1]
 **per_page** | **float**| Page size | [optional] [default to 100]
 **exchange_address** | **str**| 0x contract exchange address | [optional] 
 **fee_recipient_address** | **str**| Fee recipient address | [optional] 
 **taker_asset_data** | **str**| Encoded taker asset data | [optional] 
 **maker_asset_data** | **str**| Encoded maker asset data | [optional] 
 **sender_address** | **str**| Designated address to execute orders | [optional] 
 **trader_asset_data** | **str**| Encoded asset data (could be maker or taker) | [optional] 
 **trader_address** | **str**| Trader address (could be makerAddress or takerAddress) | [optional] 
 **taker_asset_address** | **str**| Token address of taker asset | [optional] 
 **taker_address** | **str**| Address of order taker | [optional] 
 **maker_asset_address** | **str**| Token address of maker asset | [optional] 
 **maker_address** | **str**| Address of order maker | [optional] 
 **maker_asset_proxy_id** | **str**|  | [optional] 
 **taker_asset_proxy_id** | **str**|  | [optional] 
 **pair** | **str**|  | [optional] 

### Return type

[**IGetOrdersResponse**](IGetOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

