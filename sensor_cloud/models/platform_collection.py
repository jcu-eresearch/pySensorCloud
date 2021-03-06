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


class PlatformCollection(object):
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
        'links': 'OrganisationLinks',
        'embedded': 'PlatformCollectionEmbedded',
        'count': 'float'
    }

    attribute_map = {
        'links': '_links',
        'embedded': '_embedded',
        'count': 'count'
    }

    def __init__(self, links=None, embedded=None, count=None):
        """
        PlatformCollection - a model defined in Swagger
        """

        self._links = None
        self._embedded = None
        self._count = None

        if links is not None:
          self.links = links
        if embedded is not None:
          self.embedded = embedded
        if count is not None:
          self.count = count

    @property
    def links(self):
        """
        Gets the links of this PlatformCollection.

        :return: The links of this PlatformCollection.
        :rtype: OrganisationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PlatformCollection.

        :param links: The links of this PlatformCollection.
        :type: OrganisationLinks
        """

        self._links = links

    @property
    def embedded(self):
        """
        Gets the embedded of this PlatformCollection.

        :return: The embedded of this PlatformCollection.
        :rtype: PlatformCollectionEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """
        Sets the embedded of this PlatformCollection.

        :param embedded: The embedded of this PlatformCollection.
        :type: PlatformCollectionEmbedded
        """

        self._embedded = embedded

    @property
    def count(self):
        """
        Gets the count of this PlatformCollection.

        :return: The count of this PlatformCollection.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PlatformCollection.

        :param count: The count of this PlatformCollection.
        :type: float
        """

        self._count = count

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
        if not isinstance(other, PlatformCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
