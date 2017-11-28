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


class PlatformPost(object):
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
        'name': 'str',
        'organisationid': 'str',
        'groupids': 'list[str]',
        'streamids': 'list[str]',
        'deployments': 'list[PlatformDeployment]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'organisationid': 'organisationid',
        'groupids': 'groupids',
        'streamids': 'streamids',
        'deployments': 'deployments'
    }

    def __init__(self, id=None, name=None, organisationid=None, groupids=None, streamids=None, deployments=None):
        """
        PlatformPost - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._organisationid = None
        self._groupids = None
        self._streamids = None
        self._deployments = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if organisationid is not None:
          self.organisationid = organisationid
        if groupids is not None:
          self.groupids = groupids
        if streamids is not None:
          self.streamids = streamids
        if deployments is not None:
          self.deployments = deployments

    @property
    def id(self):
        """
        Gets the id of this PlatformPost.

        :return: The id of this PlatformPost.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PlatformPost.

        :param id: The id of this PlatformPost.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PlatformPost.

        :return: The name of this PlatformPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PlatformPost.

        :param name: The name of this PlatformPost.
        :type: str
        """

        self._name = name

    @property
    def organisationid(self):
        """
        Gets the organisationid of this PlatformPost.

        :return: The organisationid of this PlatformPost.
        :rtype: str
        """
        return self._organisationid

    @organisationid.setter
    def organisationid(self, organisationid):
        """
        Sets the organisationid of this PlatformPost.

        :param organisationid: The organisationid of this PlatformPost.
        :type: str
        """

        self._organisationid = organisationid

    @property
    def groupids(self):
        """
        Gets the groupids of this PlatformPost.
        A list of group identifiers for which this stream will be a member.

        :return: The groupids of this PlatformPost.
        :rtype: list[str]
        """
        return self._groupids

    @groupids.setter
    def groupids(self, groupids):
        """
        Sets the groupids of this PlatformPost.
        A list of group identifiers for which this stream will be a member.

        :param groupids: The groupids of this PlatformPost.
        :type: list[str]
        """

        self._groupids = groupids

    @property
    def streamids(self):
        """
        Gets the streamids of this PlatformPost.
        Streams linked directly to platform

        :return: The streamids of this PlatformPost.
        :rtype: list[str]
        """
        return self._streamids

    @streamids.setter
    def streamids(self, streamids):
        """
        Sets the streamids of this PlatformPost.
        Streams linked directly to platform

        :param streamids: The streamids of this PlatformPost.
        :type: list[str]
        """

        self._streamids = streamids

    @property
    def deployments(self):
        """
        Gets the deployments of this PlatformPost.

        :return: The deployments of this PlatformPost.
        :rtype: list[PlatformDeployment]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """
        Sets the deployments of this PlatformPost.

        :param deployments: The deployments of this PlatformPost.
        :type: list[PlatformDeployment]
        """

        self._deployments = deployments

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
        if not isinstance(other, PlatformPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other