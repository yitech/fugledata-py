# fugledata.KlineApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kline_delete**](KlineApi.md#kline_delete) | **DELETE** /kline | 
[**kline_get**](KlineApi.md#kline_get) | **GET** /kline | 
[**kline_patch**](KlineApi.md#kline_patch) | **PATCH** /kline | 
[**kline_post**](KlineApi.md#kline_post) | **POST** /kline | 


# **kline_delete**
> kline_delete(id=id, symbol=symbol, dt=dt, open=open, high=high, low=low, close=close, volume=volume, prefer=prefer)



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
    api_instance = fugledata.KlineApi(api_client)
    id = 'id_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    dt = 'dt_example' # str |  (optional)
    open = 'open_example' # str |  (optional)
    high = 'high_example' # str |  (optional)
    low = 'low_example' # str |  (optional)
    close = 'close_example' # str |  (optional)
    volume = 'volume_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_instance.kline_delete(id=id, symbol=symbol, dt=dt, open=open, high=high, low=low, close=close, volume=volume, prefer=prefer)
    except Exception as e:
        print("Exception when calling KlineApi->kline_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **dt** | **str**|  | [optional] 
 **open** | **str**|  | [optional] 
 **high** | **str**|  | [optional] 
 **low** | **str**|  | [optional] 
 **close** | **str**|  | [optional] 
 **volume** | **str**|  | [optional] 
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

# **kline_get**
> List[Kline] kline_get(id=id, symbol=symbol, dt=dt, open=open, high=high, low=low, close=close, volume=volume, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example


```python
import fugledata
from fugledata.models.kline import Kline
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
    api_instance = fugledata.KlineApi(api_client)
    id = 'id_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    dt = 'dt_example' # str |  (optional)
    open = 'open_example' # str |  (optional)
    high = 'high_example' # str |  (optional)
    low = 'low_example' # str |  (optional)
    close = 'close_example' # str |  (optional)
    volume = 'volume_example' # str |  (optional)
    select = 'select_example' # str | Filtering Columns (optional)
    order = 'order_example' # str | Ordering (optional)
    range = 'range_example' # str | Limiting and Pagination (optional)
    range_unit = 'items' # str | Limiting and Pagination (optional) (default to 'items')
    offset = 'offset_example' # str | Limiting and Pagination (optional)
    limit = 'limit_example' # str | Limiting and Pagination (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_response = api_instance.kline_get(id=id, symbol=symbol, dt=dt, open=open, high=high, low=low, close=close, volume=volume, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
        print("The response of KlineApi->kline_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KlineApi->kline_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **dt** | **str**|  | [optional] 
 **open** | **str**|  | [optional] 
 **high** | **str**|  | [optional] 
 **low** | **str**|  | [optional] 
 **close** | **str**|  | [optional] 
 **volume** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to &#39;items&#39;]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**List[Kline]**](Kline.md)

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

# **kline_patch**
> kline_patch(id=id, symbol=symbol, dt=dt, open=open, high=high, low=low, close=close, volume=volume, prefer=prefer, kline=kline)



### Example


```python
import fugledata
from fugledata.models.kline import Kline
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
    api_instance = fugledata.KlineApi(api_client)
    id = 'id_example' # str |  (optional)
    symbol = 'symbol_example' # str |  (optional)
    dt = 'dt_example' # str |  (optional)
    open = 'open_example' # str |  (optional)
    high = 'high_example' # str |  (optional)
    low = 'low_example' # str |  (optional)
    close = 'close_example' # str |  (optional)
    volume = 'volume_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    kline = fugledata.Kline() # Kline | kline (optional)

    try:
        api_instance.kline_patch(id=id, symbol=symbol, dt=dt, open=open, high=high, low=low, close=close, volume=volume, prefer=prefer, kline=kline)
    except Exception as e:
        print("Exception when calling KlineApi->kline_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **symbol** | **str**|  | [optional] 
 **dt** | **str**|  | [optional] 
 **open** | **str**|  | [optional] 
 **high** | **str**|  | [optional] 
 **low** | **str**|  | [optional] 
 **close** | **str**|  | [optional] 
 **volume** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **kline** | [**Kline**](Kline.md)| kline | [optional] 

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

# **kline_post**
> kline_post(select=select, prefer=prefer, kline=kline)



### Example


```python
import fugledata
from fugledata.models.kline import Kline
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
    api_instance = fugledata.KlineApi(api_client)
    select = 'select_example' # str | Filtering Columns (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    kline = fugledata.Kline() # Kline | kline (optional)

    try:
        api_instance.kline_post(select=select, prefer=prefer, kline=kline)
    except Exception as e:
        print("Exception when calling KlineApi->kline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Filtering Columns | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **kline** | [**Kline**](Kline.md)| kline | [optional] 

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

