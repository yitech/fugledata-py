# fugledata.InventoryApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_delete**](InventoryApi.md#inventory_delete) | **DELETE** /inventory | 
[**inventory_get**](InventoryApi.md#inventory_get) | **GET** /inventory | 
[**inventory_patch**](InventoryApi.md#inventory_patch) | **PATCH** /inventory | 
[**inventory_post**](InventoryApi.md#inventory_post) | **POST** /inventory | 


# **inventory_delete**
> inventory_delete(dt=dt, symbol=symbol, num_share=num_share, id=id, prefer=prefer)



### Example


```python
import fugledata
from fugledata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = fugledata.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with fugledata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugledata.InventoryApi(api_client)
    dt = 'dt_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    num_share = 'num_share_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_instance.inventory_delete(dt=dt, symbol=symbol, num_share=num_share, id=id, prefer=prefer)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **num_share** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get**
> List[Inventory] inventory_get(dt=dt, symbol=symbol, num_share=num_share, id=id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example


```python
import fugledata
from fugledata.models.inventory import Inventory
from fugledata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = fugledata.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with fugledata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugledata.InventoryApi(api_client)
    dt = 'dt_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    num_share = 'num_share_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    select = 'select_example' # str | Filtering Columns (optional)
    order = 'order_example' # str | Ordering (optional)
    range = 'range_example' # str | Limiting and Pagination (optional)
    range_unit = 'items' # str | Limiting and Pagination (optional) (default to 'items')
    offset = 'offset_example' # str | Limiting and Pagination (optional)
    limit = 'limit_example' # str | Limiting and Pagination (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_response = api_instance.inventory_get(dt=dt, symbol=symbol, num_share=num_share, id=id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
        print("The response of InventoryApi->inventory_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **num_share** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to &#39;items&#39;]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**List[Inventory]**](Inventory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**206** | Partial Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_patch**
> inventory_patch(dt=dt, symbol=symbol, num_share=num_share, id=id, prefer=prefer, inventory=inventory)



### Example


```python
import fugledata
from fugledata.models.inventory import Inventory
from fugledata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = fugledata.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with fugledata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugledata.InventoryApi(api_client)
    dt = 'dt_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    num_share = 'num_share_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    inventory = fugledata.Inventory() # Inventory | inventory (optional)

    try:
        api_instance.inventory_patch(dt=dt, symbol=symbol, num_share=num_share, id=id, prefer=prefer, inventory=inventory)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **num_share** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **inventory** | [**Inventory**](Inventory.md)| inventory | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_post**
> inventory_post(select=select, prefer=prefer, inventory=inventory)



### Example


```python
import fugledata
from fugledata.models.inventory import Inventory
from fugledata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = fugledata.Configuration(
    host = "http://localhost:3000"
)


# Enter a context with an instance of the API client
with fugledata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fugledata.InventoryApi(api_client)
    select = 'select_example' # str | Filtering Columns (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    inventory = fugledata.Inventory() # Inventory | inventory (optional)

    try:
        api_instance.inventory_post(select=select, prefer=prefer, inventory=inventory)
    except Exception as e:
        print("Exception when calling InventoryApi->inventory_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Filtering Columns | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **inventory** | [**Inventory**](Inventory.md)| inventory | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

