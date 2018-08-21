# TradeHistoryLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Unique Identifier | 
**date_created** | **datetime** | Date of creation | 
**date_updated** | **datetime** | Date of updated | 
**order_hash** | **str** | Unique, generated hash representing 0x order | 
**tx_hash** | **str** | Transaction Hash | 
**maker_address** | **str** | Address of order maker | 
**taker_address** | **str** | Address of order taker | 
**fee_recipient_address** | **str** | Address of order feeRecipient | 
**maker_asset_address** | **str** | Address of maker token | 
**maker_token_symbol** | **str** | Symbol of maker token | 
**maker_token_name** | **str** | Name of maker token | 
**maker_token_decimals** | **float** | Decimals of maker token | 
**maker_token_usd_price** | **str** | Unit price of maker token in USD | 
**taker_asset_address** | **str** | Address of taker token | 
**taker_token_symbol** | **str** | Symbol of taker token | 
**taker_token_name** | **str** | Name of taker token | 
**taker_token_decimals** | **float** |  | 
**taker_token_usd_price** | **str** | Unit price of taker token in USD | 
**filled_maker_token_amount** | **str** | Base amount of maker token filled in trade | 
**filled_maker_token_unit_amount** | **str** | Unit amount of maker token filled in trade (adjusted for token decimals) | 
**filled_maker_token_amount_usd** | **str** | USD value of maker amount | 
**filled_taker_token_amount** | **str** | Base amount of taker token filled in trade | 
**filled_taker_token_unit_amount** | **str** | Unit amount of taker token filled in trade (adjusted for token decimals) | 
**filled_taker_token_amount_usd** | **str** | USD value of taker amount | 
**paid_maker_fee_amount** | **str** | Base amount of ZRX fees collected from maker | 
**paid_maker_fee_unit_amount** | **str** | Unit amount of ZRX fees collected from maker | 
**paid_maker_fee_usd** | **str** | USD value of maker fee | 
**paid_taker_fee_amount** | **str** | Base amount of ZRX fees collected from taker | 
**paid_taker_fee_unit_amount** | **str** | Unit amount of ZRX fees collected from taker | 
**paid_taker_fee_usd** | **str** | USD value of taker fee | 
**relayer** | **str** | Name of originating relayer (if known) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


