# coding: utf-8

"""
    fatcat

    Fatcat is a scalable, versioned, API-oriented catalog of bibliographic entities and file metadata.   # noqa: E501

    OpenAPI spec version: 0.3.1
    Contact: webservices@archive.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WorkEntity(object):
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
        'edit_extra': 'object',
        'extra': 'object',
        'redirect': 'str',
        'revision': 'str',
        'ident': 'str',
        'state': 'str'
    }

    attribute_map = {
        'edit_extra': 'edit_extra',
        'extra': 'extra',
        'redirect': 'redirect',
        'revision': 'revision',
        'ident': 'ident',
        'state': 'state'
    }

    def __init__(self, edit_extra=None, extra=None, redirect=None, revision=None, ident=None, state=None):  # noqa: E501
        """WorkEntity - a model defined in Swagger"""  # noqa: E501

        self._edit_extra = None
        self._extra = None
        self._redirect = None
        self._revision = None
        self._ident = None
        self._state = None
        self.discriminator = None

        if edit_extra is not None:
            self.edit_extra = edit_extra
        if extra is not None:
            self.extra = extra
        if redirect is not None:
            self.redirect = redirect
        if revision is not None:
            self.revision = revision
        if ident is not None:
            self.ident = ident
        if state is not None:
            self.state = state

    @property
    def edit_extra(self):
        """Gets the edit_extra of this WorkEntity.  # noqa: E501

        Free-form JSON metadata that will be stored with specific entity edits (eg, creation/update/delete).   # noqa: E501

        :return: The edit_extra of this WorkEntity.  # noqa: E501
        :rtype: object
        """
        return self._edit_extra

    @edit_extra.setter
    def edit_extra(self, edit_extra):
        """Sets the edit_extra of this WorkEntity.

        Free-form JSON metadata that will be stored with specific entity edits (eg, creation/update/delete).   # noqa: E501

        :param edit_extra: The edit_extra of this WorkEntity.  # noqa: E501
        :type: object
        """

        self._edit_extra = edit_extra

    @property
    def extra(self):
        """Gets the extra of this WorkEntity.  # noqa: E501

        Free-form JSON metadata that will be stored with the other entity metadata. See guide for (unenforced) schema conventions.   # noqa: E501

        :return: The extra of this WorkEntity.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this WorkEntity.

        Free-form JSON metadata that will be stored with the other entity metadata. See guide for (unenforced) schema conventions.   # noqa: E501

        :param extra: The extra of this WorkEntity.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def redirect(self):
        """Gets the redirect of this WorkEntity.  # noqa: E501

        base32-encoded unique identifier  # noqa: E501

        :return: The redirect of this WorkEntity.  # noqa: E501
        :rtype: str
        """
        return self._redirect

    @redirect.setter
    def redirect(self, redirect):
        """Sets the redirect of this WorkEntity.

        base32-encoded unique identifier  # noqa: E501

        :param redirect: The redirect of this WorkEntity.  # noqa: E501
        :type: str
        """
        if redirect is not None and len(redirect) > 26:
            raise ValueError("Invalid value for `redirect`, length must be less than or equal to `26`")  # noqa: E501
        if redirect is not None and len(redirect) < 26:
            raise ValueError("Invalid value for `redirect`, length must be greater than or equal to `26`")  # noqa: E501
        if redirect is not None and not re.search('[a-zA-Z2-7]{26}', redirect):  # noqa: E501
            raise ValueError("Invalid value for `redirect`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._redirect = redirect

    @property
    def revision(self):
        """Gets the revision of this WorkEntity.  # noqa: E501

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :return: The revision of this WorkEntity.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this WorkEntity.

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :param revision: The revision of this WorkEntity.  # noqa: E501
        :type: str
        """
        if revision is not None and len(revision) > 36:
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `36`")  # noqa: E501
        if revision is not None and len(revision) < 36:
            raise ValueError("Invalid value for `revision`, length must be greater than or equal to `36`")  # noqa: E501
        if revision is not None and not re.search('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', revision):  # noqa: E501
            raise ValueError("Invalid value for `revision`, must be a follow pattern or equal to `/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/`")  # noqa: E501

        self._revision = revision

    @property
    def ident(self):
        """Gets the ident of this WorkEntity.  # noqa: E501

        base32-encoded unique identifier  # noqa: E501

        :return: The ident of this WorkEntity.  # noqa: E501
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident):
        """Sets the ident of this WorkEntity.

        base32-encoded unique identifier  # noqa: E501

        :param ident: The ident of this WorkEntity.  # noqa: E501
        :type: str
        """
        if ident is not None and len(ident) > 26:
            raise ValueError("Invalid value for `ident`, length must be less than or equal to `26`")  # noqa: E501
        if ident is not None and len(ident) < 26:
            raise ValueError("Invalid value for `ident`, length must be greater than or equal to `26`")  # noqa: E501
        if ident is not None and not re.search('[a-zA-Z2-7]{26}', ident):  # noqa: E501
            raise ValueError("Invalid value for `ident`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._ident = ident

    @property
    def state(self):
        """Gets the state of this WorkEntity.  # noqa: E501


        :return: The state of this WorkEntity.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WorkEntity.


        :param state: The state of this WorkEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["wip", "active", "redirect", "deleted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, WorkEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
