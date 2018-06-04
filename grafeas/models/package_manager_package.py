# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from grafeas.models.package_manager_distribution import PackageManagerDistribution  # noqa: F401,E501


class PackageManagerPackage(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'name': 'str',
        'distribution': 'list[PackageManagerDistribution]'
    }

    attribute_map = {
        'name': 'name',
        'distribution': 'distribution'
    }

    def __init__(self, name=None, distribution=None):  # noqa: E501
        """PackageManagerPackage - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._distribution = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if distribution is not None:
            self.distribution = distribution

    @property
    def name(self):
        """Gets the name of this PackageManagerPackage.  # noqa: E501

        The name of the package.  # noqa: E501

        :return: The name of this PackageManagerPackage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageManagerPackage.

        The name of the package.  # noqa: E501

        :param name: The name of this PackageManagerPackage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def distribution(self):
        """Gets the distribution of this PackageManagerPackage.  # noqa: E501

        The various channels by which a package is distributed.  # noqa: E501

        :return: The distribution of this PackageManagerPackage.  # noqa: E501
        :rtype: list[PackageManagerDistribution]
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this PackageManagerPackage.

        The various channels by which a package is distributed.  # noqa: E501

        :param distribution: The distribution of this PackageManagerPackage.  # noqa: E501
        :type: list[PackageManagerDistribution]
        """

        self._distribution = distribution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PackageManagerPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
