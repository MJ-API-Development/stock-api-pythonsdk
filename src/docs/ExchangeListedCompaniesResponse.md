## General Fundamental Data For Exchange Listed Companies

The General Fundamental Data For Exchange Listed Companies model provides general information about companies listed on 
an exchange. This model contains several properties that provide valuable information for investors and analysts.

The "message" property is a string that indicates whether the data was successfully retrieved or if there was an error. 
If the data was retrieved successfully, the message will indicate success, otherwise it will provide an error message.

The "payload" property is an instance of the General model, which contains the general fundamental data for 
the exchange listed companies.

The "status" property is a boolean that indicates whether the data is found and valid. If the data is found and valid, 
the status will be True, otherwise it will be False.

### Properties
| Name        | Type                      | Description                     | Notes      |
|-------------|---------------------------|---------------------------------|------------|
| **message** | **str**                   | success or error message        | [optional] |
| **payload** | [**General**](General.md) |                                 | [optional] |
| **status**  | **bool**                  | True if data is found and valid | [optional] |

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


