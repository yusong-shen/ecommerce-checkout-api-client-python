# coding: utf-8

"""
    ECommerce Checkout Flow API

    Registration, Address Information, Delivery Options, Payment, Confirmation

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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
import re


class ProductSubTotal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, quantity=None, total_price=None, unit_price=None):
        """
        ProductSubTotal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'quantity': 'int',
            'total_price': 'str',
            'unit_price': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'quantity': 'quantity',
            'total_price': 'total_price',
            'unit_price': 'unit_price'
        }

        self._id = id
        self._quantity = quantity
        self._total_price = total_price
        self._unit_price = unit_price


    @property
    def id(self):
        """
        Gets the id of this ProductSubTotal.


        :return: The id of this ProductSubTotal.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductSubTotal.


        :param id: The id of this ProductSubTotal.
        :type: str
        """

        self._id = id

    @property
    def quantity(self):
        """
        Gets the quantity of this ProductSubTotal.


        :return: The quantity of this ProductSubTotal.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this ProductSubTotal.


        :param quantity: The quantity of this ProductSubTotal.
        :type: int
        """

        self._quantity = quantity

    @property
    def total_price(self):
        """
        Gets the total_price of this ProductSubTotal.


        :return: The total_price of this ProductSubTotal.
        :rtype: str
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """
        Sets the total_price of this ProductSubTotal.


        :param total_price: The total_price of this ProductSubTotal.
        :type: str
        """

        self._total_price = total_price

    @property
    def unit_price(self):
        """
        Gets the unit_price of this ProductSubTotal.


        :return: The unit_price of this ProductSubTotal.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this ProductSubTotal.


        :param unit_price: The unit_price of this ProductSubTotal.
        :type: str
        """

        self._unit_price = unit_price

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other