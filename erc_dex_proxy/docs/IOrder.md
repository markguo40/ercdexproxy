# IOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Unique Identifier | 
**date_created** | **datetime** | Date of creation | 
**date_updated** | **datetime** | Date of updated | 
**date_closed** | **datetime** | Date on which the order was closed through fill, cancel, etc | [optional] 
**exchange_address** | **str** | 0x Exchange Contract Address | 
**expiration_time_seconds** | **str** | Unix timestamp of order expiration (in seconds) | 
**fee_recipient_address** | **str** | Address of the fee recipient | 
**maker_address** | **str** | Address of the order maker | 
**maker_fee** | **str** | Fee due from maker on order fill | 
**maker_asset_address** | **str** | Token address of the maker token | 
**maker_asset_data** | **str** | Encoded maker asset data | 
**taker_asset_data** | **str** | Encoded taker asset data | 
**maker_asset_amount** | **str** | Total amount of maker token in order | 
**salt** | **str** | Secure salt | 
**signature** | **str** | Serialized version of the EC signature for signed orders | 
**taker_address** | **str** | Taker address; generally a null taker | 
**taker_fee** | **str** | Fee due from taker on order fill | 
**taker_asset_address** | **str** | Token address of the taker token | 
**taker_asset_amount** | **str** | Total amount of taker token in order | 
**remaining_fillable_taker_amount** | **str** | Remaining amount that can be filled in taker tokens | 
**remaining_fillable_maker_amount** | **str** | Remaining amount that can be filled in maker tokens | 
**order_hash** | **str** | The hash of the signed order | 
**account_id** | **float** | Account ID of originator | [optional] 
**state** | **float** | State of the order: Open (0), Canceled (1), Filled (2), Expired(3), Removed(4) | 
**price** | **str** |  | 
**sender_address** | **str** |  | 
**system** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


