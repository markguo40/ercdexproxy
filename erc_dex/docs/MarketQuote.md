# MarketQuote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Unique Identifier | 
**date_created** | **datetime** | Date of creation | 
**date_updated** | **datetime** | Date of updated | 
**salt** | **str** | Unique salt | 
**hex** | **str** | Pre-calculated hex to sign | 
**taker_address** | **str** | Order taker | 
**price** | **str** | Computed average price | 
**taker_amount** | **str** | Total taker amount | 
**maker_amount** | **str** | Total maker amount | 
**taker_asset_address** | **str** | Address of taker token | 
**expiration** | **float** | Expiration - unix timestamp in seconds | 
**fee_token_symbol** | **str** | Symbol of the token used to pay fees | 
**fee_amount** | **str** | Amount of fees paid in wei | 
**network_fee_amount** | **str** | Amount of fees paid to cover network fees in wei | 
**state** | **float** | State of the quote (Open [0], Expired [1], Invalid [2], Redeemed [3]) | 
**fee_order_id** | **float** | ID of order used to pay fees | [optional] 
**fee_order** | [**Order**](Order.md) | Order used to pay fees | [optional] 
**fills** | [**list[MarketQuoteFill]**](MarketQuoteFill.md) | Collection of fills | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


