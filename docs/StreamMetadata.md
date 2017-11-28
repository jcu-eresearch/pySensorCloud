# StreamMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**observed_property** | **str** | (Only applicable for ScalarStreamMetaData) Use the /vocabulary API to search for an applicable term. If you can&#39;t find a suitable term then contact the SensorCloud team to get your observed property added. | 
**unit_of_measure** | **str** | (Only applicable for GeoLocationStreamMetaData) Use the /vocabulary API to search for an applicable term. If you can&#39;t find a suitable term then contact SensorCloud team to get your unit of measure added. | 
**interpolation_type** | **str** | Only &#39;Continuous&#39; and &#39;Discontinuous&#39; interpolation types are valid for GeoLocationValue resulttype. | 
**cummulative** | **bool** | (Only applicable for ScalarStreamMetaData). Does this data stream represent an accumulated total. | [optional] 
**accumulation_interval** | **str** | (Only applicable for cummulative streams). Specify the accumulation interval using ISO8601 duration format. Use the most appropriate calendar unit. | [optional] 
**accumulation_anchor** | **str** | (Only applicable for cummulative streams). Specify the accumulation anchor using ISO8601 format. | [optional] 
**timezone** | **str** | Timezone of data stream. Required for cummulative scalar streams. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


