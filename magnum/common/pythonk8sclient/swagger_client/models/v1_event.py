# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1Event(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'involved_object': 'V1ObjectReference',
            'reason': 'str',
            'message': 'str',
            'source': 'V1EventSource',
            'first_timestamp': 'str',
            'last_timestamp': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'involved_object': 'involvedObject',
            'reason': 'reason',
            'message': 'message',
            'source': 'source',
            'first_timestamp': 'firstTimestamp',
            'last_timestamp': 'lastTimestamp',
            'count': 'count'
        }

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._involved_object = None
        self._reason = None
        self._message = None
        self._source = None
        self._first_timestamp = None
        self._last_timestamp = None
        self._count = None

    @property
    def kind(self):
        """
        Gets the kind of this V1Event.
        kind of object, in CamelCase; cannot be updated; see http://releases.k8s.io/v1.0.4/docs/api-conventions.md#types-kinds

        :return: The kind of this V1Event.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1Event.
        kind of object, in CamelCase; cannot be updated; see http://releases.k8s.io/v1.0.4/docs/api-conventions.md#types-kinds

        :param kind: The kind of this V1Event.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1Event.
        version of the schema the object should have; see http://releases.k8s.io/v1.0.4/docs/api-conventions.md#resources

        :return: The api_version of this V1Event.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1Event.
        version of the schema the object should have; see http://releases.k8s.io/v1.0.4/docs/api-conventions.md#resources

        :param api_version: The api_version of this V1Event.
        :type: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1Event.
        standard object metadata; see http://releases.k8s.io/v1.0.4/docs/api-conventions.md#metadata

        :return: The metadata of this V1Event.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1Event.
        standard object metadata; see http://releases.k8s.io/v1.0.4/docs/api-conventions.md#metadata

        :param metadata: The metadata of this V1Event.
        :type: V1ObjectMeta
        """
        self._metadata = metadata

    @property
    def involved_object(self):
        """
        Gets the involved_object of this V1Event.
        object this event is about

        :return: The involved_object of this V1Event.
        :rtype: V1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """
        Sets the involved_object of this V1Event.
        object this event is about

        :param involved_object: The involved_object of this V1Event.
        :type: V1ObjectReference
        """
        self._involved_object = involved_object

    @property
    def reason(self):
        """
        Gets the reason of this V1Event.
        short, machine understandable string that gives the reason for the transition into the object's current status

        :return: The reason of this V1Event.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1Event.
        short, machine understandable string that gives the reason for the transition into the object's current status

        :param reason: The reason of this V1Event.
        :type: str
        """
        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this V1Event.
        human-readable description of the status of this operation

        :return: The message of this V1Event.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1Event.
        human-readable description of the status of this operation

        :param message: The message of this V1Event.
        :type: str
        """
        self._message = message

    @property
    def source(self):
        """
        Gets the source of this V1Event.
        component reporting this event

        :return: The source of this V1Event.
        :rtype: V1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1Event.
        component reporting this event

        :param source: The source of this V1Event.
        :type: V1EventSource
        """
        self._source = source

    @property
    def first_timestamp(self):
        """
        Gets the first_timestamp of this V1Event.
        the time at which the event was first recorded

        :return: The first_timestamp of this V1Event.
        :rtype: str
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """
        Sets the first_timestamp of this V1Event.
        the time at which the event was first recorded

        :param first_timestamp: The first_timestamp of this V1Event.
        :type: str
        """
        self._first_timestamp = first_timestamp

    @property
    def last_timestamp(self):
        """
        Gets the last_timestamp of this V1Event.
        the time at which the most recent occurance of this event was recorded

        :return: The last_timestamp of this V1Event.
        :rtype: str
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """
        Sets the last_timestamp of this V1Event.
        the time at which the most recent occurance of this event was recorded

        :param last_timestamp: The last_timestamp of this V1Event.
        :type: str
        """
        self._last_timestamp = last_timestamp

    @property
    def count(self):
        """
        Gets the count of this V1Event.
        the number of times this event has occurred

        :return: The count of this V1Event.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this V1Event.
        the number of times this event has occurred

        :param count: The count of this V1Event.
        :type: int
        """
        self._count = count

    def to_dict(self):
        """
        Return model properties dict
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
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
