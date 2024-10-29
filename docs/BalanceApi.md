# fugledata.BalanceApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance_delete**](BalanceApi.md#balance_delete) | **DELETE** /balance | 
[**balance_get**](BalanceApi.md#balance_get) | **GET** /balance | 
[**balance_patch**](BalanceApi.md#balance_patch) | **PATCH** /balance | 
[**balance_post**](BalanceApi.md#balance_post) | **POST** /balance | 


# **balance_delete**
> balance_delete(dt=dt, available=available, id=id, prefer=prefer)



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
    api_instance = fugledata.BalanceApi(api_client)
    dt = 'dt_example' # str |  (optional)
    available = 'available_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_instance.balance_delete(dt=dt, available=available, id=id, prefer=prefer)
    except Exception as e:
        print("Exception when calling BalanceApi->balance_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **available** | **str**|  | [optional] 
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

# **balance_get**
> List[Balance] balance_get(dt=dt, available=available, id=id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example


```python
import fugledata
from fugledata.models.balance import Balance
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
    api_instance = fugledata.BalanceApi(api_client)
    dt = 'dt_example' # str |  (optional)
    available = 'available_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    select = 'select_example' # str | Filtering Columns (optional)
    order = 'order_example' # str | Ordering (optional)
    range = 'range_example' # str | Limiting and Pagination (optional)
    range_unit = 'items' # str | Limiting and Pagination (optional) (default to 'items')
    offset = 'offset_example' # str | Limiting and Pagination (optional)
    limit = 'limit_example' # str | Limiting and Pagination (optional)
    prefer = 'prefer_example' # str | Preference (optional)

    try:
        api_response = api_instance.balance_get(dt=dt, available=available, id=id, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
        print("The response of BalanceApi->balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalanceApi->balance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **available** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to &#39;items&#39;]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**List[Balance]**](Balance.md)

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

# **balance_patch**
> balance_patch(dt=dt, available=available, id=id, prefer=prefer, balance=balance)



### Example


```python
import fugledata
from fugledata.models.balance import Balance
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
    api_instance = fugledata.BalanceApi(api_client)
    dt = 'dt_example' # str |  (optional)
    available = 'available_example' # str |  (optional)
    id = 'id_example' # str |  (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    balance = fugledata.Balance() # Balance | balance (optional)

    try:
        api_instance.balance_patch(dt=dt, available=available, id=id, prefer=prefer, balance=balance)
    except Exception as e:
        print("Exception when calling BalanceApi->balance_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dt** | **str**|  | [optional] 
 **available** | **str**|  | [optional] 
 **id** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **balance** | [**Balance**](Balance.md)| balance | [optional] 

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

# **balance_post**
> balance_post(select=select, prefer=prefer, balance=balance)



### Example


```python
import fugledata
from fugledata.models.balance import Balance
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
    api_instance = fugledata.BalanceApi(api_client)
    select = 'select_example' # str | Filtering Columns (optional)
    prefer = 'prefer_example' # str | Preference (optional)
    balance = fugledata.Balance() # Balance | balance (optional)

    try:
        api_instance.balance_post(select=select, prefer=prefer, balance=balance)
    except Exception as e:
        print("Exception when calling BalanceApi->balance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | **str**| Filtering Columns | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **balance** | [**Balance**](Balance.md)| balance | [optional] 

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

