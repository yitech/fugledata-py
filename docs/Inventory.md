# Inventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **date** |  | 
**symbol** | **str** |  | 
**num_share** | **int** |  | 
**id** | **int** | Note: This is a Primary Key.&lt;pk/&gt; | 

## Example

```python
from fugledata.models.inventory import Inventory

# TODO update the JSON string below
json = "{}"
# create an instance of Inventory from a JSON string
inventory_instance = Inventory.from_json(json)
# print the JSON string representation of the object
print(Inventory.to_json())

# convert the object into a dict
inventory_dict = inventory_instance.to_dict()
# create an instance of Inventory from a dict
inventory_from_dict = Inventory.from_dict(inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


