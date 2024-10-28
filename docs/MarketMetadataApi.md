# fugledata.MarketMetadataApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_metadata_delete**](MarketMetadataApi.md#market_metadata_delete) | **DELETE** /market_metadata | 
[**market_metadata_get**](MarketMetadataApi.md#market_metadata_get) | **GET** /market_metadata | 
[**market_metadata_patch**](MarketMetadataApi.md#market_metadata_patch) | **PATCH** /market_metadata | 
[**market_metadata_post**](MarketMetadataApi.md#market_metadata_post) | **POST** /market_metadata | 


# **market_metadata_delete**
> market_metadata_delete(id=id, symbol=symbol, category=category, prefer=prefer)



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
    api_instance = fugledata.MarketMetadataApi(api_client)
    id = 'id_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    category = 'category_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_instance.market_metadata_delete(id=id, symbol=symbol, category=category, prefer=prefer)
    except Exception as e:
        print("Exception when calling MarketMetadataApi->market_metadata_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
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

# **market_metadata_get**
> List[MarketMetadata] market_metadata_get(id=id, symbol=symbol, category=category, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example


```python
import fugledata
from fugledata.models.market_metadata import MarketMetadata
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
    api_instance = fugledata.MarketMetadataApi(api_client)
    id = 'id_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    category = 'category_example' # str |  (optional)
    select = 'select_example' # str | Filtering Columns (optional)
    order = 'order_example' # str | Ordering (optional)
    range = 'range_example' # str | Limiting and Pagination (optional)
    range_unit = 'items' # str | Limiting and Pagination (optional) (default to 'items')
    offset = 'offset_example' # str | Limiting and Pagination (optional)
    limit = 'limit_example' # str | Limiting and Pagination (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_response = api_instance.market_metadata_get(id=id, symbol=symbol, category=category, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
        print("The response of MarketMetadataApi->market_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketMetadataApi->market_metadata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to &#39;items&#39;]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**List[MarketMetadata]**](MarketMetadata.md)

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

# **market_metadata_patch**
> market_metadata_patch(id=id, symbol=symbol, category=category, prefer=prefer, market_metadata=market_metadata)



### Example


```python
import fugledata
from fugledata.models.market_metadata import MarketMetadata
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
    api_instance = fugledata.MarketMetadataApi(api_client)
    id = 'id_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    category = 'category_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    market_metadata = fugledata.MarketMetadata() # MarketMetadata | market_metadata (optional)

    try:
        api_instance.market_metadata_patch(id=id, symbol=symbol, category=category, prefer=prefer, market_metadata=market_metadata)
    except Exception as e:
        print("Exception when calling MarketMetadataApi->market_metadata_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **market_metadata** | [**MarketMetadata**](MarketMetadata.md)| market_metadata | [optional] 

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

# **market_metadata_post**
> market_metadata_post(select=select, prefer=prefer, market_metadata=market_metadata)



### Example


```python
import fugledata
from fugledata.models.market_metadata import MarketMetadata
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
    api_instance = fugledata.MarketMetadataApi(api_client)
    select = 'select_example' # str | Filtering Columns (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    market_metadata = fugledata.MarketMetadata() # MarketMetadata | market_metadata (optional)

    try:
        api_instance.market_metadata_post(select=select, prefer=prefer, market_metadata=market_metadata)
    except Exception as e:
        print("Exception when calling MarketMetadataApi->market_metadata_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Filtering Columns | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **market_metadata** | [**MarketMetadata**](MarketMetadata.md)| market_metadata | [optional] 

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

