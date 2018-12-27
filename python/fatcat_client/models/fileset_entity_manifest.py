# coding: utf-8

"""
    fatcat

    A scalable, versioned, API-oriented catalog of bibliographic entities and file metadata  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FilesetEntityManifest(object):
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
        'path': 'str',
        'size': 'int',
        'md5': 'str',
        'sha1': 'str',
        'sha256': 'str',
        'extra': 'object'
    }

    attribute_map = {
        'path': 'path',
        'size': 'size',
        'md5': 'md5',
        'sha1': 'sha1',
        'sha256': 'sha256',
        'extra': 'extra'
    }

    def __init__(self, path=None, size=None, md5=None, sha1=None, sha256=None, extra=None):  # noqa: E501
        """FilesetEntityManifest - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._size = None
        self._md5 = None
        self._sha1 = None
        self._sha256 = None
        self._extra = None
        self.discriminator = None

        self.path = path
        self.size = size
        if md5 is not None:
            self.md5 = md5
        if sha1 is not None:
            self.sha1 = sha1
        if sha256 is not None:
            self.sha256 = sha256
        if extra is not None:
            self.extra = extra

    @property
    def path(self):
        """Gets the path of this FilesetEntityManifest.  # noqa: E501


        :return: The path of this FilesetEntityManifest.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FilesetEntityManifest.


        :param path: The path of this FilesetEntityManifest.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def size(self):
        """Gets the size of this FilesetEntityManifest.  # noqa: E501


        :return: The size of this FilesetEntityManifest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FilesetEntityManifest.


        :param size: The size of this FilesetEntityManifest.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def md5(self):
        """Gets the md5 of this FilesetEntityManifest.  # noqa: E501


        :return: The md5 of this FilesetEntityManifest.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FilesetEntityManifest.


        :param md5: The md5 of this FilesetEntityManifest.  # noqa: E501
        :type: str
        """
        if md5 is not None and len(md5) > 32:
            raise ValueError("Invalid value for `md5`, length must be less than or equal to `32`")  # noqa: E501
        if md5 is not None and len(md5) < 32:
            raise ValueError("Invalid value for `md5`, length must be greater than or equal to `32`")  # noqa: E501
        if md5 is not None and not re.search('[a-f0-9]{32}', md5):  # noqa: E501
            raise ValueError("Invalid value for `md5`, must be a follow pattern or equal to `/[a-f0-9]{32}/`")  # noqa: E501

        self._md5 = md5

    @property
    def sha1(self):
        """Gets the sha1 of this FilesetEntityManifest.  # noqa: E501


        :return: The sha1 of this FilesetEntityManifest.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FilesetEntityManifest.


        :param sha1: The sha1 of this FilesetEntityManifest.  # noqa: E501
        :type: str
        """
        if sha1 is not None and len(sha1) > 40:
            raise ValueError("Invalid value for `sha1`, length must be less than or equal to `40`")  # noqa: E501
        if sha1 is not None and len(sha1) < 40:
            raise ValueError("Invalid value for `sha1`, length must be greater than or equal to `40`")  # noqa: E501
        if sha1 is not None and not re.search('[a-f0-9]{40}', sha1):  # noqa: E501
            raise ValueError("Invalid value for `sha1`, must be a follow pattern or equal to `/[a-f0-9]{40}/`")  # noqa: E501

        self._sha1 = sha1

    @property
    def sha256(self):
        """Gets the sha256 of this FilesetEntityManifest.  # noqa: E501


        :return: The sha256 of this FilesetEntityManifest.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this FilesetEntityManifest.


        :param sha256: The sha256 of this FilesetEntityManifest.  # noqa: E501
        :type: str
        """
        if sha256 is not None and len(sha256) > 64:
            raise ValueError("Invalid value for `sha256`, length must be less than or equal to `64`")  # noqa: E501
        if sha256 is not None and len(sha256) < 64:
            raise ValueError("Invalid value for `sha256`, length must be greater than or equal to `64`")  # noqa: E501
        if sha256 is not None and not re.search('[a-f0-9]{64}', sha256):  # noqa: E501
            raise ValueError("Invalid value for `sha256`, must be a follow pattern or equal to `/[a-f0-9]{64}/`")  # noqa: E501

        self._sha256 = sha256

    @property
    def extra(self):
        """Gets the extra of this FilesetEntityManifest.  # noqa: E501


        :return: The extra of this FilesetEntityManifest.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this FilesetEntityManifest.


        :param extra: The extra of this FilesetEntityManifest.  # noqa: E501
        :type: object
        """

        self._extra = extra

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
        if not isinstance(other, FilesetEntityManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
