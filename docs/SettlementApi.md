# fugledata.SettlementApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settlement_delete**](SettlementApi.md#settlement_delete) | **DELETE** /settlement | 
[**settlement_get**](SettlementApi.md#settlement_get) | **GET** /settlement | 
[**settlement_patch**](SettlementApi.md#settlement_patch) | **PATCH** /settlement | 
[**settlement_post**](SettlementApi.md#settlement_post) | **POST** /settlement | 


# **settlement_delete**
> settlement_delete(dt=dt, next_day=next_day, after_next=after_next, id=id, prefer=prefer)



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
    api_instance = fugledata.SettlementApi(api_client)
    dt = 'dt_example' # str |  (optional)
    next_day = 'next_day_example' # str |  (optional)
    after_next = 'after_next_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_instance.settlement_delete(dt=dt, next_day=next_day, after_next=after_next, id=id, prefer=prefer)
    except Exception as e:
        print("Exception when calling SettlementApi->settlement_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **next_day** | **str**|  | [optional] 
 **after_next** | **str**|  | [optional] 
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

# **settlement_get**
> List[Settlement] settlement_get(dt=dt, next_day=next_day, after_next=after_next, id=id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example


```python
import fugledata
from fugledata.models.settlement import Settlement
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
    api_instance = fugledata.SettlementApi(api_client)
    dt = 'dt_example' # str |  (optional)
    next_day = 'next_day_example' # str |  (optional)
    after_next = 'after_next_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    select = 'select_example' # str | Filtering Columns (optional)
    order = 'order_example' # str | Ordering (optional)
    range = 'range_example' # str | Limiting and Pagination (optional)
    range_unit = 'items' # str | Limiting and Pagination (optional) (default to 'items')
    offset = 'offset_example' # str | Limiting and Pagination (optional)
    limit = 'limit_example' # str | Limiting and Pagination (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_response = api_instance.settlement_get(dt=dt, next_day=next_day, after_next=after_next, id=id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
        print("The response of SettlementApi->settlement_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettlementApi->settlement_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **next_day** | **str**|  | [optional] 
 **after_next** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to &#39;items&#39;]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**List[Settlement]**](Settlement.md)

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

# **settlement_patch**
> settlement_patch(dt=dt, next_day=next_day, after_next=after_next, id=id, prefer=prefer, settlement=settlement)



### Example


```python
import fugledata
from fugledata.models.settlement import Settlement
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
    api_instance = fugledata.SettlementApi(api_client)
    dt = 'dt_example' # str |  (optional)
    next_day = 'next_day_example' # str |  (optional)
    after_next = 'after_next_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    settlement = fugledata.Settlement() # Settlement | settlement (optional)

    try:
        api_instance.settlement_patch(dt=dt, next_day=next_day, after_next=after_next, id=id, prefer=prefer, settlement=settlement)
    except Exception as e:
        print("Exception when calling SettlementApi->settlement_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **next_day** | **str**|  | [optional] 
 **after_next** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **settlement** | [**Settlement**](Settlement.md)| settlement | [optional] 

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

# **settlement_post**
> settlement_post(select=select, prefer=prefer, settlement=settlement)



### Example


```python
import fugledata
from fugledata.models.settlement import Settlement
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
    api_instance = fugledata.SettlementApi(api_client)
    select = 'select_example' # str | Filtering Columns (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    settlement = fugledata.Settlement() # Settlement | settlement (optional)

    try:
        api_instance.settlement_post(select=select, prefer=prefer, settlement=settlement)
    except Exception as e:
        print("Exception when calling SettlementApi->settlement_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Filtering Columns | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **settlement** | [**Settlement**](Settlement.md)| settlement | [optional] 

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

