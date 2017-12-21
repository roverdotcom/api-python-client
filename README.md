# onfido
The Onfido API is used to submit check requests.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.1.0
- Build date: 2017-12-21T16:52:44.835Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/onfido/api-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/onfido/api-python-client.git`)

Then import the package:
```python
import onfido 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import onfido
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import onfido
from onfido.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
onfido.configuration.api_key['Authorization'] = 'token=' + 'YOUR_API_KEY'
onfido.configuration.api_key_prefix['Authorization'] = 'Token'
# create an instance of the API class
api_instance = onfido.DefaultApi()

# setting applicant details
applicant = onfido.Applicant()
applicant.first_name = 'John'
applicant.last_name = 'Smith'
applicant.dob = datetime.date(1980, 1, 22)
applicant.country = 'GBR'

address = onfido.Address()
address.building_number = '100'
address.street = 'Main Street'
address.town = 'London'
address.postcode = 'SW4 6EH'
address.country = 'GBR'

applicant.addresses = [address];

# setting check request details
check = onfido.CheckCreationRequest()
check.type = 'express'

report = onfido.Report()
report.name = 'identity'

check.reports = [report];

try: 
    # Create Applicant
    api_response = api_instance.create_applicant(data=applicant)
    applicant_id = api_response.id
    api_response = api_instance.create_check(applicant_id, data=check)
    pprint(api_response)
except ApiException as e:
    pprint(e.body)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.onfido.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**cancel_report**](docs/DefaultApi.md#cancel_report) | **POST** /checks/{check_id}/reports/{report_id}/cancel | This endpoint is for cancelling individual paused reports.
*DefaultApi* | [**create_applicant**](docs/DefaultApi.md#create_applicant) | **POST** /applicants | Create Applicant
*DefaultApi* | [**create_check**](docs/DefaultApi.md#create_check) | **POST** /applicants/{applicant_id}/checks | Create a check
*DefaultApi* | [**create_webhook**](docs/DefaultApi.md#create_webhook) | **POST** /webhooks | Create a webhook
*DefaultApi* | [**destroy_applicant**](docs/DefaultApi.md#destroy_applicant) | **DELETE** /applicants/{applicant_id} | Delete Applicant
*DefaultApi* | [**download_document**](docs/DefaultApi.md#download_document) | **GET** /applicants/{applicant_id}/documents/{document_id}/download | Download a documents raw data
*DefaultApi* | [**download_live_photo**](docs/DefaultApi.md#download_live_photo) | **GET** /live_photos/{live_photo_id}/download | Download live photo
*DefaultApi* | [**find_addresses**](docs/DefaultApi.md#find_addresses) | **GET** /addresses/pick | Search for addresses by postcode
*DefaultApi* | [**find_applicant**](docs/DefaultApi.md#find_applicant) | **GET** /applicants/{applicant_id} | Retrieve Applicant
*DefaultApi* | [**find_check**](docs/DefaultApi.md#find_check) | **GET** /applicants/{applicant_id}/checks/{check_id} | Retrieve a Check
*DefaultApi* | [**find_document**](docs/DefaultApi.md#find_document) | **GET** /applicants/{applicant_id}/documents/{document_id} | A single document can be retrieved by calling this endpoint with the document’s unique identifier.
*DefaultApi* | [**find_live_photo**](docs/DefaultApi.md#find_live_photo) | **GET** /live_photos/{live_photo_id} | Retrieve live photo
*DefaultApi* | [**find_report**](docs/DefaultApi.md#find_report) | **GET** /checks/{check_id}/reports/{report_id} | A single report can be retrieved using this endpoint with the corresponding unique identifier.
*DefaultApi* | [**find_report_type_group**](docs/DefaultApi.md#find_report_type_group) | **GET** /report_type_groups/{report_type_group_id} | Retrieve single report type group object
*DefaultApi* | [**find_webhook**](docs/DefaultApi.md#find_webhook) | **GET** /webhooks/{webhook_id} | Retrieve a Webhook
*DefaultApi* | [**list_applicants**](docs/DefaultApi.md#list_applicants) | **GET** /applicants | List Applicants
*DefaultApi* | [**list_checks**](docs/DefaultApi.md#list_checks) | **GET** /applicants/{applicant_id}/checks | Retrieve Checks
*DefaultApi* | [**list_documents**](docs/DefaultApi.md#list_documents) | **GET** /applicants/{applicant_id}/documents | List documents
*DefaultApi* | [**list_live_photos**](docs/DefaultApi.md#list_live_photos) | **GET** /live_photos | List live photos
*DefaultApi* | [**list_report_type_groups**](docs/DefaultApi.md#list_report_type_groups) | **GET** /report_type_groups | Retrieve all report type groups
*DefaultApi* | [**list_reports**](docs/DefaultApi.md#list_reports) | **GET** /checks/{check_id}/reports | All the reports belonging to a particular check can be listed from this endpoint.
*DefaultApi* | [**list_webhooks**](docs/DefaultApi.md#list_webhooks) | **GET** /webhooks | List webhooks
*DefaultApi* | [**resume_check**](docs/DefaultApi.md#resume_check) | **POST** /checks/{check_id}/resume | Resume a Check
*DefaultApi* | [**resume_report**](docs/DefaultApi.md#resume_report) | **POST** /checks/{check_id}/reports/{report_id}/resume | This endpoint is for resuming individual paused reports.
*DefaultApi* | [**update_applicant**](docs/DefaultApi.md#update_applicant) | **PUT** /applicants/{applicant_id} | Update Applicant
*DefaultApi* | [**upload_document**](docs/DefaultApi.md#upload_document) | **POST** /applicants/{applicant_id}/documents | Upload a document
*DefaultApi* | [**upload_live_photo**](docs/DefaultApi.md#upload_live_photo) | **POST** /live_photos | Upload live photo


## Documentation For Models

 - [Address](docs/Address.md)
 - [Applicant](docs/Applicant.md)
 - [ApplicantsList](docs/ApplicantsList.md)
 - [Check](docs/Check.md)
 - [CheckCreationRequest](docs/CheckCreationRequest.md)
 - [ChecksList](docs/ChecksList.md)
 - [Document](docs/Document.md)
 - [DocumentsList](docs/DocumentsList.md)
 - [Error](docs/Error.md)
 - [GenericAddress](docs/GenericAddress.md)
 - [GenericAddressesList](docs/GenericAddressesList.md)
 - [IdNumber](docs/IdNumber.md)
 - [LivePhoto](docs/LivePhoto.md)
 - [LivePhotosList](docs/LivePhotosList.md)
 - [Report](docs/Report.md)
 - [ReportType](docs/ReportType.md)
 - [ReportTypeGroup](docs/ReportTypeGroup.md)
 - [ReportTypeGroupsList](docs/ReportTypeGroupsList.md)
 - [ReportTypeOption](docs/ReportTypeOption.md)
 - [ReportsList](docs/ReportsList.md)
 - [Webhook](docs/Webhook.md)
 - [WebhooksList](docs/WebhooksList.md)