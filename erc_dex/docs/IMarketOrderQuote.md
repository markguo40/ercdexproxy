# IMarketOrderQuote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Unique quote identifier | 
**fills** | [**list[IExtendedOrderFill]**](IExtendedOrderFill.md) | Collection of fills | 
**salt** | **str** | Unique salt | 
**hex** | **str** | Pre-calculated hex to sign | 
**taker** | **str** | Order taker | 
**fee_data** | [**IFeeData**](IFeeData.md) | Contains information regarding any applicable fees | [optional] 
**token_pair** | [**ITokenPair**](ITokenPair.md) | Trade token pair | 
**price** | **str** | Computed average price | 
**taker_amount** | **str** | Total taker amount | 
**maker_amount** | **str** | Total maker amount | 
**taker_asset_address** | **str** | Address of taker token | 
**is_partial** | **bool** | Can only provide a partial quote | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


