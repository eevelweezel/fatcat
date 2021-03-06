# coding: utf-8

"""
    fatcat

    Fatcat is a scalable, versioned, API-oriented catalog of bibliographic entities and file metadata.   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: webservices@archive.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class EntityHistoryEntry(object):
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
        'edit': 'EntityEdit',
        'editgroup': 'Editgroup',
        'changelog_entry': 'ChangelogEntry'
    }

    attribute_map = {
        'edit': 'edit',
        'editgroup': 'editgroup',
        'changelog_entry': 'changelog_entry'
    }

    def __init__(self, edit=None, editgroup=None, changelog_entry=None):  # noqa: E501
        """EntityHistoryEntry - a model defined in OpenAPI"""  # noqa: E501

        self._edit = None
        self._editgroup = None
        self._changelog_entry = None
        self.discriminator = None

        self.edit = edit
        self.editgroup = editgroup
        self.changelog_entry = changelog_entry

    @property
    def edit(self):
        """Gets the edit of this EntityHistoryEntry.  # noqa: E501


        :return: The edit of this EntityHistoryEntry.  # noqa: E501
        :rtype: EntityEdit
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this EntityHistoryEntry.


        :param edit: The edit of this EntityHistoryEntry.  # noqa: E501
        :type: EntityEdit
        """
        if edit is None:
            raise ValueError("Invalid value for `edit`, must not be `None`")  # noqa: E501

        self._edit = edit

    @property
    def editgroup(self):
        """Gets the editgroup of this EntityHistoryEntry.  # noqa: E501


        :return: The editgroup of this EntityHistoryEntry.  # noqa: E501
        :rtype: Editgroup
        """
        return self._editgroup

    @editgroup.setter
    def editgroup(self, editgroup):
        """Sets the editgroup of this EntityHistoryEntry.


        :param editgroup: The editgroup of this EntityHistoryEntry.  # noqa: E501
        :type: Editgroup
        """
        if editgroup is None:
            raise ValueError("Invalid value for `editgroup`, must not be `None`")  # noqa: E501

        self._editgroup = editgroup

    @property
    def changelog_entry(self):
        """Gets the changelog_entry of this EntityHistoryEntry.  # noqa: E501


        :return: The changelog_entry of this EntityHistoryEntry.  # noqa: E501
        :rtype: ChangelogEntry
        """
        return self._changelog_entry

    @changelog_entry.setter
    def changelog_entry(self, changelog_entry):
        """Sets the changelog_entry of this EntityHistoryEntry.


        :param changelog_entry: The changelog_entry of this EntityHistoryEntry.  # noqa: E501
        :type: ChangelogEntry
        """
        if changelog_entry is None:
            raise ValueError("Invalid value for `changelog_entry`, must not be `None`")  # noqa: E501

        self._changelog_entry = changelog_entry

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
        if not isinstance(other, EntityHistoryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
