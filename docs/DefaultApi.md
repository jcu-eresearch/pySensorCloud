# sensor_cloud.DefaultApi

All URIs are relative to *https://sensor-cloud.io/api/sensor/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregation_get**](DefaultApi.md#aggregation_get) | **GET** /aggregation | Calculate an aggregated view of observations.
[**collections_collectionid_shares_get**](DefaultApi.md#collections_collectionid_shares_get) | **GET** /collections/{collectionid}/shares | Get shares for a collection
[**collections_collectionid_shares_id_delete**](DefaultApi.md#collections_collectionid_shares_id_delete) | **DELETE** /collections/{collectionid}/shares/{id} | Delete a share from an existing collection.
[**collections_collectionid_shares_id_get**](DefaultApi.md#collections_collectionid_shares_id_get) | **GET** /collections/{collectionid}/shares/{id} | Get details about a share resource
[**collections_count_get**](DefaultApi.md#collections_count_get) | **GET** /collections/count | Get a count of collections.
[**collections_get**](DefaultApi.md#collections_get) | **GET** /collections | Get a list of collections.
[**collections_id_delete**](DefaultApi.md#collections_id_delete) | **DELETE** /collections/{id} | Delete an existing Collection.
[**collections_id_get**](DefaultApi.md#collections_id_get) | **GET** /collections/{id} | Get details about a collection.
[**collections_id_put**](DefaultApi.md#collections_id_put) | **PUT** /collections/{id} | Create or update a collection
[**collections_post**](DefaultApi.md#collections_post) | **POST** /collections | Create a new collection.
[**groups_get**](DefaultApi.md#groups_get) | **GET** /groups | Get a collection of groups.
[**groups_id_delete**](DefaultApi.md#groups_id_delete) | **DELETE** /groups/{id} | Delete an existing group.
[**groups_id_get**](DefaultApi.md#groups_id_get) | **GET** /groups/{id} | Get details about a group.
[**groups_id_put**](DefaultApi.md#groups_id_put) | **PUT** /groups/{id} | Create a new or update an existing group.
[**invitations_id_accept_post**](DefaultApi.md#invitations_id_accept_post) | **POST** /invitations/{id}/accept | Accepts an invitation
[**invitations_id_get**](DefaultApi.md#invitations_id_get) | **GET** /invitations/{id} | Get details about an invitation
[**invitations_post**](DefaultApi.md#invitations_post) | **POST** /invitations | Send a new invitation
[**locations_count_get**](DefaultApi.md#locations_count_get) | **GET** /locations/count | Get a count of locations.
[**locations_get**](DefaultApi.md#locations_get) | **GET** /locations | Get a collection of locations.
[**locations_id_delete**](DefaultApi.md#locations_id_delete) | **DELETE** /locations/{id} | Delete an existing location.
[**locations_id_get**](DefaultApi.md#locations_id_get) | **GET** /locations/{id} | Get details about a location.
[**locations_id_put**](DefaultApi.md#locations_id_put) | **PUT** /locations/{id} | Create a new or update an existing Location
[**observations_delete**](DefaultApi.md#observations_delete) | **DELETE** /observations | Delete observations from a stream
[**observations_get**](DefaultApi.md#observations_get) | **GET** /observations | Get a collection of observations.
[**observations_post**](DefaultApi.md#observations_post) | **POST** /observations | Upload observations for a stream
[**organisations_get**](DefaultApi.md#organisations_get) | **GET** /organisations | Get a collection of organisations.
[**organisations_organisationid_get**](DefaultApi.md#organisations_organisationid_get) | **GET** /organisations/{organisationid} | Get details about an organisation.
[**organisations_organisationid_put**](DefaultApi.md#organisations_organisationid_put) | **PUT** /organisations/{organisationid} | Update or create a new organisation.
[**platforms_get**](DefaultApi.md#platforms_get) | **GET** /platforms | Get a collection of platforms.
[**platforms_id_delete**](DefaultApi.md#platforms_id_delete) | **DELETE** /platforms/{id} | Delete an existing platform.
[**platforms_id_get**](DefaultApi.md#platforms_id_get) | **GET** /platforms/{id} | Get details about a platform.
[**platforms_id_put**](DefaultApi.md#platforms_id_put) | **PUT** /platforms/{id} | Create a new or update an existing platform.
[**procedures_get**](DefaultApi.md#procedures_get) | **GET** /procedures | Get a collection of sensing procedures.
[**procedures_id_delete**](DefaultApi.md#procedures_id_delete) | **DELETE** /procedures/{id} | Delete an existing sensing procedure.
[**procedures_id_get**](DefaultApi.md#procedures_id_get) | **GET** /procedures/{id} | Get details about a sensing procedures.
[**procedures_id_put**](DefaultApi.md#procedures_id_put) | **PUT** /procedures/{id} | Create a new or update an existing sensing procedure.
[**roles_get**](DefaultApi.md#roles_get) | **GET** /roles | Get a collection of roles.
[**roles_roleid_delete**](DefaultApi.md#roles_roleid_delete) | **DELETE** /roles/{roleid} | Delete an existing role.
[**roles_roleid_get**](DefaultApi.md#roles_roleid_get) | **GET** /roles/{roleid} | Get details about a specific role.
[**roles_roleid_put**](DefaultApi.md#roles_roleid_put) | **PUT** /roles/{roleid} | Update or create a role.
[**root_get**](DefaultApi.md#root_get) | **GET** / | Sensor Data API Root
[**shares_count_get**](DefaultApi.md#shares_count_get) | **GET** /shares/count | Get a count of current shares.
[**shares_get**](DefaultApi.md#shares_get) | **GET** /shares | Get a list of current shares.
[**shares_id_delete**](DefaultApi.md#shares_id_delete) | **DELETE** /shares/{id} | Delete an existing Share.
[**shares_id_get**](DefaultApi.md#shares_id_get) | **GET** /shares/{id} | Get details about a share.
[**shares_id_put**](DefaultApi.md#shares_id_put) | **PUT** /shares/{id} | Update an existing Share.
[**shares_post**](DefaultApi.md#shares_post) | **POST** /shares | Create a new share.
[**streams_count_get**](DefaultApi.md#streams_count_get) | **GET** /streams/count | Count a collection of streams.
[**streams_get**](DefaultApi.md#streams_get) | **GET** /streams | Get a collection of streams.
[**streams_id_delete**](DefaultApi.md#streams_id_delete) | **DELETE** /streams/{id} | Delete an existing stream.
[**streams_id_get**](DefaultApi.md#streams_id_get) | **GET** /streams/{id} | Get details about a stream.
[**streams_id_put**](DefaultApi.md#streams_id_put) | **PUT** /streams/{id} | Create a new or update an existing Stream.
[**users_get**](DefaultApi.md#users_get) | **GET** /users | Get a collection of users.
[**users_userid_get**](DefaultApi.md#users_userid_get) | **GET** /users/{userid} | Get details about a user.
[**users_userid_put**](DefaultApi.md#users_userid_put) | **PUT** /users/{userid} | Update or create a user.
[**vocabulary_get**](DefaultApi.md#vocabulary_get) | **GET** /vocabulary | Search for vocabulary terms.
[**vocabulary_proxy_get**](DefaultApi.md#vocabulary_proxy_get) | **GET** /vocabularyProxy | Resolve a specific vocabulary term


# **aggregation_get**
> aggregation_get(streamid, start=start, end=end, si=si, ei=ei, limit=limit, aggperiod=aggperiod, count=count)

Calculate an aggregated view of observations.

Calculate an aggregated view of observations. The aggregation is calculated on demand.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
streamid = 'streamid_example' # str | Stream identifier
start = 'start_example' # str | Start date (url encoded iso8601 format) (optional)
end = 'end_example' # str | End date (url encoded iso8601 format) (optional)
si = true # bool | Is the start parameter treated as an inclusive boundary (optional)
ei = true # bool | Is the end parameter treated as an inclusive boundary (optional)
limit = 3.4 # float | Limit the number of results. The limit is 1000 by default. (optional)
aggperiod = 3.4 # float | The number of milliseconds in each aggregation interval. (optional)
count = 'count_example' # str | Include this parameter to return a count of the observations in a stream. (Note, a value is not required for this parameter.) (optional)

try: 
    # Calculate an aggregated view of observations.
    api_instance.aggregation_get(streamid, start=start, end=end, si=si, ei=ei, limit=limit, aggperiod=aggperiod, count=count)
except ApiException as e:
    print("Exception when calling DefaultApi->aggregation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streamid** | **str**| Stream identifier | 
 **start** | **str**| Start date (url encoded iso8601 format) | [optional] 
 **end** | **str**| End date (url encoded iso8601 format) | [optional] 
 **si** | **bool**| Is the start parameter treated as an inclusive boundary | [optional] 
 **ei** | **bool**| Is the end parameter treated as an inclusive boundary | [optional] 
 **limit** | **float**| Limit the number of results. The limit is 1000 by default. | [optional] 
 **aggperiod** | **float**| The number of milliseconds in each aggregation interval. | [optional] 
 **count** | **str**| Include this parameter to return a count of the observations in a stream. (Note, a value is not required for this parameter.) | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_shares_get**
> collections_collectionid_shares_get(collectionid, id=id, limit=limit, skip=skip, expand=expand, recursive=recursive, organisationid=organisationid, groupid=groupid)

Get shares for a collection

Get shares for a collection

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
collectionid = 'collectionid_example' # str | 
id = 'id_example' # str | Only return shares with this id or partial match using wildcards (*, ?).  \\n* matches zero or more characters.\\n* ? matches exactly one character.\\n\\nFor example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
limit = 3.4 # float | Maximum number of shares to return (optional)
skip = 3.4 # float | Skip this many results (optional)
expand = true # bool | Return full details of matching shares (optional)
recursive = true # bool | Return full details of embedded resources (optional)
organisationid = 'organisationid_example' # str | Filter response by this organisation id (optional)
groupid = 'groupid_example' # str | Filter response by a comma separated list of group ids (optional)

try: 
    # Get shares for a collection
    api_instance.collections_collectionid_shares_get(collectionid, id=id, limit=limit, skip=skip, expand=expand, recursive=recursive, organisationid=organisationid, groupid=groupid)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_collectionid_shares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**|  | 
 **id** | **str**| Only return shares with this id or partial match using wildcards (*, ?).  \\n* matches zero or more characters.\\n* ? matches exactly one character.\\n\\nFor example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **limit** | **float**| Maximum number of shares to return | [optional] 
 **skip** | **float**| Skip this many results | [optional] 
 **expand** | **bool**| Return full details of matching shares | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **organisationid** | **str**| Filter response by this organisation id | [optional] 
 **groupid** | **str**| Filter response by a comma separated list of group ids | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_shares_id_delete**
> collections_collectionid_shares_id_delete(collectionid, id)

Delete a share from an existing collection.

Delete a share from an existing collection. The client must have an appropriate delete collection permission

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
collectionid = 'collectionid_example' # str | 
id = 'id_example' # str | The unique identifier for the share to be deleted from the collection

try: 
    # Delete a share from an existing collection.
    api_instance.collections_collectionid_shares_id_delete(collectionid, id)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_collectionid_shares_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**|  | 
 **id** | **str**| The unique identifier for the share to be deleted from the collection | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_shares_id_get**
> collections_collectionid_shares_id_get(collectionid, id, recursive=recursive)

Get details about a share resource

Get details about a specific share resource

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
collectionid = 'collectionid_example' # str | 
id = 'id_example' # str | The unique identifier for the share to be deleted from the collection
recursive = false # bool | Return full details of embedded resources (optional) (default to false)

try: 
    # Get details about a share resource
    api_instance.collections_collectionid_shares_id_get(collectionid, id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_collectionid_shares_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**|  | 
 **id** | **str**| The unique identifier for the share to be deleted from the collection | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_count_get**
> CollectionCollection collections_count_get(limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, streamids=streamids)

Get a count of collections.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
limit = 3.4 # float | Maximum number of streams to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
expand = true # bool | Return full details of platforms (optional)
recursive = true # bool | Return full details of embedded resources (optional)
groupids = 'groupids_example' # str | filter response by a comma separated list of group ids (optional)
streamids = 'streamids_example' # str | filter response by a comma separated list of stream ids (optional)

try: 
    # Get a count of collections.
    api_response = api_instance.collections_count_get(limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, streamids=streamids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Maximum number of streams to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **expand** | **bool**| Return full details of platforms | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **groupids** | **str**| filter response by a comma separated list of group ids | [optional] 
 **streamids** | **str**| filter response by a comma separated list of stream ids | [optional] 

### Return type

[**CollectionCollection**](CollectionCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get**
> CollectionCollection collections_get(limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, streamids=streamids)

Get a list of collections.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
limit = 3.4 # float | Maximum number of streams to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
expand = true # bool | Return full details of platforms (optional)
recursive = true # bool | Return full details of embedded resources (optional)
groupids = 'groupids_example' # str | filter response by a comma separated list of group ids (optional)
streamids = 'streamids_example' # str | filter response by a comma separated list of stream ids (optional)

try: 
    # Get a list of collections.
    api_response = api_instance.collections_get(limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, streamids=streamids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Maximum number of streams to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **expand** | **bool**| Return full details of platforms | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **groupids** | **str**| filter response by a comma separated list of group ids | [optional] 
 **streamids** | **str**| filter response by a comma separated list of stream ids | [optional] 

### Return type

[**CollectionCollection**](CollectionCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_id_delete**
> collections_id_delete(id)

Delete an existing Collection.

Delete an existing Collection. The client must have an appropriate delete Collection permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 

try: 
    # Delete an existing Collection.
    api_instance.collections_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_id_get**
> collections_id_get(id, recursive=recursive)

Get details about a collection.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Collection id
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a collection.
    api_instance.collections_id_get(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection id | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_id_put**
> collections_id_put(id, body=body, recursive=recursive)

Create or update a collection

Create or update a collection

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | The unique identifier for the target collection to create or update
body = sensor_cloud.CollectionPut() # CollectionPut |  (optional)
recursive = false # bool | Return full details of the created or updated collection (optional) (default to false)

try: 
    # Create or update a collection
    api_instance.collections_id_put(id, body=body, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the target collection to create or update | 
 **body** | [**CollectionPut**](CollectionPut.md)|  | [optional] 
 **recursive** | **bool**| Return full details of the created or updated collection | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_post**
> collections_post(body)

Create a new collection.

Create a new collection. Do not provide the id property in the body. The server will generate a UUID.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
body = sensor_cloud.CollectionPost() # CollectionPost | 

try: 
    # Create a new collection.
    api_instance.collections_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->collections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionPost**](CollectionPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> GroupCollection groups_get(id=id, organisationid=organisationid, groupids=groupids, limit=limit, skip=skip, expand=expand, recursive=recursive)

Get a collection of groups.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Only return groups with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
groupids = 'groupids_example' # str | filter response by a comma separated list of group ids (optional)
limit = 3.4 # float | Maximum number of streams to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
expand = true # bool | Return full details of groups (optional)
recursive = true # bool | Return full details of groups and linked objects (optional)

try: 
    # Get a collection of groups.
    api_response = api_instance.groups_get(id=id, organisationid=organisationid, groupids=groupids, limit=limit, skip=skip, expand=expand, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Only return groups with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **groupids** | **str**| filter response by a comma separated list of group ids | [optional] 
 **limit** | **float**| Maximum number of streams to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **expand** | **bool**| Return full details of groups | [optional] 
 **recursive** | **bool**| Return full details of groups and linked objects | [optional] 

### Return type

[**GroupCollection**](GroupCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_delete**
> groups_id_delete(id, cascade=cascade)

Delete an existing group.

Delete an existing Group. The client must have an appropriate delete Group permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
cascade = true # bool | Remove group even when not empty. (optional)

try: 
    # Delete an existing group.
    api_instance.groups_id_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cascade** | **bool**| Remove group even when not empty. | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_get**
> groups_id_get(id, recursive=recursive)

Get details about a group.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Group id
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a group.
    api_instance.groups_id_get(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Group id | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_put**
> groups_id_put(id, body)

Create a new or update an existing group.

Create a new group. If a group with the posted 'id' already exists then it will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
body = sensor_cloud.GroupPost() # GroupPost | 

try: 
    # Create a new or update an existing group.
    api_instance.groups_id_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GroupPost**](GroupPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitations_id_accept_post**
> Invitation invitations_id_accept_post(id)

Accepts an invitation

Accepts an invitation.  Only the invited user can accept invitations.  Invitations can only be accepted once.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | The unique identifier for the target invitation

try: 
    # Accepts an invitation
    api_response = api_instance.invitations_id_accept_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->invitations_id_accept_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the target invitation | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitations_id_get**
> Invitation invitations_id_get(id, recursive=recursive)

Get details about an invitation

Get details about an invitation. Only users who sent the invitation are permitted to read the invitation.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | The unique identifier for the target invitation
recursive = false # bool | Return full details of embedded resources (optional) (default to false)

try: 
    # Get details about an invitation
    api_response = api_instance.invitations_id_get(id, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->invitations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the target invitation | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] [default to false]

### Return type

[**Invitation**](Invitation.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitations_post**
> Invitation invitations_post(body=body)

Send a new invitation

Send a new invitation.  Users must have the AssignRolePermission to be able to send invitations within their organisation and/or group.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
body = sensor_cloud.InvitationPost() # InvitationPost | Information about the invitation to be sent. (optional)

try: 
    # Send a new invitation
    api_response = api_instance.invitations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->invitations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvitationPost**](InvitationPost.md)| Information about the invitation to be sent. | [optional] 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_count_get**
> LocationCollection locations_count_get(id=id, description=description, limit=limit, skip=skip, organisationid=organisationid, groupids=groupids, expand=expand, near=near, radius=radius)

Get a count of locations.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Only return locations with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
description = 'description_example' # str | Only return locations with this description or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
limit = 3.4 # float | Limit the number of results. The limit is 1000 by default (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
groupids = 'groupids_example' # str | filter response by this group id (optional)
expand = true # bool | Return full details of platforms (optional)
near = 'near_example' # str | Return locations ordered based on how close they are to this WKT 'POINT'. For example 'near=POINT (lon lat)' where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id=25355 for WTK Specification and examples. (optional)
radius = 3.4 # float | Limit results to locations within this distance (in metres) of the 'near' location. (optional)

try: 
    # Get a count of locations.
    api_response = api_instance.locations_count_get(id=id, description=description, limit=limit, skip=skip, organisationid=organisationid, groupids=groupids, expand=expand, near=near, radius=radius)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->locations_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Only return locations with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **description** | **str**| Only return locations with this description or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **limit** | **float**| Limit the number of results. The limit is 1000 by default | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **groupids** | **str**| filter response by this group id | [optional] 
 **expand** | **bool**| Return full details of platforms | [optional] 
 **near** | **str**| Return locations ordered based on how close they are to this WKT &#39;POINT&#39;. For example &#39;near&#x3D;POINT (lon lat)&#39; where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id&#x3D;25355 for WTK Specification and examples. | [optional] 
 **radius** | **float**| Limit results to locations within this distance (in metres) of the &#39;near&#39; location. | [optional] 

### Return type

[**LocationCollection**](LocationCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_get**
> LocationCollection locations_get(id=id, description=description, limit=limit, skip=skip, organisationid=organisationid, groupids=groupids, expand=expand, near=near, radius=radius)

Get a collection of locations.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Only return locations with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
description = 'description_example' # str | Only return locations with this description or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
limit = 3.4 # float | Limit the number of results. The limit is 1000 by default (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
groupids = 'groupids_example' # str | filter response by this group id (optional)
expand = true # bool | Return full details of platforms (optional)
near = 'near_example' # str | Return locations ordered based on how close they are to this WKT 'POINT'. For example 'near=POINT (lon lat)' where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id=25355 for WTK Specification and examples. (optional)
radius = 3.4 # float | Limit results to locations within this distance (in metres) of the 'near' location. (optional)

try: 
    # Get a collection of locations.
    api_response = api_instance.locations_get(id=id, description=description, limit=limit, skip=skip, organisationid=organisationid, groupids=groupids, expand=expand, near=near, radius=radius)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->locations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Only return locations with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **description** | **str**| Only return locations with this description or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **limit** | **float**| Limit the number of results. The limit is 1000 by default | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **groupids** | **str**| filter response by this group id | [optional] 
 **expand** | **bool**| Return full details of platforms | [optional] 
 **near** | **str**| Return locations ordered based on how close they are to this WKT &#39;POINT&#39;. For example &#39;near&#x3D;POINT (lon lat)&#39; where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id&#x3D;25355 for WTK Specification and examples. | [optional] 
 **radius** | **float**| Limit results to locations within this distance (in metres) of the &#39;near&#39; location. | [optional] 

### Return type

[**LocationCollection**](LocationCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_id_delete**
> locations_id_delete(id, cascade=cascade)

Delete an existing location.

Delete an existing Location. The client must have an appropriate delete Location permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
cascade = true # bool | Remove Location even when is referenced by other objects (eg. Platform deployments or Streams). (optional)

try: 
    # Delete an existing location.
    api_instance.locations_id_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling DefaultApi->locations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cascade** | **bool**| Remove Location even when is referenced by other objects (eg. Platform deployments or Streams). | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_id_get**
> locations_id_get(id, recursive=recursive)

Get details about a location.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Location id
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a location.
    api_instance.locations_id_get(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->locations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location id | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_id_put**
> locations_id_put(id, body)

Create a new or update an existing Location

Create a new Location. If a Location with the posted 'id' already exists then it will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
body = sensor_cloud.LocationPost() # LocationPost | A `Location` describes a point with a known latitude and longitude (and, optionally, elevation above mean sea level).  The coordinates of the `Location` are specified using a [GeoJSON Point](http://geojson.org/geojson-spec.html#point) object, which by convention lists coordinates in the order longitude, latitude then elevation.  For example, the following snippet defines a `Location` located at 42.903 degrees South, 147.327 degrees East, and 25 metres above mean sea level:      {       \"id\": \"NewLocation\",       \"organisationid\": \"MyOrg\",       \"geoJson\": {         \"type\": \"Point\",         \"coordinates\": [147.327, -42.903, 25.0]       }     }  If elevation is unknown, pass only two values (the longitude and latitude) in the `coordinates` property.

try: 
    # Create a new or update an existing Location
    api_instance.locations_id_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->locations_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**LocationPost**](LocationPost.md)| A &#x60;Location&#x60; describes a point with a known latitude and longitude (and, optionally, elevation above mean sea level).  The coordinates of the &#x60;Location&#x60; are specified using a [GeoJSON Point](http://geojson.org/geojson-spec.html#point) object, which by convention lists coordinates in the order longitude, latitude then elevation.  For example, the following snippet defines a &#x60;Location&#x60; located at 42.903 degrees South, 147.327 degrees East, and 25 metres above mean sea level:      {       \&quot;id\&quot;: \&quot;NewLocation\&quot;,       \&quot;organisationid\&quot;: \&quot;MyOrg\&quot;,       \&quot;geoJson\&quot;: {         \&quot;type\&quot;: \&quot;Point\&quot;,         \&quot;coordinates\&quot;: [147.327, -42.903, 25.0]       }     }  If elevation is unknown, pass only two values (the longitude and latitude) in the &#x60;coordinates&#x60; property. | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_delete**
> observations_delete(streamid)

Delete observations from a stream

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
streamid = 'streamid_example' # str | 

try: 
    # Delete observations from a stream
    api_instance.observations_delete(streamid)
except ApiException as e:
    print("Exception when calling DefaultApi->observations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streamid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_get**
> observations_get(streamid, start=start, end=end, time=time, si=si, ei=ei, bounds=bounds, media=media, limit=limit, sort=sort)

Get a collection of observations.

Get a collection of observations

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
streamid = 'streamid_example' # str | Stream identifier or a comma separated list of stream identifiers
start = 'start_example' # str | Start date (url encoded iso8601 format) (optional)
end = 'end_example' # str | End date (url encoded iso8601 format) (optional)
time = 'time_example' # str | Timestamp of a specific result. (url encoded iso8601 format) (optional)
si = true # bool | Is the start parameter treated as an inclusive boundary (optional)
ei = true # bool | Is the end parameter treated as an inclusive boundary (optional)
bounds = 'bounds_example' # str | Boundary filter for a geolocation stream, or any stream located by a geolocation stream. The boundary is provided as a POLYGON in WTK format. (optional)
media = 'media_example' # str | Format of response. Valid formats are csv, json, geojson (for geolocationvalue streams) (optional)
limit = 3.4 # float | Limit the number of results. The limit is 1000 by default. (optional)
sort = 'sort_example' # str | Sort the results. By default results are returned in ascending order. (optional)

try: 
    # Get a collection of observations.
    api_instance.observations_get(streamid, start=start, end=end, time=time, si=si, ei=ei, bounds=bounds, media=media, limit=limit, sort=sort)
except ApiException as e:
    print("Exception when calling DefaultApi->observations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streamid** | **str**| Stream identifier or a comma separated list of stream identifiers | 
 **start** | **str**| Start date (url encoded iso8601 format) | [optional] 
 **end** | **str**| End date (url encoded iso8601 format) | [optional] 
 **time** | **str**| Timestamp of a specific result. (url encoded iso8601 format) | [optional] 
 **si** | **bool**| Is the start parameter treated as an inclusive boundary | [optional] 
 **ei** | **bool**| Is the end parameter treated as an inclusive boundary | [optional] 
 **bounds** | **str**| Boundary filter for a geolocation stream, or any stream located by a geolocation stream. The boundary is provided as a POLYGON in WTK format. | [optional] 
 **media** | **str**| Format of response. Valid formats are csv, json, geojson (for geolocationvalue streams) | [optional] 
 **limit** | **float**| Limit the number of results. The limit is 1000 by default. | [optional] 
 **sort** | **str**| Sort the results. By default results are returned in ascending order. | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observations_post**
> observations_post(streamid, body)

Upload observations for a stream

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
streamid = 'streamid_example' # str | 
body = sensor_cloud.ObservationsPost() # ObservationsPost | 

try: 
    # Upload observations for a stream
    api_instance.observations_post(streamid, body)
except ApiException as e:
    print("Exception when calling DefaultApi->observations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streamid** | **str**|  | 
 **body** | [**ObservationsPost**](ObservationsPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_get**
> OrganisationCollection organisations_get()

Get a collection of organisations.

This operations returns a list of all organisations.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()

try: 
    # Get a collection of organisations.
    api_response = api_instance.organisations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->organisations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganisationCollection**](OrganisationCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_organisationid_get**
> Organisation organisations_organisationid_get(organisationid)

Get details about an organisation.

Get details about a specific organisation

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
organisationid = 'organisationid_example' # str | Specify the orgnisation identifier

try: 
    # Get details about an organisation.
    api_response = api_instance.organisations_organisationid_get(organisationid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->organisations_organisationid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisationid** | **str**| Specify the orgnisation identifier | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organisations_organisationid_put**
> Organisation organisations_organisationid_put(organisationid, body)

Update or create a new organisation.

Add a new organisation. Only an administrator can create a new organisation. 

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
organisationid = 'organisationid_example' # str | 
body = sensor_cloud.OrganisationPost() # OrganisationPost | This must match the organisationid parameter in the path

try: 
    # Update or create a new organisation.
    api_response = api_instance.organisations_organisationid_put(organisationid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->organisations_organisationid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisationid** | **str**|  | 
 **body** | [**OrganisationPost**](OrganisationPost.md)| This must match the organisationid parameter in the path | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_get**
> PlatformCollection platforms_get(id=id, name=name, limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, streamids=streamids, deployments_locationid=deployments_locationid)

Get a collection of platforms.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Only return platforms with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
name = 'name_example' # str | Only return platforms with this name or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
limit = 3.4 # float | Maximum number of streams to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
expand = true # bool | Return full details of platforms (optional)
recursive = true # bool | Return full details of embedded resources (optional)
groupids = 'groupids_example' # str | filter response by a comma separated list of group ids (optional)
streamids = 'streamids_example' # str | filter response by a comma separated list of stream ids (optional)
deployments_locationid = 'deployments_locationid_example' # str | filter response to include only platforms deployed at this location. Note this will consider all deployment properties both past and present. (optional)

try: 
    # Get a collection of platforms.
    api_response = api_instance.platforms_get(id=id, name=name, limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, streamids=streamids, deployments_locationid=deployments_locationid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->platforms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Only return platforms with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **name** | **str**| Only return platforms with this name or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **limit** | **float**| Maximum number of streams to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **expand** | **bool**| Return full details of platforms | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **groupids** | **str**| filter response by a comma separated list of group ids | [optional] 
 **streamids** | **str**| filter response by a comma separated list of stream ids | [optional] 
 **deployments_locationid** | **str**| filter response to include only platforms deployed at this location. Note this will consider all deployment properties both past and present. | [optional] 

### Return type

[**PlatformCollection**](PlatformCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_id_delete**
> platforms_id_delete(id, cascade=cascade)

Delete an existing platform.

Delete an existing Platform. The client must have an appropriate delete Platform permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
cascade = true # bool | Remove Platform even when is referenced by other objects (eg. SensorDeployments). (optional)

try: 
    # Delete an existing platform.
    api_instance.platforms_id_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling DefaultApi->platforms_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cascade** | **bool**| Remove Platform even when is referenced by other objects (eg. SensorDeployments). | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_id_get**
> platforms_id_get(id, recursive=recursive)

Get details about a platform.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Platform id
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a platform.
    api_instance.platforms_id_get(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->platforms_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Platform id | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platforms_id_put**
> platforms_id_put(id, body)

Create a new or update an existing platform.

Create a new platform. If a platform with the posted 'id' already exists then it will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
body = sensor_cloud.PlatformPost() # PlatformPost | 

try: 
    # Create a new or update an existing platform.
    api_instance.platforms_id_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->platforms_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**PlatformPost**](PlatformPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **procedures_get**
> SensingProcedureCollection procedures_get(limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, observed_property=observed_property)

Get a collection of sensing procedures.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
limit = 3.4 # float | Maximum number of sensing procedures to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
expand = true # bool | Return full details of sensing procedures (optional)
recursive = true # bool | Return full details of embedded resources (optional)
groupids = 'groupids_example' # str | filter response by a comma separated list of group ids (optional)
observed_property = 'observed_property_example' # str | filter response by observedProperty (optional)

try: 
    # Get a collection of sensing procedures.
    api_response = api_instance.procedures_get(limit=limit, skip=skip, organisationid=organisationid, expand=expand, recursive=recursive, groupids=groupids, observed_property=observed_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->procedures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Maximum number of sensing procedures to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **expand** | **bool**| Return full details of sensing procedures | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **groupids** | **str**| filter response by a comma separated list of group ids | [optional] 
 **observed_property** | **str**| filter response by observedProperty | [optional] 

### Return type

[**SensingProcedureCollection**](SensingProcedureCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **procedures_id_delete**
> procedures_id_delete(id, cascade=cascade)

Delete an existing sensing procedure.

Delete an existing sensing procedure. The client must have an appropriate delete sensing procedure permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
cascade = true # bool | Remove sensing procedure even when is referenced by other objects (eg. Streams). (optional)

try: 
    # Delete an existing sensing procedure.
    api_instance.procedures_id_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling DefaultApi->procedures_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cascade** | **bool**| Remove sensing procedure even when is referenced by other objects (eg. Streams). | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **procedures_id_get**
> procedures_id_get(id, recursive=recursive)

Get details about a sensing procedures.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | sensing procedure id
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a sensing procedures.
    api_instance.procedures_id_get(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->procedures_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| sensing procedure id | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **procedures_id_put**
> procedures_id_put(id, body)

Create a new or update an existing sensing procedure.

Create a new sensing procedure. If a sensing procedure with the posted 'id' already exists then it will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
body = sensor_cloud.SensingProcedurePost() # SensingProcedurePost | 

try: 
    # Create a new or update an existing sensing procedure.
    api_instance.procedures_id_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->procedures_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SensingProcedurePost**](SensingProcedurePost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_get**
> RoleCollection roles_get(expand=expand, recursive=recursive)

Get a collection of roles.

This operation returns a list of all roles or all roles in the authorised organisation. An admin role with read role permission is required, or an organisational role with role read permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
expand = true # bool | Return full details of roles (optional)
recursive = true # bool | Return full details of related objects (optional)

try: 
    # Get a collection of roles.
    api_response = api_instance.roles_get(expand=expand, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **bool**| Return full details of roles | [optional] 
 **recursive** | **bool**| Return full details of related objects | [optional] 

### Return type

[**RoleCollection**](RoleCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_roleid_delete**
> roles_roleid_delete(roleid)

Delete an existing role.

Delete an existing role. The client must have a delete role permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
roleid = 'roleid_example' # str | 

try: 
    # Delete an existing role.
    api_instance.roles_roleid_delete(roleid)
except ApiException as e:
    print("Exception when calling DefaultApi->roles_roleid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_roleid_get**
> Role roles_roleid_get(roleid, recursive=recursive)

Get details about a specific role.

Get role details

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
roleid = 'roleid_example' # str | Specify the role identifier
recursive = true # bool | Return full details of related objects (optional)

try: 
    # Get details about a specific role.
    api_response = api_instance.roles_roleid_get(roleid, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->roles_roleid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleid** | **str**| Specify the role identifier | 
 **recursive** | **bool**| Return full details of related objects | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_roleid_put**
> Role roles_roleid_put(roleid, body)

Update or create a role.

Add or update a Role. The User will need to have admin level Roles for creating or updating a Role, or an organisation level Role for creating or updating a Role.  Permissions can be one or more of the following - .AllPermission, .AllReadPermission, .AssignRolePermission, .CreateCollectionPermission, .CreateGroupPermission, .CreateLocationPermission, .CreateOrganisationPermission, .CreatePlatformPermission, .CreateProcedurePermission, .CreateResultsPermission, .CreateRolePermission, .CreateSharePermission, .CreateStreamPermission, .CreateUserPermission, .DeleteCollectionPermission, .DeleteGroupPermission, .DeleteLocationPermission, .DeleteOrganisationPermission, .DeletePlatformPermission, .DeleteProcedurePermission, .DeleteResultsPermission, .DeleteRolePermission, .DeleteSharePermission, .DeleteStreamPermission, .DeleteUserPermission, .ReadCollectionPermission, .ReadGroupPermission, .ReadLocationPermission, .ReadModelPermission, .ReadOrganisationPermission, .ReadPlatformPermission, .ReadProcedurePermission, .ReadResultsPermission, .ReadRolePermission, .ReadSharePermission, .ReadStreamPermission, .ReadUserPermission, .ReadWorkflowPermission, .ReadWorkflowResultsPermission, .RunWorkflowPermission, .UpdateCollectionPermission, .UpdateGroupPermission, .UpdateLocationPermission, .UpdateOrganisationPermission, .UpdatePlatformPermission, .UpdateProcedurePermission, .UpdateResultsPermission, .UpdateRolePermission, .UpdateSharePermission, .UpdateStreamPermission, .UpdateUserPermission, .WriteModelPermission, .WriteWorkflowPermission.  A client can only assign a permission to a role of a certain role scope if they already have a role with the 'createrolepermission'. For example if user a has an OrganisationRole with 'createrolepermission' they will beable to create an organisation role with any permission. Importantly they can only create an organisation role for the organisation with which they already have a 'createrolepermission'.   Similarly, if a client has a GroupRole with createrolepermission on 'group1' then they can create an other GroupRole with any permission.  Given this, the 'createrolepermission' essentially allows the client to do anything with the the scope of the role. 

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
roleid = 'roleid_example' # str | 
body = sensor_cloud.RolePost() # RolePost | This must match the roleid parameter in the path

try: 
    # Update or create a role.
    api_response = api_instance.roles_roleid_put(roleid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->roles_roleid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roleid** | **str**|  | 
 **body** | [**RolePost**](RolePost.md)| This must match the roleid parameter in the path | 

### Return type

[**Role**](Role.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> root_get()

Sensor Data API Root

The root resource of the sensor data API. Provides links to other resources and some general meta-data about the user and the API 

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()

try: 
    # Sensor Data API Root
    api_instance.root_get()
except ApiException as e:
    print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_count_get**
> ShareCollection shares_count_get(limit=limit, skip=skip, organisationid=organisationid, groupid=groupid, collectionid=collectionid, expand=expand, recursive=recursive)

Get a count of current shares.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
limit = 3.4 # float | Maximum number of shares to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
groupid = 'groupid_example' # str | filter response by a comma separated list of group ids (optional)
collectionid = 'collectionid_example' # str | filter response by a comma separated list of collection ids (optional)
expand = true # bool | Return full details of shares (optional)
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get a count of current shares.
    api_response = api_instance.shares_count_get(limit=limit, skip=skip, organisationid=organisationid, groupid=groupid, collectionid=collectionid, expand=expand, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shares_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Maximum number of shares to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **groupid** | **str**| filter response by a comma separated list of group ids | [optional] 
 **collectionid** | **str**| filter response by a comma separated list of collection ids | [optional] 
 **expand** | **bool**| Return full details of shares | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

[**ShareCollection**](ShareCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_get**
> ShareCollection shares_get(limit=limit, skip=skip, organisationid=organisationid, groupid=groupid, collectionid=collectionid, expand=expand, recursive=recursive)

Get a list of current shares.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
limit = 3.4 # float | Maximum number of shares to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
organisationid = 'organisationid_example' # str | filter response by this organisation id (optional)
groupid = 'groupid_example' # str | filter response by a comma separated list of group ids (optional)
collectionid = 'collectionid_example' # str | filter response by a comma separated list of collection ids (optional)
expand = true # bool | Return full details of shares (optional)
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get a list of current shares.
    api_response = api_instance.shares_get(limit=limit, skip=skip, organisationid=organisationid, groupid=groupid, collectionid=collectionid, expand=expand, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Maximum number of shares to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **organisationid** | **str**| filter response by this organisation id | [optional] 
 **groupid** | **str**| filter response by a comma separated list of group ids | [optional] 
 **collectionid** | **str**| filter response by a comma separated list of collection ids | [optional] 
 **expand** | **bool**| Return full details of shares | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

[**ShareCollection**](ShareCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_id_delete**
> shares_id_delete(id)

Delete an existing Share.

Delete an existing Share. The client must have an appropriate delete Share permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 

try: 
    # Delete an existing Share.
    api_instance.shares_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->shares_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_id_get**
> shares_id_get(id, recursive=recursive)

Get details about a share.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Share id
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a share.
    api_instance.shares_id_get(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling DefaultApi->shares_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Share id | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_id_put**
> shares_id_put(id, body)

Update an existing Share.

Update an existing Share. The existing object will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
body = sensor_cloud.SharePut() # SharePut | 

try: 
    # Update an existing Share.
    api_instance.shares_id_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->shares_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SharePut**](SharePut.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_post**
> shares_post(body)

Create a new share.

Create a new share. Do not provide the id property in the body. The server will generate a UUID.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
body = sensor_cloud.SharePost() # SharePost | 

try: 
    # Create a new share.
    api_instance.shares_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->shares_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharePost**](SharePost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streams_count_get**
> StreamCollectionCount streams_count_get(id=id, limit=limit, skip=skip, resulttype=resulttype, expand=expand, recursive=recursive, groupids=groupids, organisationid=organisationid, locationid=locationid, near=near, radius=radius, stream_metadata_observed_property=stream_metadata_observed_property, stream_metadata_unit_of_measure=stream_metadata_unit_of_measure, properties=properties)

Count a collection of streams.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Only return streams with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
limit = 3.4 # float | Maximum number of streams to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
resulttype = 'resulttype_example' # str | Return only Streams which match this resulttype. Valid resulttypes are geolocationvalue, scalarvalue, imagevalue and vectorvalue (optional)
expand = true # bool | Return full details of streams (optional)
recursive = true # bool | Return full details of embedded resources (optional)
groupids = 'groupids_example' # str | Only return streams in this group (optional)
organisationid = 'organisationid_example' # str | Only return streams in this organisation (optional)
locationid = 'locationid_example' # str | Only return streams with this location (optional)
near = 'near_example' # str | Return streams at locations based on how close they are to this WKT 'POINT'. For example 'near=POINT (lon lat)' where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id=25355 for WTK Specification and examples. (optional)
radius = 3.4 # float | Limit results to streams that have locations within this distance (in metres) of the 'near' location. (optional)
stream_metadata_observed_property = 'stream_metadata_observed_property_example' # str | Only return streams with this observed property URI (optional)
stream_metadata_unit_of_measure = 'stream_metadata_unit_of_measure_example' # str | Only return streams with this unit of measure URI (optional)
properties = 'properties_example' # str | Provide a comma separated list of properties to include in the collection. (optional)

try: 
    # Count a collection of streams.
    api_response = api_instance.streams_count_get(id=id, limit=limit, skip=skip, resulttype=resulttype, expand=expand, recursive=recursive, groupids=groupids, organisationid=organisationid, locationid=locationid, near=near, radius=radius, stream_metadata_observed_property=stream_metadata_observed_property, stream_metadata_unit_of_measure=stream_metadata_unit_of_measure, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->streams_count_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Only return streams with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **limit** | **float**| Maximum number of streams to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **resulttype** | **str**| Return only Streams which match this resulttype. Valid resulttypes are geolocationvalue, scalarvalue, imagevalue and vectorvalue | [optional] 
 **expand** | **bool**| Return full details of streams | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **groupids** | **str**| Only return streams in this group | [optional] 
 **organisationid** | **str**| Only return streams in this organisation | [optional] 
 **locationid** | **str**| Only return streams with this location | [optional] 
 **near** | **str**| Return streams at locations based on how close they are to this WKT &#39;POINT&#39;. For example &#39;near&#x3D;POINT (lon lat)&#39; where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id&#x3D;25355 for WTK Specification and examples. | [optional] 
 **radius** | **float**| Limit results to streams that have locations within this distance (in metres) of the &#39;near&#39; location. | [optional] 
 **stream_metadata_observed_property** | **str**| Only return streams with this observed property URI | [optional] 
 **stream_metadata_unit_of_measure** | **str**| Only return streams with this unit of measure URI | [optional] 
 **properties** | **str**| Provide a comma separated list of properties to include in the collection. | [optional] 

### Return type

[**StreamCollectionCount**](StreamCollectionCount.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streams_get**
> StreamCollection streams_get(id=id, limit=limit, skip=skip, resulttype=resulttype, expand=expand, recursive=recursive, groupids=groupids, organisationid=organisationid, locationid=locationid, near=near, radius=radius, stream_metadata_observed_property=stream_metadata_observed_property, stream_metadata_unit_of_measure=stream_metadata_unit_of_measure, properties=properties)

Get a collection of streams.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | Only return streams with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. (optional)
limit = 3.4 # float | Maximum number of streams to return (optional)
skip = 3.4 # float | Skip this many results. (optional)
resulttype = 'resulttype_example' # str | Return only Streams which match this resulttype. Valid resulttypes are geolocationvalue, scalarvalue, imagevalue and vectorvalue (optional)
expand = true # bool | Return full details of streams (optional)
recursive = true # bool | Return full details of embedded resources (optional)
groupids = 'groupids_example' # str | Only return streams in this group (optional)
organisationid = 'organisationid_example' # str | Only return streams in this organisation (optional)
locationid = 'locationid_example' # str | Only return streams with this location (optional)
near = 'near_example' # str | Return streams at locations based on how close they are to this WKT 'POINT'. For example 'near=POINT (lon lat)' where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id=25355 for WTK Specification and examples. (optional)
radius = 3.4 # float | Limit results to streams that have locations within this distance (in metres) of the 'near' location. (optional)
stream_metadata_observed_property = 'stream_metadata_observed_property_example' # str | Only return streams with this observed property URI (optional)
stream_metadata_unit_of_measure = 'stream_metadata_unit_of_measure_example' # str | Only return streams with this unit of measure URI (optional)
properties = 'properties_example' # str | Provide a comma separated list of properties to include in the collection. (optional)

try: 
    # Get a collection of streams.
    api_response = api_instance.streams_get(id=id, limit=limit, skip=skip, resulttype=resulttype, expand=expand, recursive=recursive, groupids=groupids, organisationid=organisationid, locationid=locationid, near=near, radius=radius, stream_metadata_observed_property=stream_metadata_observed_property, stream_metadata_unit_of_measure=stream_metadata_unit_of_measure, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->streams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Only return streams with this id or partial match using wildcards (*, ?).   * matches zero or more characters. * ? matches exactly one character.  For example, bo* will match any word starting with bo, such as bo, bom, body, and so on. On the other hand, bo? will only match three-letter words starting with bo, such as bo, bom, and so on. | [optional] 
 **limit** | **float**| Maximum number of streams to return | [optional] 
 **skip** | **float**| Skip this many results. | [optional] 
 **resulttype** | **str**| Return only Streams which match this resulttype. Valid resulttypes are geolocationvalue, scalarvalue, imagevalue and vectorvalue | [optional] 
 **expand** | **bool**| Return full details of streams | [optional] 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 
 **groupids** | **str**| Only return streams in this group | [optional] 
 **organisationid** | **str**| Only return streams in this organisation | [optional] 
 **locationid** | **str**| Only return streams with this location | [optional] 
 **near** | **str**| Return streams at locations based on how close they are to this WKT &#39;POINT&#39;. For example &#39;near&#x3D;POINT (lon lat)&#39; where lon and lat are your GPS coordinates. See http://portal.opengeospatial.org/files/?artifact_id&#x3D;25355 for WTK Specification and examples. | [optional] 
 **radius** | **float**| Limit results to streams that have locations within this distance (in metres) of the &#39;near&#39; location. | [optional] 
 **stream_metadata_observed_property** | **str**| Only return streams with this observed property URI | [optional] 
 **stream_metadata_unit_of_measure** | **str**| Only return streams with this unit of measure URI | [optional] 
 **properties** | **str**| Provide a comma separated list of properties to include in the collection. | [optional] 

### Return type

[**StreamCollection**](StreamCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streams_id_delete**
> streams_id_delete(id)

Delete an existing stream.

Delete an existing stream. The client must have an appropriate delete stream permission.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 

try: 
    # Delete an existing stream.
    api_instance.streams_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->streams_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streams_id_get**
> Stream streams_id_get(id, recursive=recursive)

Get details about a stream.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
recursive = true # bool | Return full details of embedded resources (optional)

try: 
    # Get details about a stream.
    api_response = api_instance.streams_id_get(id, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->streams_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **recursive** | **bool**| Return full details of embedded resources | [optional] 

### Return type

[**Stream**](Stream.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streams_id_put**
> streams_id_put(id, body)

Create a new or update an existing Stream.

Create a new Stream. If a stream with the posted 'id' already exists then it will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | 
body = sensor_cloud.StreamPost() # StreamPost | 

try: 
    # Create a new or update an existing Stream.
    api_instance.streams_id_put(id, body)
except ApiException as e:
    print("Exception when calling DefaultApi->streams_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**StreamPost**](StreamPost.md)|  | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> UserCollection users_get(expand=expand, recursive=recursive, roleids=roleids)

Get a collection of users.

This request will return a collection of all users known to the Sensor Data API. Only Organisation or Admin roles with the read user permission will be authorised.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
expand = true # bool | Return full details of users (optional)
recursive = true # bool | Return full details of roles (optional)
roleids = 'roleids_example' # str | A commona separated list of roleids to filter the returned roles. (optional)

try: 
    # Get a collection of users.
    api_response = api_instance.users_get(expand=expand, recursive=recursive, roleids=roleids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **bool**| Return full details of users | [optional] 
 **recursive** | **bool**| Return full details of roles | [optional] 
 **roleids** | **str**| A commona separated list of roleids to filter the returned roles. | [optional] 

### Return type

[**UserCollection**](UserCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_userid_get**
> User users_userid_get(userid, recursive=recursive)

Get details about a user.

Returns a User object for the specified user. You must either be authenticated as the requested user or have an administration or organisation role with read user permission. If a user id is not specified then details about the currently authenticated user will be returned.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
userid = 'userid_example' # str | Specify a user id (email address)
recursive = true # bool | Return full details of linked objects (optional)

try: 
    # Get details about a user.
    api_response = api_instance.users_userid_get(userid, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_userid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Specify a user id (email address) | 
 **recursive** | **bool**| Return full details of linked objects | [optional] 

### Return type

[**User**](User.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_userid_put**
> User users_userid_put(userid, body)

Update or create a user.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
userid = 'userid_example' # str | Specify a user id (email address)
body = sensor_cloud.UserPost() # UserPost | This must match the userid parameter in the path

try: 
    # Update or create a user.
    api_response = api_instance.users_userid_put(userid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_userid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Specify a user id (email address) | 
 **body** | [**UserPost**](UserPost.md)| This must match the userid parameter in the path | 

### Return type

[**User**](User.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vocabulary_get**
> VocabularyCollection vocabulary_get(query, type)

Search for vocabulary terms.

This operation will query linked registers. A query and type parameter must be provided. Using this operation a client can search for possible matches on both units of measure and observed property.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
query = 'query_example' # str | Keywords to search. '*' wild cards are permitted.
type = 'type_example' # str | Uri of concept type. Typically will be http://qudt.org/schema/qudt#Unit for units of measure and http://qudt.org/schema/qudt#QuantityKind for observed properties. Don't forget to URL encode the parameters.

try: 
    # Search for vocabulary terms.
    api_response = api_instance.vocabulary_get(query, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->vocabulary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Keywords to search. &#39;*&#39; wild cards are permitted. | 
 **type** | **str**| Uri of concept type. Typically will be http://qudt.org/schema/qudt#Unit for units of measure and http://qudt.org/schema/qudt#QuantityKind for observed properties. Don&#39;t forget to URL encode the parameters. | 

### Return type

[**VocabularyCollection**](VocabularyCollection.md)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vocabulary_proxy_get**
> vocabulary_proxy_get(id)

Resolve a specific vocabulary term

This operation will resolve a URI and return a JSON-LD document. Vocabulary terms can be resolved directly, however this operation allows an application to avoid mixed http/https content problems by using https to resolve the term. Only URIs from the whitelisted linked data registry instances are permitted.

### Example 
```python
from __future__ import print_function
import time
import sensor_cloud
from sensor_cloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: headerkey
sensor_cloud.configuration.api_key['X-apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-apiKey'] = 'Bearer'
# Configure API key authorization: kongheader
sensor_cloud.configuration.api_key['X-Consumer-Custom-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['X-Consumer-Custom-ID'] = 'Bearer'
# Configure HTTP basic authorization: normal
sensor_cloud.configuration.username = 'YOUR_USERNAME'
sensor_cloud.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: querykey
sensor_cloud.configuration.api_key['apiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# sensor_cloud.configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = sensor_cloud.DefaultApi()
id = 'id_example' # str | URI of vocabulary term to resolve.

try: 
    # Resolve a specific vocabulary term
    api_instance.vocabulary_proxy_get(id)
except ApiException as e:
    print("Exception when calling DefaultApi->vocabulary_proxy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| URI of vocabulary term to resolve. | 

### Return type

void (empty response body)

### Authorization

[headerkey](../README.md#headerkey), [kongheader](../README.md#kongheader), [normal](../README.md#normal), [querykey](../README.md#querykey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

