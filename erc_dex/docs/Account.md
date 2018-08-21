# Account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Unique Identifier | 
**date_created** | **datetime** | Date of creation | 
**date_updated** | **datetime** | Date of updated | 
**name** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 
**address** | **str** |  | 
**account_type** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**referrer_account_id** | **float** |  | [optional] 
**referral_wallet_id** | **float** |  | [optional] 
**is_confirmed** | **bool** |  | 
**referrer_account** | [**Account**](Account.md) |  | 
**referral_wallet** | [**AuthorizedWallet**](AuthorizedWallet.md) |  | [optional] 
**users** | [**list[User]**](User.md) |  | 
**rebate_contracts** | [**list[RebateContract]**](RebateContract.md) |  | 
**api_keys** | [**list[ApiKey]**](ApiKey.md) |  | 
**authorized_wallets** | [**list[AuthorizedWallet]**](AuthorizedWallet.md) |  | 
**orders** | [**list[Order]**](Order.md) |  | 
**transaction_claims** | [**list[TransactionClaim]**](TransactionClaim.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


