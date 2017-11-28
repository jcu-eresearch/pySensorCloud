# RolePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A string identifier for the role. If the identifier already exists then this will be treated as an update operation.   | 
**type** | **str** | This can be either \&quot;.OrganisationRole\&quot;, \&quot;.AdministrationRole\&quot; or \&quot;.GroupRole\&quot; | 
**organisationid** | **str** |  | 
**permissions** | [**list[RolePostPermissions]**](RolePostPermissions.md) | A list of permissions. | 
**groupid** | **str** |  | [optional] 
**implied** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


