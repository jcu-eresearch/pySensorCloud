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


class GroupCollectionEmbedded(object):
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
        'groups': 'list[Group]'
    }

    attribute_map = {
        'groups': 'groups'
    }

    def __init__(self, groups=None):
        """
        GroupCollectionEmbedded - a model defined in Swagger
        """

        self._groups = None

        if groups is not None:
          self.groups = groups

    @property
    def groups(self):
        """
        Gets the groups of this GroupCollectionEmbedded.

        :return: The groups of this GroupCollectionEmbedded.
        :rtype: list[Group]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this GroupCollectionEmbedded.

        :param groups: The groups of this GroupCollectionEmbedded.
        :type: list[Group]
        """

        self._groups = groups

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
        if not isinstance(other, GroupCollectionEmbedded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
