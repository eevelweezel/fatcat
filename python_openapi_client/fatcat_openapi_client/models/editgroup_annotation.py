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

from fatcat_openapi_client.models.editor import Editor  # noqa: F401,E501


class EditgroupAnnotation(object):
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
        'annotation_id': 'str',
        'editgroup_id': 'str',
        'editor_id': 'str',
        'editor': 'Editor',
        'created': 'datetime',
        'comment_markdown': 'str',
        'extra': 'object'
    }

    attribute_map = {
        'annotation_id': 'annotation_id',
        'editgroup_id': 'editgroup_id',
        'editor_id': 'editor_id',
        'editor': 'editor',
        'created': 'created',
        'comment_markdown': 'comment_markdown',
        'extra': 'extra'
    }

    def __init__(self, annotation_id=None, editgroup_id=None, editor_id=None, editor=None, created=None, comment_markdown=None, extra=None):  # noqa: E501
        """EditgroupAnnotation - a model defined in Swagger"""  # noqa: E501

        self._annotation_id = None
        self._editgroup_id = None
        self._editor_id = None
        self._editor = None
        self._created = None
        self._comment_markdown = None
        self._extra = None
        self.discriminator = None

        if annotation_id is not None:
            self.annotation_id = annotation_id
        if editgroup_id is not None:
            self.editgroup_id = editgroup_id
        if editor_id is not None:
            self.editor_id = editor_id
        if editor is not None:
            self.editor = editor
        if created is not None:
            self.created = created
        if comment_markdown is not None:
            self.comment_markdown = comment_markdown
        if extra is not None:
            self.extra = extra

    @property
    def annotation_id(self):
        """Gets the annotation_id of this EditgroupAnnotation.  # noqa: E501

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :return: The annotation_id of this EditgroupAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._annotation_id

    @annotation_id.setter
    def annotation_id(self, annotation_id):
        """Sets the annotation_id of this EditgroupAnnotation.

        UUID (lower-case, dash-separated, hex-encoded 128-bit)  # noqa: E501

        :param annotation_id: The annotation_id of this EditgroupAnnotation.  # noqa: E501
        :type: str
        """
        if annotation_id is not None and len(annotation_id) > 36:
            raise ValueError("Invalid value for `annotation_id`, length must be less than or equal to `36`")  # noqa: E501
        if annotation_id is not None and len(annotation_id) < 36:
            raise ValueError("Invalid value for `annotation_id`, length must be greater than or equal to `36`")  # noqa: E501
        if annotation_id is not None and not re.search('[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', annotation_id):  # noqa: E501
            raise ValueError("Invalid value for `annotation_id`, must be a follow pattern or equal to `/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/`")  # noqa: E501

        self._annotation_id = annotation_id

    @property
    def editgroup_id(self):
        """Gets the editgroup_id of this EditgroupAnnotation.  # noqa: E501

        Editgroup that this annotation applies to. Set automatically in creations based on URL parameter.   # noqa: E501

        :return: The editgroup_id of this EditgroupAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._editgroup_id

    @editgroup_id.setter
    def editgroup_id(self, editgroup_id):
        """Sets the editgroup_id of this EditgroupAnnotation.

        Editgroup that this annotation applies to. Set automatically in creations based on URL parameter.   # noqa: E501

        :param editgroup_id: The editgroup_id of this EditgroupAnnotation.  # noqa: E501
        :type: str
        """
        if editgroup_id is not None and len(editgroup_id) > 26:
            raise ValueError("Invalid value for `editgroup_id`, length must be less than or equal to `26`")  # noqa: E501
        if editgroup_id is not None and len(editgroup_id) < 26:
            raise ValueError("Invalid value for `editgroup_id`, length must be greater than or equal to `26`")  # noqa: E501
        if editgroup_id is not None and not re.search('[a-zA-Z2-7]{26}', editgroup_id):  # noqa: E501
            raise ValueError("Invalid value for `editgroup_id`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._editgroup_id = editgroup_id

    @property
    def editor_id(self):
        """Gets the editor_id of this EditgroupAnnotation.  # noqa: E501

        Defaults to editor created the annotation via POST request.   # noqa: E501

        :return: The editor_id of this EditgroupAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._editor_id

    @editor_id.setter
    def editor_id(self, editor_id):
        """Sets the editor_id of this EditgroupAnnotation.

        Defaults to editor created the annotation via POST request.   # noqa: E501

        :param editor_id: The editor_id of this EditgroupAnnotation.  # noqa: E501
        :type: str
        """
        if editor_id is not None and len(editor_id) > 26:
            raise ValueError("Invalid value for `editor_id`, length must be less than or equal to `26`")  # noqa: E501
        if editor_id is not None and len(editor_id) < 26:
            raise ValueError("Invalid value for `editor_id`, length must be greater than or equal to `26`")  # noqa: E501
        if editor_id is not None and not re.search('[a-zA-Z2-7]{26}', editor_id):  # noqa: E501
            raise ValueError("Invalid value for `editor_id`, must be a follow pattern or equal to `/[a-zA-Z2-7]{26}/`")  # noqa: E501

        self._editor_id = editor_id

    @property
    def editor(self):
        """Gets the editor of this EditgroupAnnotation.  # noqa: E501

        Only included in GET responses; ignored in PUT or POST requests.   # noqa: E501

        :return: The editor of this EditgroupAnnotation.  # noqa: E501
        :rtype: Editor
        """
        return self._editor

    @editor.setter
    def editor(self, editor):
        """Sets the editor of this EditgroupAnnotation.

        Only included in GET responses; ignored in PUT or POST requests.   # noqa: E501

        :param editor: The editor of this EditgroupAnnotation.  # noqa: E501
        :type: Editor
        """

        self._editor = editor

    @property
    def created(self):
        """Gets the created of this EditgroupAnnotation.  # noqa: E501

        Timestamp when annotation was first created.   # noqa: E501

        :return: The created of this EditgroupAnnotation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EditgroupAnnotation.

        Timestamp when annotation was first created.   # noqa: E501

        :param created: The created of this EditgroupAnnotation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def comment_markdown(self):
        """Gets the comment_markdown of this EditgroupAnnotation.  # noqa: E501


        :return: The comment_markdown of this EditgroupAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._comment_markdown

    @comment_markdown.setter
    def comment_markdown(self, comment_markdown):
        """Sets the comment_markdown of this EditgroupAnnotation.


        :param comment_markdown: The comment_markdown of this EditgroupAnnotation.  # noqa: E501
        :type: str
        """

        self._comment_markdown = comment_markdown

    @property
    def extra(self):
        """Gets the extra of this EditgroupAnnotation.  # noqa: E501

        Additional free-form JSON metadata that can be included as part of the annotation (or even as the primary annotation itself). See guide for details.   # noqa: E501

        :return: The extra of this EditgroupAnnotation.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this EditgroupAnnotation.

        Additional free-form JSON metadata that can be included as part of the annotation (or even as the primary annotation itself). See guide for details.   # noqa: E501

        :param extra: The extra of this EditgroupAnnotation.  # noqa: E501
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
        if not isinstance(other, EditgroupAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
