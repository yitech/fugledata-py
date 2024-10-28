# Kline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Note: This is a Primary Key.&lt;pk/&gt; | 
**symbol** | **str** |  | 
**dt** | **date** |  | 
**open** | **float** |  | 
**high** | **float** |  | 
**low** | **float** |  | 
**close** | **float** |  | 
**volume** | **int** |  | 

## Example

```python
from fugledata.models.kline import Kline

# TODO update the JSON string below
json = "{}"
# create an instance of Kline from a JSON string
kline_instance = Kline.from_json(json)
# print the JSON string representation of the object
print(Kline.to_json())

# convert the object into a dict
kline_dict = kline_instance.to_dict()
# create an instance of Kline from a dict
kline_from_dict = Kline.from_dict(kline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


