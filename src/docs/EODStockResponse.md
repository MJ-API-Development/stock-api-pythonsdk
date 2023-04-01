# EODStockResponse

The EODStockResponse model represents the response data that is returned by the EODStock API endpoint. This model contains three optional properties that provide information about the status of the API call and the data that was returned.

The "message" property is a string that indicates whether the API call was successful or if an error occurred. If the call was successful, the "message" property will contain the string "Success". If an error occurred, the "message" property will contain a description of the error.

The "payload" property is an instance of the "EODStock" object, which contains data about the requested stock. This object includes properties such as the stock symbol, the date range of the stock data, and an array of daily stock data points.

The "status" property is a Boolean value that indicates whether the data returned by the API is valid. If the data is valid, the "status" property will be set to "True". If the data is invalid, the "status" property will be set to "False".
## Properties
| Name        | Type                        | Description                     | Notes      |
|-------------|-----------------------------|---------------------------------|------------|
| **message** | **str**                     | success or error message        | [optional] |
| **payload** | [**EODStock**](EODStock.md) |                                 | [optional] |
| **status**  | **bool**                    | True if data is found and valid | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


