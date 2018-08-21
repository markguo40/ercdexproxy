# IOrderCreationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker_address** | **str** | Order maker | 
**taker_address** | **str** | Order taker; should generally be the null address (0x000...) in the case of ERC dEX | 
**fee_recipient_address** | **str** | Recipient of owed fees | 
**sender_address** | **str** | Required order sender | 
**maker_asset_amount** | **str** | Amount of maker token in trade | 
**taker_asset_amount** | **str** | Amount of taker token in trade | 
**maker_fee** | **str** | Fee owed by maker | 
**taker_fee** | **str** | Fee owed by taker | 
**maker_asset_data** | **str** | Address of maker token | 
**taker_asset_data** | **str** | Address of taker token | 
**salt** | **str** | Secure salt | 
**exchange_address** | **str** | Address of 0x exchange contract | 
**expiration_time_seconds** | **str** | Unix timestamp when order expires | 
**signature** | **str** | Secure EC Signature | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


