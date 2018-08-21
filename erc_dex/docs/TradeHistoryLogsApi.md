# erc_dex.TradeHistoryLogsApi

All URIs are relative to *https://api.ercdex.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trade_history_logs**](TradeHistoryLogsApi.md#get_trade_history_logs) | **GET** /trade_history_logs | 


# **get_trade_history_logs**
> IGetTradeHistoryLogsResponse get_trade_history_logs(page=page, per_page=per_page, sort_order=sort_order, sort_direction=sort_direction, relayer=relayer, maker=maker, fee_recipient=fee_recipient, maker_token_address=maker_token_address, maker_token_symbol=maker_token_symbol, taker=taker, taker_token_address=taker_token_address, taker_token_symbol=taker_token_symbol, order_hash=order_hash, token_address=token_address, token_symbol=token_symbol, tx_hash=tx_hash, trader=trader, min_date=min_date, max_date=max_date, format=format, pair=pair)



### Example
```python
from __future__ import print_function
import time
import erc_dex
from erc_dex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = erc_dex.TradeHistoryLogsApi()
page = 1 # float | Page number (default: 1) (optional) (default to 1)
per_page = 20 # float | Page size (max 1000, default: 20) (optional) (default to 20)
sort_order = 'date' # str | Sort order (default: 'date'). date: Sort by trade date (optional) (default to date)
sort_direction = 'desc' # str | Sort direction (default: 'desc'). Options: asc: Ascending, desc: Descending (optional) (default to desc)
relayer = 'relayer_example' # str | Name of originating 0x relayer (optional)
maker = 'maker_example' # str | Address of order maker (optional)
fee_recipient = 'fee_recipient_example' # str | Address of order feeRecipient (optional)
maker_token_address = 'maker_token_address_example' # str | Address of maker token (optional)
maker_token_symbol = 'maker_token_symbol_example' # str | Symbol of maker token (optional)
taker = 'taker_example' # str | Address of order taker (optional)
taker_token_address = 'taker_token_address_example' # str | Address of taker token (optional)
taker_token_symbol = 'taker_token_symbol_example' # str | Symbol of taker token (optional)
order_hash = 'order_hash_example' # str | Unique, generated hash representing 0x order (optional)
token_address = 'token_address_example' # str | Address of token that is either maker or taker (optional)
token_symbol = 'token_symbol_example' # str | Symbol of token that is either maker or taker (optional)
tx_hash = 'tx_hash_example' # str | Transaction hash (optional)
trader = 'trader_example' # str | Address of either maker or taker (optional)
min_date = '2013-10-20T19:20:30+01:00' # datetime | Minimum trade date: format (UTC): 2017-01-01T00:00:00.000Z (optional)
max_date = '2013-10-20T19:20:30+01:00' # datetime | Maximum trade date. Format (UTC): 2017-01-01T00:00:00.000Z (optional)
format = 'json' # str | Result format (default: 'json'). Options: 'json', 'csv'. CSV: Page size limited to 10000 records (optional) (default to json)
pair = 'pair_example' # str | Token pair. Format: base_token_symbol/quote_token_symbol. Example: ZRX/WETH (optional)

try:
    api_response = api_instance.get_trade_history_logs(page=page, per_page=per_page, sort_order=sort_order, sort_direction=sort_direction, relayer=relayer, maker=maker, fee_recipient=fee_recipient, maker_token_address=maker_token_address, maker_token_symbol=maker_token_symbol, taker=taker, taker_token_address=taker_token_address, taker_token_symbol=taker_token_symbol, order_hash=order_hash, token_address=token_address, token_symbol=token_symbol, tx_hash=tx_hash, trader=trader, min_date=min_date, max_date=max_date, format=format, pair=pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeHistoryLogsApi->get_trade_history_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Page number (default: 1) | [optional] [default to 1]
 **per_page** | **float**| Page size (max 1000, default: 20) | [optional] [default to 20]
 **sort_order** | **str**| Sort order (default: &#39;date&#39;). date: Sort by trade date | [optional] [default to date]
 **sort_direction** | **str**| Sort direction (default: &#39;desc&#39;). Options: asc: Ascending, desc: Descending | [optional] [default to desc]
 **relayer** | **str**| Name of originating 0x relayer | [optional] 
 **maker** | **str**| Address of order maker | [optional] 
 **fee_recipient** | **str**| Address of order feeRecipient | [optional] 
 **maker_token_address** | **str**| Address of maker token | [optional] 
 **maker_token_symbol** | **str**| Symbol of maker token | [optional] 
 **taker** | **str**| Address of order taker | [optional] 
 **taker_token_address** | **str**| Address of taker token | [optional] 
 **taker_token_symbol** | **str**| Symbol of taker token | [optional] 
 **order_hash** | **str**| Unique, generated hash representing 0x order | [optional] 
 **token_address** | **str**| Address of token that is either maker or taker | [optional] 
 **token_symbol** | **str**| Symbol of token that is either maker or taker | [optional] 
 **tx_hash** | **str**| Transaction hash | [optional] 
 **trader** | **str**| Address of either maker or taker | [optional] 
 **min_date** | **datetime**| Minimum trade date: format (UTC): 2017-01-01T00:00:00.000Z | [optional] 
 **max_date** | **datetime**| Maximum trade date. Format (UTC): 2017-01-01T00:00:00.000Z | [optional] 
 **format** | **str**| Result format (default: &#39;json&#39;). Options: &#39;json&#39;, &#39;csv&#39;. CSV: Page size limited to 10000 records | [optional] [default to json]
 **pair** | **str**| Token pair. Format: base_token_symbol/quote_token_symbol. Example: ZRX/WETH | [optional] 

### Return type

[**IGetTradeHistoryLogsResponse**](IGetTradeHistoryLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

