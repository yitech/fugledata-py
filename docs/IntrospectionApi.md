# fugledata.IntrospectionApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](IntrospectionApi.md#root_get) | **GET** / | OpenAPI description (this document)


# **root_get**
> root_get()

OpenAPI description (this document)

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
    api_instance = fugledata.IntrospectionApi(api_client)

    try:
        # OpenAPI description (this document)
        api_instance.root_get()
    except Exception as e:
        print("Exception when calling IntrospectionApi->root_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

