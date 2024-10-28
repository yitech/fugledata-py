# MarketMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Note: This is a Primary Key.&lt;pk/&gt; | 
**symbol** | **str** |  | 
**category** | **str** |  | [optional] 

## Example

```python
from fugledata.models.market_metadata import MarketMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MarketMetadata from a JSON string
market_metadata_instance = MarketMetadata.from_json(json)
# print the JSON string representation of the object
print(MarketMetadata.to_json())

# convert the object into a dict
market_metadata_dict = market_metadata_instance.to_dict()
# create an instance of MarketMetadata from a dict
market_metadata_from_dict = MarketMetadata.from_dict(market_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


