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


class UnivariateResult(object):
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
        't': 'str',
        'v': 'object'
    }

    attribute_map = {
        't': 't',
        'v': 'v'
    }

    def __init__(self, t=None, v=None):
        """
        UnivariateResult - a model defined in Swagger
        """

        self._t = None
        self._v = None

        if t is not None:
          self.t = t
        if v is not None:
          self.v = v

    @property
    def t(self):
        """
        Gets the t of this UnivariateResult.

        :return: The t of this UnivariateResult.
        :rtype: str
        """
        return self._t

    @t.setter
    def t(self, t):
        """
        Sets the t of this UnivariateResult.

        :param t: The t of this UnivariateResult.
        :type: str
        """

        self._t = t

    @property
    def v(self):
        """
        Gets the v of this UnivariateResult.

        :return: The v of this UnivariateResult.
        :rtype: object
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        Sets the v of this UnivariateResult.

        :param v: The v of this UnivariateResult.
        :type: object
        """

        self._v = v

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
        if not isinstance(other, UnivariateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
