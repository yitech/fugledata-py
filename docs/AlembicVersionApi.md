# fugledata.AlembicVersionApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alembic_version_delete**](AlembicVersionApi.md#alembic_version_delete) | **DELETE** /alembic_version | 
[**alembic_version_get**](AlembicVersionApi.md#alembic_version_get) | **GET** /alembic_version | 
[**alembic_version_patch**](AlembicVersionApi.md#alembic_version_patch) | **PATCH** /alembic_version | 
[**alembic_version_post**](AlembicVersionApi.md#alembic_version_post) | **POST** /alembic_version | 


# **alembic_version_delete**
> alembic_version_delete(version_num=version_num, prefer=prefer)



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
    api_instance = fugledata.AlembicVersionApi(api_client)
    version_num = 'version_num_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_instance.alembic_version_delete(version_num=version_num, prefer=prefer)
    except Exception as e:
        print("Exception when calling AlembicVersionApi->alembic_version_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **str**|  | [optional] 
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

# **alembic_version_get**
> List[AlembicVersion] alembic_version_get(version_num=version_num, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example


```python
import fugledata
from fugledata.models.alembic_version import AlembicVersion
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
    api_instance = fugledata.AlembicVersionApi(api_client)
    version_num = 'version_num_example' # str |  (optional)
    select = 'select_example' # str | Filtering Columns (optional)
    order = 'order_example' # str | Ordering (optional)
    range = 'range_example' # str | Limiting and Pagination (optional)
    range_unit = 'items' # str | Limiting and Pagination (optional) (default to 'items')
    offset = 'offset_example' # str | Limiting and Pagination (optional)
    limit = 'limit_example' # str | Limiting and Pagination (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_response = api_instance.alembic_version_get(version_num=version_num, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
        print("The response of AlembicVersionApi->alembic_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlembicVersionApi->alembic_version_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to &#39;items&#39;]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**List[AlembicVersion]**](AlembicVersion.md)

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

# **alembic_version_patch**
> alembic_version_patch(version_num=version_num, prefer=prefer, alembic_version=alembic_version)



### Example


```python
import fugledata
from fugledata.models.alembic_version import AlembicVersion
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
    api_instance = fugledata.AlembicVersionApi(api_client)
    version_num = 'version_num_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    alembic_version = fugledata.AlembicVersion() # AlembicVersion | alembic_version (optional)

    try:
        api_instance.alembic_version_patch(version_num=version_num, prefer=prefer, alembic_version=alembic_version)
    except Exception as e:
        print("Exception when calling AlembicVersionApi->alembic_version_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_num** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **alembic_version** | [**AlembicVersion**](AlembicVersion.md)| alembic_version | [optional] 

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

# **alembic_version_post**
> alembic_version_post(select=select, prefer=prefer, alembic_version=alembic_version)



### Example


```python
import fugledata
from fugledata.models.alembic_version import AlembicVersion
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
    api_instance = fugledata.AlembicVersionApi(api_client)
    select = 'select_example' # str | Filtering Columns (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    alembic_version = fugledata.AlembicVersion() # AlembicVersion | alembic_version (optional)

    try:
        api_instance.alembic_version_post(select=select, prefer=prefer, alembic_version=alembic_version)
    except Exception as e:
        print("Exception when calling AlembicVersionApi->alembic_version_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Filtering Columns | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **alembic_version** | [**AlembicVersion**](AlembicVersion.md)| alembic_version | [optional] 

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

