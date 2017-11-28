# coding: utf-8

"""
    Sensor Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LocationPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'organisationid': 'str',
        'description': 'str',
        'groupids': 'list[str]',
        'geo_json': 'GeoJSONPoint'
    }

    attribute_map = {
        'id': 'id',
        'organisationid': 'organisationid',
        'description': 'description',
        'groupids': 'groupids',
        'geo_json': 'geoJson'
    }

    def __init__(self, id=None, organisationid=None, description=None, groupids=None, geo_json=None):
        """
        LocationPost - a model defined in Swagger
        """

        self._id = None
        self._organisationid = None
        self._description = None
        self._groupids = None
        self._geo_json = None

        self.id = id
        self.organisationid = organisationid
        if description is not None:
          self.description = description
        if groupids is not None:
          self.groupids = groupids
        if geo_json is not None:
          self.geo_json = geo_json

    @property
    def id(self):
        """
        Gets the id of this LocationPost.

        :return: The id of this LocationPost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LocationPost.

        :param id: The id of this LocationPost.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def organisationid(self):
        """
        Gets the organisationid of this LocationPost.

        :return: The organisationid of this LocationPost.
        :rtype: str
        """
        return self._organisationid

    @organisationid.setter
    def organisationid(self, organisationid):
        """
        Sets the organisationid of this LocationPost.

        :param organisationid: The organisationid of this LocationPost.
        :type: str
        """
        if organisationid is None:
            raise ValueError("Invalid value for `organisationid`, must not be `None`")

        self._organisationid = organisationid

    @property
    def description(self):
        """
        Gets the description of this LocationPost.

        :return: The description of this LocationPost.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LocationPost.

        :param description: The description of this LocationPost.
        :type: str
        """

        self._description = description

    @property
    def groupids(self):
        """
        Gets the groupids of this LocationPost.
        A list of group identifiers for which this Location will be a member.

        :return: The groupids of this LocationPost.
        :rtype: list[str]
        """
        return self._groupids

    @groupids.setter
    def groupids(self, groupids):
        """
        Sets the groupids of this LocationPost.
        A list of group identifiers for which this Location will be a member.

        :param groupids: The groupids of this LocationPost.
        :type: list[str]
        """

        self._groupids = groupids

    @property
    def geo_json(self):
        """
        Gets the geo_json of this LocationPost.

        :return: The geo_json of this LocationPost.
        :rtype: GeoJSONPoint
        """
        return self._geo_json

    @geo_json.setter
    def geo_json(self, geo_json):
        """
        Sets the geo_json of this LocationPost.

        :param geo_json: The geo_json of this LocationPost.
        :type: GeoJSONPoint
        """

        self._geo_json = geo_json

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LocationPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
