# Settlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **date** |  | 
**next_day** | **int** |  | [optional] 
**after_next** | **int** |  | [optional] 
**id** | **int** | Note: This is a Primary Key.&lt;pk/&gt; | 

## Example

```python
from fugledata.models.settlement import Settlement

# TODO update the JSON string below
json = "{}"
# create an instance of Settlement from a JSON string
settlement_instance = Settlement.from_json(json)
# print the JSON string representation of the object
print(Settlement.to_json())

# convert the object into a dict
settlement_dict = settlement_instance.to_dict()
# create an instance of Settlement from a dict
settlement_from_dict = Settlement.from_dict(settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


