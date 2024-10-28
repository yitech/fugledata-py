# AlembicVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_num** | **str** | Note: This is a Primary Key.&lt;pk/&gt; | 

## Example

```python
from fugledata.models.alembic_version import AlembicVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AlembicVersion from a JSON string
alembic_version_instance = AlembicVersion.from_json(json)
# print the JSON string representation of the object
print(AlembicVersion.to_json())

# convert the object into a dict
alembic_version_dict = alembic_version_instance.to_dict()
# create an instance of AlembicVersion from a dict
alembic_version_from_dict = AlembicVersion.from_dict(alembic_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


