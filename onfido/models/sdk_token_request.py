# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SdkTokenRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'applicant_id': 'str',
        'referrer': 'str',
        'application_id': 'str'
    }

    attribute_map = {
        'applicant_id': 'applicant_id',
        'referrer': 'referrer',
        'application_id': 'application_id'
    }

    def __init__(self, applicant_id=None, referrer=None, application_id=None):  # noqa: E501
        """SdkTokenRequest - a model defined in OpenAPI"""  # noqa: E501

        self._applicant_id = None
        self._referrer = None
        self._application_id = None
        self.discriminator = None

        self.applicant_id = applicant_id
        if referrer is not None:
            self.referrer = referrer
        if application_id is not None:
            self.application_id = application_id

    @property
    def applicant_id(self):
        """Gets the applicant_id of this SdkTokenRequest.  # noqa: E501

        The unique identifier of the applicant  # noqa: E501

        :return: The applicant_id of this SdkTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, applicant_id):
        """Sets the applicant_id of this SdkTokenRequest.

        The unique identifier of the applicant  # noqa: E501

        :param applicant_id: The applicant_id of this SdkTokenRequest.  # noqa: E501
        :type: str
        """
        if applicant_id is None:
            raise ValueError("Invalid value for `applicant_id`, must not be `None`")  # noqa: E501

        self._applicant_id = applicant_id

    @property
    def referrer(self):
        """Gets the referrer of this SdkTokenRequest.  # noqa: E501

        The referrer URL pattern  # noqa: E501

        :return: The referrer of this SdkTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this SdkTokenRequest.

        The referrer URL pattern  # noqa: E501

        :param referrer: The referrer of this SdkTokenRequest.  # noqa: E501
        :type: str
        """

        self._referrer = referrer

    @property
    def application_id(self):
        """Gets the application_id of this SdkTokenRequest.  # noqa: E501

        The application ID (iOS or Android)  # noqa: E501

        :return: The application_id of this SdkTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this SdkTokenRequest.

        The application ID (iOS or Android)  # noqa: E501

        :param application_id: The application_id of this SdkTokenRequest.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SdkTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
